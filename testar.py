import pandas as pd

loop = 0

df = pd.DataFrame()

while True:
    loop = loop + 1
    df = df.append({'Loop': [loop]}, ignore_index=True)

    if loop >= 32:
        break

v