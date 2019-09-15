_INTERNAL = True
_TENSORFLOW_AVAILABLE = False

if _INTERNAL:
    from .internal import *
else:
    # Fallback in case TensorFlow is not available.
    try:
        # Tensorflow implementation
        import tensorflow as tf
        from .external import *
        _TENSORFLOW_AVAILABLE = True
    except ImportError:
        # Internal implementation
        from .internal import *
        _TENSORFLOW_AVAILABLE = False

print("{}, using TF: {}".format(__name__, _TENSORFLOW_AVAILABLE))