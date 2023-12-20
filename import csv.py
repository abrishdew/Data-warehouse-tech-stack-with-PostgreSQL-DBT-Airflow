import pandas as pd

# Empty DataFrames to hold the filtered data
track_info_df = pd.DataFrame(columns=["track_id", "type"])
speed_df = pd.DataFrame(columns=["track_id", "traveled_d", "avg_speed"])


with open('20181024_d1_0830_0900.csv', 'r') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        # Split the line into separate records
        values = [value.strip(' ') for value in line.split(';') if value]

        # Extract desired data
        track_id, type_, traveled_d, avg_speed = values[:4]

        # Append data to respective DataFrames
        track_info_df.loc[i] = [track_id, type_]
        speed_df.loc[i] = [track_id, traveled_d, avg_speed]
print(track_info_df)