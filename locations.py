import pandas as pd
import os


_dir = os.listdir('fares')
download_name = _dir[0][:-4]

# Locations file
location = pd.read_csv(os.path.join('fares',f"{download_name}.LOC"), header=None, skiprows=6, dtype=str)
location = location.iloc[:-1, :] # Remove last row
location['record_type'] = location[0].str[1]

locations = location[location['record_type'] == "L"].copy()
locations['Update_Marker'] = locations[0].str[0]
locations['UIC_Code'] = locations[0].str[2:9]
locations['End_Date'] = locations[0].str[9:17]
locations['Start_Date'] = locations[0].str[17:25]
locations['Description'] = locations[0].str[40:56]

locations.to_csv(f"locations.csv", index=False)