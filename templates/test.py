import pandas as pd

path = "json.json"
df = pd.read_json(path)
df_group = df.group(["DCName","DealerName","GoodsId","GoodsName"])


