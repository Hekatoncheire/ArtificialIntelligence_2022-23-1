import pandas as pd
import numpy as np

df = pd.read_csv("ip.txt", header=None, dtype="string")
print(df.shape[0], "sor van a fájlban")

ips = df.squeeze()

doc_ips_count = np.sum(ips.str.startswith("2001:0db8", na=False))
global_ips_count = np.sum(ips.str.startswith("2001:0e", na=False))
local_ips_count = np.sum(ips.str.startswith(
    "fc", na=False)) + np.sum(ips.str.startswith("fd", na=False))

print(doc_ips_count, "dokumentációs-,", global_ips_count,
      "globális-, és", local_ips_count, "lokális IP cím van")
