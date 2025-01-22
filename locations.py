import pandas as pd
import os


_dir = os.listdir('fares')
download_name = _dir[0][:-4]
download_date = '2025 Jan'

# Locations file
location = pd.read_csv(os.path.join('fares',f"{download_name}.LOC"), header=None, skiprows=6, dtype=str)

# Remove the last row
location = location.iloc[:-1, :]

# Add 'recordtype' column
location['recordtype'] = location[0].str[1]

# Filter rows where recordtype == "L"
locations = location[location['recordtype'] == "L"].copy()

# Add columns to locations
locations['Update_Marker'] = locations[0].str[0]
locations['Record_Type'] = locations[0].str[1]
locations['UIC_Code'] = locations[0].str[2:9]
locations['End_Date'] = locations[0].str[9:17]
locations['Start_Date'] = locations[0].str[17:25]
locations['Quote_Date'] = locations[0].str[25:33]
locations['Admin_Area_Code'] = locations[0].str[33:36]
locations['NLC_Code'] = locations[0].str[36:40]
locations['Description'] = locations[0].str[40:56]
locations['CRS_Code'] = locations[0].str[56:59]
locations['Resv_Code'] = locations[0].str[59:64]
locations['Ers_Country'] = locations[0].str[64:66]
locations['Ers_Code'] = locations[0].str[66:69]
locations['Fare_Group'] = locations[0].str[69:75]
locations['County'] = locations[0].str[75:77]
locations['PTE_Code'] = locations[0].str[77:79]
locations['Zone_No'] = locations[0].str[79:83]
locations['Zone_ID'] = locations[0].str[83:85]
locations['Region'] = locations[0].str[85:86]
locations['Hierarchy'] = locations[0].str[86:87]
locations['CC_Desc_Out'] = locations[0].str[87:128]
locations['CC_Desc_RTN'] = locations[0].str[128:144]
locations['ATB_Desc_Out'] = locations[0].str[144:204]
locations['ATB_Des_RTN'] = locations[0].str[204:234]
locations['Special_Facilities'] = locations[0].str[234:260]
locations['LUL_Direction_ind'] = locations[0].str[260:261]
locations['LUL_UTS_MODE'] = locations[0].str[261:262]
locations['LUL_Zone_1'] = locations[0].str[262:263]
locations['LUL_Zone_2'] = locations[0].str[263:264]
locations['LUL_Zone_3'] = locations[0].str[264:265]
locations['LUL_Zone_4'] = locations[0].str[265:266]
locations['LUL_Zone_5'] = locations[0].str[266:267]
locations['LUL_Zone_6'] = locations[0].str[267:268]
locations['LUL_UTS_London_Station'] = locations[0].str[268:269]
locations['UTS_Code'] = locations[0].str[269:270]
locations['UTS_A_Code'] = locations[0].str[270:273]
locations['UTS_PTR_Bias'] = locations[0].str[273:274]
locations['UTS_Offset'] = locations[0].str[274:275]
locations['UTS_North'] = locations[0].str[275:278]
locations['UTS_East'] = locations[0].str[278:281]
locations['UTS_South'] = locations[0].str[281:284]
locations['UTS_West'] = locations[0].str[284:287]

# Drop the original column
locations.drop(columns=[0], inplace=True)
locations.to_csv(f"locations_{download_date}.csv", index=False)