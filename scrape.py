# Width – 185, Aspect Ratio – 16, Rim Size – 14

import re
import json
import requests
import pandas as pd


url = "https://www.dexel.co.uk/shopping/tyre-results?width=185&profile160&rim=14&speed=."

data = json.loads(
    re.search(r"allTyres = (.*);", requests.get(url).text).group(1)
)

# uncomment to print all data:
# print(json.dumps(data, indent=4))

df = pd.DataFrame(data)
print(df.head())

df = df[["manufacturer", "description", "winter", "summer", "price"]]
df.to_csv("data.csv", index=False)
