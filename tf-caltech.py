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
                                 model_dir='ct_model',
                                 activation_fn=tf.nn.sigmoid,
                                 hidden_units=[10, 20, 10], n_classes=2)
classifier.fit(data, labels, batch_size=200, steps=10000)
result = classifier.evaluate(test_data, test_labels)
print 'recall'
print result['recall/positive_threshold_0.500000_mean']
print 'accuracy'
print result["accuracy"]

