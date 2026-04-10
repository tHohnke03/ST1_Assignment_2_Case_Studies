from tensorflow import keras
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train_f = x_train.astype('float32')
mean = x_train_f.mean()
std = x_train_f.std()

x_train_std = (x_train_f - mean) / std
x_test_std = (x_test.astype('float32') - mean) / std

print("After standardization:")
print("Mean:", x_train_std.mean())
print("Std:", x_train_std.std())
print("Min:", x_train_std.min())
print("Max:", x_train_std.max())
