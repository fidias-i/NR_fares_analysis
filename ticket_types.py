import os
import pandas as pd
import numpy as np
from datetime import datetime

_dir = os.listdir('fares')
download_name = _dir[0][:-4]

# Ticket types file
ticket_types = pd.read_csv(os.path.join('fares',f"{download_name}.TTY"), header=None, skiprows=6, dtype=str)
ticket_types['record_type'] = ticket_types[0].str[0]
ticket_types['ticket_code'] = ticket_types[0].str[1:4]
ticket_types['ticket_code_desc'] = ticket_types[0].str[28:43]
ticket_types['ticket_type'] = ticket_types[0].str[44]

ticket_types.to_csv(f"ticket.csv", index=False)