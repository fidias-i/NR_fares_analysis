# Data Files Generator

# VERSION CONTROL
# v9 - correcting name of ticket type export from routes to tickets FMB

# Importing Necessary packages
import os
import pandas as pd
import numpy as np
from datetime import datetime

# -----------------------------------------------------------------------------------------------------------------------------
# Setting Directory and Data folders

base_folder = r"U:\London\Groups\Discipline Development\Rail Demand Forecasting\04 Work\09 Fares Database\01 Data\\"
os.chdir(base_folder)

data_download_info = pd.read_csv("Data Downloaded Info.csv")

database_files_folder = r"U:\London\Groups\Discipline Development\Rail Demand Forecasting\04 Work\09 Fares Database\02 Work\Database Files\\"

# -----------------------------------------------------------------------------------------------------------------------------
# For loop for all data files

now1 = datetime.now()

download_codes_list = data_download_info['Download Name'].tolist()
download_names_list = data_download_info['Folder Name'].tolist()

list_to_process = ["2023 March"]

for download_date in list_to_process:
    now2 = datetime.now()

    # Create directory
    output_folder_download = os.path.join(database_files_folder, download_date)

    if os.path.exists(output_folder_download):
        print(f"Folder for download data: {download_date} already exists")
    else:
        print(f"Starting processing the data for: {download_date}")
        os.makedirs(output_folder_download)

    match_1 = download_names_list.index(download_date)
    download_name = data_download_info['Download Name'][match_1]
    download_file_path = os.path.join(base_folder, download_date, download_name)
    os.chdir(download_file_path)

    # Module 1 - Raw Files
    # -----------------------------------------------------------------------------------------------------------------------------

    # Flows file
    flows = pd.read_csv(f"{download_name}.FFL", header=None, skiprows=6, dtype=str)
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

    flows.to_csv(f"{output_folder_download}/flows_{download_date}.csv", index=False)

    # Fares file
    fares['update_marker'] = fares[0].str[0]
    fares['flow_ID'] = fares[0].str[2:9]
    fares['fare'] = pd.to_numeric(fares[0].str[12:20])
    fares['ticket_code'] = fares[0].str[9:12]
    fares['restriction_code'] = fares[0].str[20:22]

    fares.to_csv(f"{output_folder_download}/fares_{download_date}.csv", index=False)

    # Locations file
    location = pd.read_csv(f"{download_name}.LOC", header=None, skiprows=6, dtype=str)
    location = location.iloc[:-1, :]  # Remove last row
    location['record_type'] = location[0].str[1]

    locations = location[location['record_type'] == "L"].copy()
    locations['Update_Marker'] = locations[0].str[0]
    locations['UIC_Code'] = locations[0].str[2:9]
    locations['End_Date'] = locations[0].str[9:17]
    locations['Start_Date'] = locations[0].str[17:25]
    locations['Description'] = locations[0].str[40:56]

    locations.to_csv(f"{output_folder_download}/locations_{download_date}.csv", index=False)

    # Cluster file
    cluster = pd.read_csv(f"{download_name}.Fsc", header=None, skiprows=6, dtype=str)
    cluster = cluster.iloc[:-1, :]
    cluster['cluster_ID'] = cluster[0].str[1:5]
    cluster['cluster_NLC'] = cluster[0].str[5:9]

    cluster.to_csv(f"{output_folder_download}/cluster_{download_date}.csv", index=False)

    # TOC file
    TOC_raw = pd.read_csv(f"{download_name}.TOC", header=None, skiprows=6, dtype=str)
    TOC_raw = TOC_raw.iloc[:-1, :]
    TOC_raw['record_type'] = TOC_raw[0].str[0]

    TOC = TOC_raw[TOC_raw['record_type'] == "T"].copy()
    TOC['TOC_id'] = TOC[0].str[1:3]
    TOC['TOC_name'] = TOC[0].str[3:33]

    TOC.to_csv(f"{output_folder_download}/TOC_record_{download_date}.csv", index=False)

    # Ticket types file
    ticket_types = pd.read_csv(f"{download_name}.TTY", header=None, skiprows=6, dtype=str)
    ticket_types['record_type'] = ticket_types[0].str[0]
    ticket_types['ticket_code'] = ticket_types[0].str[1:4]
    ticket_types['ticket_code_desc'] = ticket_types[0].str[28:43]
    ticket_types['ticket_type'] = ticket_types[0].str[44]

    ticket_types.to_csv(f"{output_folder_download}/ticket_{download_date}.csv", index=False)

    # Joining fares and flow
    flows_fares = pd.merge(flows, fares, on="flow_ID", how="left")
    flows_fares['OD_flow'] = flows_fares['origin_code'] + "-" + flows_fares['dest_code']

    flows_fares.to_csv(f"{output_folder_download}/flows_fares_{download_date}.csv", index=False)
