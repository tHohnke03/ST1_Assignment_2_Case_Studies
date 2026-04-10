from tensorflow import keras
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train_f = x_train.astype('float32')
mean = x_train_f.mean()
x_train_centered = x_train_f - mean
x_test_centered = x_test.astype('float32') - mean

print("After centering:")
print("Mean:", x_train_centered.mean())
print("Min:", x_train_centered.min())
print("Max:", x_train_centered.max())
