if stfsclient._INTERNAL:
    import stfsclient.tensorflow_serving.internal import as tensorflow_serving
else:
    # Fallback in case TensorFlow implementation is not available.
    try:
        # Tensorflow implementation
        import tensorflow as tf
        import stfsclient.tensorflow_serving.external import as tensorflow_serving
        _TENSORFLOW_AVAILABLE = True
except ImportError:
    # Internal implementation
    import stfsclient.tensorflow_serving.internal import as tensorflow_serving
	_TENSORFLOW_AVAILABLE = False

stfsclient._TENSORFLOW_AVAILABLE = _TENSORFLOW_AVAILABLE

print('TensorFlow Available: {}'.format(stfsclient._TENSORFLOW_AVAILABLE))
