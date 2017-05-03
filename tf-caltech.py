import numpy as np
import tensorflow as tf

from data import read_caltech

learn = tf.contrib.learn
tf.logging.set_verbosity(tf.logging.ERROR)

data, labels, test_data, test_labels = read_caltech()
data = np.asarray(data, dtype=np.float32)
labels = np.asarray(labels, dtype=np.int32)
test_data = np.asarray(test_data, dtype=np.float32)
test_labels = np.asarray(test_labels, dtype=np.int32)

feature_columns = learn.infer_real_valued_columns_from_input(data)
classifier = learn.DNNClassifier(feature_columns=feature_columns,
                                 activation_fn=tf.nn.sigmoid,
                                 hidden_units=[40, 20, 10, 5], n_classes=2)
classifier.fit(data, labels, batch_size=200, steps=10000)
result = classifier.evaluate(test_data, test_labels)
print result["accuracy"]

