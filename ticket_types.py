import os
import pandas as pd
import numpy as np
from datetime import datetime

_dir = os.listdir('fares')
download_name = _dir[0][:-4]
download_date = '2025 Jan'

# Ticket types file
ticket_types = pd.read_csv(os.path.join('fares',f"{download_name}.TTY"), header=None, skiprows=6, dtype=str)
ticket_types['record_type'] = ticket_types[0].str[0:1]
ticket_types['ticket_code'] = ticket_types[0].str[1:4]
ticket_types['end_date'] = ticket_types[0].str[4:12]
ticket_types['start_date'] = ticket_types[0].str[12:20]
ticket_types['quote_date'] = ticket_types[0].str[20:28]
ticket_types['ticket_code_desc'] = ticket_types[0].str[28:43].str.strip()
ticket_types['ticket_class'] = ticket_types[0].str[43:44]
ticket_types['ticket_type'] = ticket_types[0].str[44:45]
ticket_types['ticket_group'] = ticket_types[0].str[45:46]
ticket_types['last_valid_day'] = ticket_types[0].str[46:54]
ticket_types['max_passengers'] = ticket_types[0].str[54:57]
ticket_types['min_passengers'] = ticket_types[0].str[57:60]
ticket_types['max_adults'] = ticket_types[0].str[60:63]
ticket_types['min_adults'] = ticket_types[0].str[63:66]
ticket_types['restricted_by_date'] = ticket_types[0].str[72:73]
ticket_types['restricted_by_train'] = ticket_types[0].str[73:74]
ticket_types['restricted_by_area'] = ticket_types[0].str[74:75]
ticket_types['validity_code'] = ticket_types[0].str[74:75]
ticket_types['reservation_required'] = ticket_types[0].str[98:99]
ticket_types['discount_category'] = ticket_types[0].str[111:113]

# --------------------------
# Adding descriptive fields
ticket_types['ticket_type_desc'] = ticket_types['ticket_type'].map({
    "S": "Single",
    "R": "Return",
    "N": "Season"
})

ticket_types['ticket_type_group_desc'] = ticket_types['ticket_group'].map({
    "F": "First",
    "S": "Standard",
    "P": "Promotion",
    "E": "Euro"
})

ticket_types['reservation_required_desc'] = ticket_types['reservation_required'].map({
    "N": "No",
    "O": "reservation on outward",
    "R": "reservation on return",
    "B": "both",
    "E": "Euro"
})

# --------------------------
# Drop the original column and save to CSV
ticket_types.drop(columns=[0], inplace=True)

ticket_types_file_path = os.path.join(f"ticket_{download_date}.csv")
ticket_types.to_csv(ticket_types_file_path, index=False)