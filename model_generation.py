import numpy
import sys

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

# STOLEN FROM THE INTERNET


def generate_lstm(filename):
    text = open(filename).read()
    chars = sorted(list(set(text)))
    char_map = dict((c, i) for i, c in enumerate(chars))
    characters = len(text)
    letters = len(chars)

    seq_length = 1000
    dataX = []
    dataY = []
    for i in range(0, characters - seq_length, 1):
        seq_in = text[i:i + seq_length]
        seq_out = text[i + seq_length]
        dataX.append([char_map[char] for char in seq_in])
        dataY.append(char_map[seq_out])

    n_patterns = len(dataX)
    X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
    X = X / float(letters)
    y = np_utils.to_categorical(dataY)

    lstm = Sequential()
    lstm.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
    lstm.add(Dropout(0.2))
    lstm.add(Dense(y.shape[1], activation='softmax'))
    lstm.compile(loss='categorical_crossentropy', optimizer='adam')

    filepath = "text-model-{epoch:02d}-{loss:.4f}.hdf5"
    checkpoint = ModelCheckpoint(
        filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]

    lstm.fit(X, y, epochs=20, batch_size=128, callbacks=callbacks_list)


def text_generation():
    filename = "weights-improvement-01-3.0053.hdf5"
    text = open("text.txt").read()
    chars = sorted(list(set(text)))
    char_map = dict((c, i) for i, c in enumerate(chars))
    characters = len(text)
    letters = len(chars)

    seq_length = 1000
    dataX = []
    dataY = []
    for i in range(0, characters - seq_length, 1):
        seq_in = text[i:i + seq_length]
        seq_out = text[i + seq_length]
        dataX.append([char_map[char] for char in seq_in])
        dataY.append(char_map[seq_out])

    n_patterns = len(dataX)
    X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
    X = X / float(letters)
    y = np_utils.to_categorical(dataY)

    model = Sequential()
    model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
    model.add(Dropout(0.2))
    model.add(Dense(y.shape[1], activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    model.load_weights(filename)
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    int_to_char = dict((i, c) for i, c in enumerate(chars))

    # pick a random seed
    start = numpy.random.randint(0, len(dataX) - 1)
    pattern = dataX[start]
    print("Seed:")
    print("\"", ''.join([int_to_char[value] for value in pattern]), "\"")
    # generate characters
    for i in range(1000):
        x = numpy.reshape(pattern, (1, len(pattern), 1))
        #x = x / float(n_vocab)
        x = x / float(letters)
        prediction = model.predict(x, verbose=0)
        index = numpy.argmax(prediction)
        result = int_to_char[index]
        seq_in = [int_to_char[value] for value in pattern]
        sys.stdout.write(result)
        pattern.append(index)
        pattern = pattern[1:len(pattern)]
    print("\nDone.")


if __name__ == "__main__":
    # execute only if run as a script
    generate_lstm("text.txt")
