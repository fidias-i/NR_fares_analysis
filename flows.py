# Importing Necessary packages
import os
import pandas as pd
import numpy as np
from datetime import datetime 

_dir = os.listdir('fares')
download_name = _dir[0][:-4]


 # Module 1 - Raw Files
# -----------------------------------------------------------------------------------------------------------------------------

# Flows file
flows = pd.read_csv(os.path.join('fares',f"{download_name}.FFL"), header=None, skiprows=6, dtype=str)
flows = flows.iloc[:-1, :]  # Remove last row
flows['update_marker'] = flows[0].str[0]
flows['record_type'] = flows[0].str[1]

fares = flows[flows['record_type'] == "T"].copy()
flows = flows[flows['record_type'] == "F"].copy()

flows['origin_code'] = flows[0].str[2:6]
flows['dest_code'] = flows[0].str[6:10]
flows['route_code'] = flows[0].str[10:15]
flows['status_code'] = flows[0].str[15:18]
flows['usage_code'] = flows[0].str[18]
flows['direction'] = flows[0].str[19]
flows['end_date'] = flows[0].str[20:28]
flows['start_date'] = flows[0].str[28:36]
flows['TOC'] = flows[0].str[36:39]
flows['cross_london_ind'] = flows[0].str[39]
flows['NS_disc_ind'] = flows[0].str[40]
flows['publication_ind'] = flows[0].str[41]
flows['flow_ID'] = flows[0].str[42:49]
flows.drop(columns=[0], inplace=True)

flows.to_csv(f"flows.csv", index=False)

# Fares file
fares['update_marker'] = fares[0].str[0]
fares['flow_ID'] = fares[0].str[2:9]
fares['fare'] = pd.to_numeric(fares[0].str[12:20])
fares['ticket_code'] = fares[0].str[9:12]
fares['restriction_code'] = fares[0].str[20:22]

fares.to_csv(f"fares.csv", index=False)