_INTERNAL = True
_TENSORFLOW_AVAILABLE = False

if _INTERNAL:
    from .tensor_util import make_ndarray, make_tensor_proto
else:
    # Fallback in case tensorflow library is not available.
    try:
        # Tensorflow implementation
        from tensorflow import make_ndarray, make_tensor_proto
        _TENSORFLOW_AVAILABLE = True
    except ImportError:
        # Internal implementation
        from .tensor_util import make_ndarray, make_tensor_proto
	    _TENSORFLOW_AVAILABLE = False

print("{}, using TF: {}".format(__name__, _TENSORFLOW_AVAILABLE))
