# Fallback in case tensorflow library is not available.
try:
    # Tensorflow implementation
    import tensorflow as tf
    make_ndarray = tf.make_ndarray
    make_tensor_proto = tf.make_tensor_proto
    _TENSORFLOW_AVAILABLE = True
except ImportError:
    # Internal implementation
    from tf.python.framework.tensor_util as MakeTensorProto, MakeNdarray
    import stfsclient.tensorflow_serving.internal import as tensorflow_serving
    make_ndarray = MakeNdarray
    make_tensor_proto = MakeTensorProto
	_TENSORFLOW_AVAILABLE = False

# Fallback in case tensorflow library is not available.
try:
	from tensorflow.contrib.util import make_tensor_proto, make_ndarray
	# Tensorflow implementation
	_TENSORFLOW_AVAILABLE = True
except ImportError:
	from stfsclient.tensorflow.python.framework.tensor_util import MakeTensorProto, MakeNdarray
	# Internal implementation
	_TENSORFLOW_AVAILABLE = False

print("Tensorflow Library Available: {}".format(_TENSORFLOW_AVAILABLE))

def _make_tensor_proto(values, dtype=None, shape=None, verify_shape=False, allow_broadcast=False):
    if _TENSORFLOW_AVAILABLE:
        return make_tensor_proto(values, dtype, shape, verify_shape, allow_broadcast)
    return MakeTensorProto(values, dtype)

def _make_ndarray(tensor):
	if _TENSORFLOW_AVAILABLE:
		return make_ndarray(tensor)
	return MakeNdarray(tensor)
