import os
import pandas as pd
import numpy as np
from datetime import datetime

_dir = os.listdir('fares')
download_name = _dir[0][:-4]
download_date = '2025 Jan'

# TOC file
TOC_raw = pd.read_csv(os.path.join('fares',f"{download_name}.TOC"), header=None, skiprows=6, dtype=str)
TOC_raw = TOC_raw.iloc[:-1, :]
TOC_raw['record_type'] = TOC_raw[0].str[0]

TOC = TOC_raw[TOC_raw['record_type'] == "T"].copy()
TOC['TOC_id'] = TOC[0].str[1:3]
TOC['TOC_name'] = TOC[0].str[3:33].str.strip()  # Strip to remove extra spaces
TOC['reservation_system'] = TOC[0].str[33:41].str.strip()
TOC['active_indicator'] = TOC[0].str[41:42]

TOC.to_csv(f"TOC_record_{download_date}.csv", index=False)


# Fare TOC Record
Fare_TOC = TOC_raw[TOC_raw['record_type'] == "F"].copy()

# Extract columns
Fare_TOC['fare_TOC_id'] = Fare_TOC[0].str[1:4]
Fare_TOC['TOC_id'] = Fare_TOC[0].str[4:6]
Fare_TOC['fare_TOC_name'] = Fare_TOC[0].str[6:36].str.strip()

# Drop the original column
Fare_TOC.drop(columns=[0], inplace=True)

# Save Fare TOC records to CSV
Fare_TOC_file_path = os.path.join(f"Fare_TOC_record_{download_date}.csv")
Fare_TOC.to_csv(Fare_TOC_file_path, index=False)

# --------------------------
# TOC Map
TOC_map = Fare_TOC.drop(columns=['record_type']).drop_duplicates()
TOC_map['TOC'] = TOC_map['fare_TOC_id']
