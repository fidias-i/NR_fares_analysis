import os
import pandas as pd
import numpy as np
from datetime import datetime

_dir = os.listdir('fares')
download_name = _dir[0][:-4]
download_date = '2025 Jan'


# Cluster file
cluster = pd.read_csv(os.path.join('fares',f"{download_name}.fsc"), header=None, skiprows=6, dtype=str)
cluster = cluster.iloc[:-1, :]
cluster['cluster_ID'] = cluster[0].str[1:5]
cluster['cluster_NLC'] = cluster[0].str[5:9]
cluster.drop(columns=[0], inplace=True)

cluster.to_csv(f"cluster_{download_date}.csv", index=False)