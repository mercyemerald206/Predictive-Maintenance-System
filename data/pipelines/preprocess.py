import pandas as pd

df = pd.read_csv("data/sensor_data.csv")

df["temp_avg"] = df["temperature"].rolling(2).mean()
df["volt_avg"] = df["voltage"].rolling(2).mean()

df.dropna(inplace=True)

df.to_csv("data/processed.csv", index=False)
print("Preprocessing done.")
