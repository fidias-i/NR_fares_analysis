import os
import pandas as pd
import numpy as np
from datetime import datetime

_dir = os.listdir('fares')
download_name = _dir[0][:-4]

# TOC file
TOC_raw = pd.read_csv(os.path.join('fares',f"{download_name}.TOC"), header=None, skiprows=6, dtype=str)
TOC_raw = TOC_raw.iloc[:-1, :]
TOC_raw['record_type'] = TOC_raw[0].str[0]

TOC = TOC_raw[TOC_raw['record_type'] == "T"].copy()
TOC['TOC_id'] = TOC[0].str[1:3]
TOC['TOC_name'] = TOC[0].str[3:33]

TOC.to_csv(f"TOC_record_.csv", index=False)