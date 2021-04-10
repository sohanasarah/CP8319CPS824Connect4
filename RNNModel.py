import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical
from tensorflow.keras.layers import LSTM, Dropout, Dense, Embedding
from keras.layers import Dense, Activation
from keras.utils.vis_utils import plot_model
import keras
from keras.layers import Dropout
class ConnectFourModelRNN:

    def __init__(self, numberOfInputs, numberOfOutputs, batchSize, epochs):
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.batchSize = batchSize
        self.epochs = epochs
        
        self.model = Sequential()
        self.model.add(LSTM(42, return_sequences=True, 
               dropout=0.1, recurrent_dropout=0.1, input_shape=(1,numberOfInputs)))
        self.model.add(Dense(64, activation='relu'))

        self.model.add(Dense(numberOfOutputs, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer="nadam", metrics=['accuracy'])

    def getModel(self):
        return self.model
    
    def train(self, dataset):
        input = []
        output = []
        
        for data in dataset:
            input.append(data[1])
            output.append(data[0])

        X = np.array(input).reshape((-1, self.numberOfInputs))

        y = to_categorical(output, num_classes=3)
        limit = int(0.7 * len(X))
        X_train = X[:limit]
        
        X_train = X_train[:, np.newaxis, :]
        print(X_train.shape)

        X_test = X[limit:]
        y_train = y[:limit]
        y_test = y[limit:]
        X_test = X_test[:, np.newaxis, :]
        y_train = y_train[:, np.newaxis, :]
        y_test = y_test[:, np.newaxis, :]



        self.model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=self.epochs, batch_size=self.batchSize)

    def predict(self, data, index):
        d = np.array(data).reshape(-1, self.numberOfInputs)
        d=d[:, np.newaxis, :]
        return self.model.predict(d)[0][0][index]