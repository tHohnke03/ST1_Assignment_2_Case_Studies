from tensorflow import keras
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train_norm = x_train.astype('float32') / 255.0
x_test_norm = x_test.astype('float32') / 255.0

print("After normalization:")
print("Min:", x_train_norm.min())
print("Max:", x_train_norm.max())
print("Mean:", x_train_norm.mean())
