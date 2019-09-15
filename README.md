# Simple TensorFlow Serving Client

A simple, consolidated [gRPC](https://grpc.io/)-based client wrapper for querying a hosted TensorFlow Model Server.

**What it does?**

- It simplifies working with [protocol buffers](https://developers.google.com/protocol-buffers/) and provides custom functions for working with `protobuf` APIs (i.e. messages and services) inside [Tensorflow Serving](https://www.tensorflow.org/tfx/guide/serving), all without leaving the comfort of python. 

- Implements gRPC client stubs for `GetModelMetadata`, `GetModelStatus`, `HandleReloadConfig` and `Predict` APIs (more to come, including some custom ones).

- It requires only the minimum dependencies, i.e. numpy, grpcio, protobuf making it very light to install on memory constrained edge devices, such as [Raspberry Pi](https://www.raspberrypi.org/), [NVIDIA Jetson](https://developer.nvidia.com/embedded/jetson-nano-developer-kit), etc.

For a more detailed reference, [click here](./docs/DESIGN.md).

## Installation

### Client

Clone the repository and run ;

```bash
cd stfsclient
pip install .
```
or 

```bash
pip install git+https://github.com/jagans94/stfsclient.git
```

for just the package.

### `tensorflow_model_server` 

**Note:** Run as `sudo`; only works on Debian/Ubuntu

```bash
echo "deb http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | tee /etc/apt/sources.list.d/tensorflow-serving.list && \
curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add -
apt update
apt-get install tensorflow-model-server
```

## Tutorial

Refer here for the most up-to-date [tutorial.](./extras/tutorial/simple_tutorial.ipynb)

## Benchmark

![](./docs/latency_profile_mnist.png)

​      			Prediction latency on 10,000 images with batch sizes 1, 4, 8, and 16 on MNIST data set! :) 

**Conclusion:** gRPC predict requests have a lot smaller latency profile and are approx. 6 times faster compared with REST based predict requests 

**Note:** Code for bench marking can be found at  [extras/benchmarks.](./extras/benchmarks)

## Contributions

Want to add a feature that's not in here or implement [one of these](./docs/TODO.md). Raise an **Issue** or better yet **PR**. ;)

## Copyright

Copyright 2019 onward. Licensed under the MIT License; you may not use this project's files except in compliance with the License. A copy of the License is provided in the [LICENSE](./LICENSE) file in this repository.

