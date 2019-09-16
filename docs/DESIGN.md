# **Design** Considerations and Decisions

**Note:**  
1. `pb` refers to raw protocol buffer object.
2. wrapped `pb` refers to a wrapped protocol buffer object.

## Design Aspirations:

- Provide a common name-space for invoking gRPC and REST APIs in Tensorflow Serving.
- Create a common abstraction layer for working with protocol buffer definitions in TensorFlow Serving.

## Motivation

I ask myself this now and then, so once for all, I'm putting it **down** in *mark____*.  ;P

-  Working with `pb` should be simple. It is and it isn't. 
- Tensorflow Serving provides [gRPC client API](https://github.com/tensorflow/serving/tree/master/tensorflow_serving/apis), but leaves implementation as an exercise for the user. Plus, there is little available, mostly sparse, reference for implementing the gRPC clients for TensorFlow Serving.

The repo started as a by-product of working with Tensorflow Serving, mostly focusing on implementing a distributed serving mechanism for all models [Tensorflow](https://www.tensorflow.org/) and otherwise.

## Simplicity and Customisation

The wrapper provides one-line invocation for many useful  `pb` functions as well as provides custom methods for specific `pb` message/service definitions found in the `tensorflow_serving` library.

Most of the methods that accept a wrapped `pb` also work fine with the pure `pb`.

## Getting and Setting attributes

Simplifying interface for getting/setting some complex `attr`s, like nested `pb` messages, that can't be set directly is done by writing custom `getter` and `setter` methods for the respective attributes in the derived class.

This makes sense, since each `pb` definition is different and hence needs to be handled differently.

## API consistency

The library abstracts away working directly with `pb`. It does so by providing a wrapper class around each definition.

As a principle, it doesn't expect the user to work with `pb` directly, even though that's an option, but instead work with the abstraction layer provided as part of the library. 

This is especially true while returning a child `pb` from inside a parent `pb`. The nested `pb` is wrapped in a corresponding class to provide a consistent API.

## Mirroring

In order to provide API consistency, without breaking features that made working with `pb` great in the first place,  we simply *mirror* the ***internal*** (part of the internal `pb` message) nested `pb` message attribute to an ***external*** (part of the wrapper, but outside of the internal `pb` object) `pb` wrapped message attribute. 

The external attribute is attached to the parent `pb` wrapper message, in a way so as to reflect any changes in the internal `pb` state, i.e. through chained assignment. 

This only applies to non-scalar (singular and repeated) fields, a.k.a. the message and repeated message types.  For scalar (singular or repeated) fields, the `getter` and `setter` methods directly exposes the internal `pb` state.

## Chained Assignment

Here's an example to explain what chained assignment looks like. Let's say we want to initialise a predict request. It goes something like this:

```python
model_spec = ModelSpec(name='mnist', signature_name='serving_default', version=1)
predict_request = PredictRequest(model_spec=model_spec, input_tensor=None)
```

Now, let's say we wanted to update the some `model_spec` attribute before sending the request. This can be done in two ways:

**A)** Update `model_spec` and update the `model_spec` attribute in `predict_request`.

```python
model_spec.version = 2
predict_request.model_spec = model_spec
```

**B)** Update the attribute directly using chained assignment in `predict_request`, and this should directly reflect in the `predict_request` instance.

```python
predict_request.model_spec.version = 2
```

Method **B)** is what is referred to as ***chain assignment***. 

What's the *big* difference? Mainly *two*: 

1. Chain assignment is intrinsically supported in the `pb` python library.
2. It provides a more fine-grained control over the internal attributes space of wrapped `pb` message objects.

This is achieved by using a simple pointer-style reference to update the parent `pb` wrapper object whenever an attribute is changed on the nested `pb` wrapper object using a `setter` method.

**Psst...** *However, I personally, prefer method **A)**, because it's more explicit that way. It can be argued that there's not much use for method **B)** , however, it allows us to set some long winded nested dependency in a single easy declaration, without having to tweak other attributes, especially while testing.*

*I'll be looking into removing it in the future, if the need arises.*

## Response messages and wrappers

Response `pb`  shouldn't be modifiable unless we want to insert some business logic into it and thereby transform it for later consumption. Therefore, response wrappers provide a non-mutable interface to the underlying response `pb` .

However, modifications can still be made to internal `pb` directly, thereby, making changes more explicit.

## Catching Errors

Since, `google.protobuf.message` takes care of handling most of the errors, it shouldn't be a problem. 

IMO, letting  errors percolate with sensible warnings should be the way to go, i.e. shouldn't cause the user to go mad. 

## TensorFlow Backend

The library works in two different modes, i.e. internal or using Tensorflow backend. You cannot mix importing internal backend while also importing TensorFlow library, as this leads to collision in the `protobuf ` definitions shared by the two libraries. You can import the TensorFlow backend, which will prevent this at the cost of locking you into the TensorFlow implementation, i.e. relying on TensorFlow.

## Limitations

1. Currently, the main limitation is in the form of chained assignment on items inside `MessageList` container. `MessageList` container wraps around repeated message type (objects that are sometimes found in a `pb` definition) which for almost all purposes act like a python `list` object.

2. Another limitation is the current dependency on TensorFlow library for converting `np.array` inputs to `tensor_proto` and vice-versa. Though, the code for the has been divorced from the TensorFlow library, some dependencies are too long or complicated to trace back and support. Therefore, right now a simple adaptation of the code is used, where required, falling back on the TensorFlow implementation if installed.
