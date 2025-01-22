import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("fares_database.db")
cursor = conn.cursor()

# Create FLOW table
cursor.execute("""
CREATE TABLE IF NOT EXISTS FLOW (
    FLOW_ID TEXT PRIMARY KEY,       -- Unique identifier for the flow
    UPDATE_MARKER TEXT,             -- 'I', 'A', or 'D' for changes; 'R' for full refresh
    RECORD_TYPE TEXT,               -- Record type ('F' for Flow records)
    ORIGIN_CODE TEXT,               -- Origin location code
    DEST_CODE TEXT,                 -- Destination location code
    ROUTE_CODE TEXT,                -- Route code
    STATUS_CODE TEXT,               -- Status code
    USAGE_CODE TEXT,                -- Usage indicator ('A' for actual, 'G' for generated)
    DIRECTION TEXT,                 -- Direction indicator ('S' or 'R')
    END_DATE TEXT,                  -- End date (format: YYYYMMDD)
    START_DATE TEXT,                -- Start date (format: YYYYMMDD)
    TOC TEXT,                       -- Train Operating Company code
    CROSS_LONDON_IND TEXT,          -- Cross-London indicator (e.g., '0', '1', '2', '3')
    NS_DISC_IND TEXT,               -- Non-standard discount indicator
    PUBLICATION_IND TEXT            -- Publication indicator ('Y' or 'N')
);
""")
flows.to_sql("FLOW", conn, if_exists="replace", index=False)

# Commit and close the connection
conn.commit()
conn.close()

print("FLOW table created successfully.")








#
# # Create LOCATIONS table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS LOCATIONS (
#     NLC TEXT PRIMARY KEY,
#     LOCATION_NAME TEXT,
#     LOCATION_TYPE TEXT
# );
# """)
#
# # Create STATION_CLUSTERS table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS STATION_CLUSTERS (
#     CLUSTER_ID TEXT PRIMARY KEY,
#     CLUSTER_NLC TEXT NOT NULL,
#     START_DATE TEXT,
#     END_DATE TEXT,
#     FOREIGN KEY (CLUSTER_NLC) REFERENCES LOCATIONS(NLC)
# );
# """)
#
# # Create FLOW table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS FLOW (
#     FLOW_ID INTEGER PRIMARY KEY,
#     ORIGIN_CODE TEXT NOT NULL,
#     DESTINATION_CODE TEXT NOT NULL,
#     ROUTE_CODE TEXT,
#     STATUS_CODE TEXT,
#     USAGE_CODE TEXT,
#     DIRECTION TEXT,
#     START_DATE TEXT,
#     END_DATE TEXT,
#     FOREIGN KEY (ORIGIN_CODE) REFERENCES LOCATIONS(NLC),
#     FOREIGN KEY (DESTINATION_CODE) REFERENCES LOCATIONS(NLC)
# );
# """)
#
# # Create FARE table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS FARE (
#     FLOW_ID INTEGER NOT NULL,
#     TICKET_CODE TEXT NOT NULL,
#     FARE_AMOUNT INTEGER,
#     RESTRICTION_CODE TEXT,
#     PRIMARY KEY (FLOW_ID, TICKET_CODE),
#     FOREIGN KEY (FLOW_ID) REFERENCES FLOW(FLOW_ID)
# );
# """)
#
#
# # this one failed
#
# # Create TICKET_TYPES table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS TICKET_TYPES (
#     TICKET_CODE TEXT PRIMARY KEY,
#     DESCRIPTION TEXT,
#     CLASS TEXT,
#     TYPE TEXT,
#     GROUP TEXT,
#     VALIDITY_CODE TEXT
# );
# """)
#
# # Insert sample data into LOCATIONS
# cursor.executemany("""
# INSERT INTO LOCATIONS (NLC, LOCATION_NAME, LOCATION_TYPE) VALUES (?, ?, ?)
# """, [
#     ('0010', 'London', 'Station'),
#     ('0020', 'Manchester', 'Station'),
#     ('0030', 'Birmingham', 'Station')
# ])
#
# # Insert sample data into FLOW
# cursor.executemany("""
# INSERT INTO FLOW (FLOW_ID, ORIGIN_CODE, DESTINATION_CODE, ROUTE_CODE, STATUS_CODE, USAGE_CODE, DIRECTION, START_DATE, END_DATE)
# VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
# """, [
#     (1, '0010', '0020', 'A123', '000', 'A', 'R', '2023-01-01', '2023-12-31'),
#     (2, '0020', '0030', 'B456', '001', 'G', 'S', '2023-01-01', '2023-12-31')
# ])
#
# # Query the database
# cursor.execute("SELECT * FROM FLOW")
# rows = cursor.fetchall()
#
# for row in rows:
#     print(row)
#
#
# # Commit changes and close the connection
# conn.commit()
# conn.close()
