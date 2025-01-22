import pandas as pd
import os


_dir = os.listdir('fares')
download_name = _dir[0][:-4]
download_date = '2025 Jan'

# --------------------------
# Reading the ROUTE file
route = pd.read_csv(os.path.join('fares',f"{download_name}.RTE"), sep=None, header=None, skiprows=6, engine='python', dtype=str)
# Assuming `download_name`, `download_date`, and `output_folder_download` are defined
file_path = os.path.join('fares', f"{download_name}.RTE")

# Read the fixed-width file
route = pd.read_fwf(
    file_path,
    widths=[1, 1, 5, 8, 8, 16],  # Specify column widths
    header=None,
    skiprows=6,
    dtype=str
)


# Remove the last row if needed
route = route.iloc[:-1, :]

# Add meaningful column names
route.columns = ['record_type_prefix', 'record_type', 'route_code', 'end_date', 'start_date', 'route_description']

# Filter for "R" record type
route = route[route['record_type'] == "R"].copy()

# Clean up and process further
route['route_code'] = route['route_code'].str.strip()
route['end_date'] = route['end_date'].str.strip()
route['start_date'] = route['start_date'].str.strip()
route['route_description'] = route['route_description'].str.strip()

# Drop unnecessary columns
route.drop(columns=['record_type_prefix', 'record_type'], inplace=True)

# Save to CSV
output_file = os.path.join(f"route_{download_date}.csv")
route.to_csv(output_file, index=False)
# Remove the last row
route = route.iloc[:-1, :]

# Add the record_type column
route['record_type'] = route[0].str[1:2]

# --------------------------
# Filter for "R" record types
route = route[route['record_type'] == "R"].copy()

# Extract columns
route['route_code'] = route[0].str[2:7]
route['end_date'] = route[0].str[7:15]
route['start_date'] = route[0].str[15:23]
route['route_description'] = route[0].str[31:47].str.strip()  # Strip to remove extra spaces

# Drop unnecessary columns
route.drop(columns=[0, 'record_type'], inplace=True)

# Save to CSV
route_file_path = os.path.join(f"route_{download_date}.csv")
route.to_csv(route_file_path, index=False)
