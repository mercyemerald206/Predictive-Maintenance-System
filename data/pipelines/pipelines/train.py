import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

df = pd.read_csv("data/processed.csv")

X = df[["temp_avg", "volt_avg"]].values
y = df["failure"].values

X = X.reshape((X.shape[0], 1, X.shape[1]))

model = Sequential([
    LSTM(32, input_shape=(1, 2)),
    Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy")
model.fit(X, y, epochs=5)

model.save("model/lstm_model.h5")
