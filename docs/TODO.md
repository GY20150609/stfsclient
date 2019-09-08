## To Do

The basic implementation is almost complete. However, there are some add-ons that would be well worth expanding on, such as:

### General

- [ ] Documentation

### Message

- [ ] Reduce replicated `property` logic by defining custom [descriptors](https://docs.python.org/3/howto/descriptor.html).
- [ ] Implement `Classify`,  `Regress` and `MultiInference` APIs.
- [ ] Write test script for expected behaviours for each wrapper class as well as a generic test suite covering the base class implementation.
- [ ] Add parser for reading `signature_def` from  `GetModelMetadataResponse`.
- [ ] Extend `tensor_proto` conversion utilities to fully support all operations supported natively in TensorFlow.

### gRPC

- [ ] Add examples for asynchronous requests.
- [ ] Create a gRPC service for downloading a model from a blob store on client request. 
- [ ] Create  gRPC service for querying latest versions available from a blob store and making them available automatically, based on policy, etc.
- [ ] Support authentication (gRPC already supports authentication. However, the wrapper around the gRPC client services uses `insecure_channel` for communication. Ideally, I'd like to extend authentication support for  both client, i.e. this library and server, i.e. hosted  `tensorflow_model_server` using the many already in-built authentication mechanisms as well as custom plugins)
- [ ] Add more bench-marking tests for gRPC vs REST API endpoints.
