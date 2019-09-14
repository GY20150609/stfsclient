# Which implementation to use, i.e. internal vs external
_INTERNAL = True

if _INTERNAL:
    from stfsclient.tensorflow_serving import internal as tensorflow_serving
else:
    # Fallback in case TensorFlow implementation is not available.
    try:
        # Tensorflow implementation
        import tensorflow as tf
        from stfsclient.tensorflow_serving import external as tensorflow_serving
        _TENSORFLOW_AVAILABLE = True
    except ImportError:
        # Internal implementation
        from stfsclient.tensorflow_serving import internal as tensorflow_serving
	    _TENSORFLOW_AVAILABLE = False

print('TensorFlow Available: {}'.format(_TENSORFLOW_AVAILABLE))
