# import pandas as pd
# import json
# import os
# from datetime import datetime
#
#
# class JSONToCSV:
#     def main(self):
#         mstr_df = pd.DataFrame()
#         folder_path = "D:/Navaantrix/ThetaControls/ThetaControlsData"
#
#         for file in os.listdir(folder_path):
#             d = {}
#             file_path = os.path.join(folder_path, file)
#             with open(file_path, "r", encoding='utf-8') as f:
#                 data = json.load(f)
#                 for i in data.values():
#                     standard_variable_data = i.split('|')
#                     standard_variable_data = standard_variable_data[:5]
#
#
#                     # Basic columns
#                     d['Location'] = standard_variable_data[0]
#                     d['SerialNumber'] = standard_variable_data[1]
#                     d['UnitType'] = standard_variable_data[2]
#
#                     # Parse RtcDate and RtcTime
#                     try:
#                         # Convert RtcDate to a proper date format
#                         raw_date = standard_variable_data[3]
#                         d['RtcDate'] = datetime.strptime(raw_date, "%y:%m:%d").date()  # Adjust format here if needed
#
#                         # Convert RtcTime to a proper time format
#                         raw_time = standard_variable_data[4]
#                         d['RtcTime'] = datetime.strptime(raw_time, "%H:%M:%S").time()  # Adjust format here if needed
#                     except ValueError as e:
#                         print(f"Error parsing date or time in file {file}: {e}")
#                         d['RtcDate'] = raw_date  # Keep raw value if parsing fails
#                         d['RtcTime'] = raw_time
#
#                 # Handle attribute variables
#                 for i in data.values():
#                     attribute_variable = i.split('|')
#                     attribute_variable = attribute_variable[5:]
#                     numeric_values = [int("".join(filter(str.isdigit, item))) for item in attribute_variable]
#                     for j in range(len(numeric_values)):
#                         d[f"Attribute{j + 1}Value"] = numeric_values[j]
#
#                 # Default values
#                 default_values = {
#                     'Attribute1': 'ON TIME',
#                     'Attribute2': 'BATTERY VOLTAGE',
#                     'Attribute3': 'BATTERY CURRENT',
#                     'Attribute4': 'BATTERY W',
#                     'Attribute5': 'ONTIME WH',
#                     'Attribute6': 'INVERTER VOLTAGE',
#                     'Attribute7': 'INVERTER CURRENT',
#                     'Attribute8': 'INVERTER POWER',
#                     'Attribute9': 'INVERTER ONTIME KWH',
#                     'Attribute10': 'TEMPERATURE',
#                     'Attribute11': 'TAP INFO',
#                     'Attribute12': 'FAULTS',
#                     'Attribute13': 'SEQUENCE NUMBER'
#                 }
#                 d.update(default_values)
#                 mstr_df = mstr_df._append(d, ignore_index=True)
#
#                 # Save as CSV
#                 mstr_df.to_csv("output_new1.txt",sep="|", index=False, date_format="%Y-%m-%d %H:%M:%S")
#
#
#
# if __name__ == "__main__":
#     a = JSONToCSV()
#     a.main()
#
#


# import pandas as pd
# import json
# import os
# from datetime import datetime
#
#
# class JSONToCSV:
#     def main(self):
#         folder_path = "D:/Navaantrix/ThetaControls/ThetaControlsData"
#
#         for file in os.listdir(folder_path):
#             d = {}
#             file_path = os.path.join(folder_path, file)
#             with open(file_path, "r", encoding='utf-8') as f:
#                 data = json.load(f)
#                 for i in data.values():
#                     standard_variable_data = i.split('|')
#                     standard_variable_data = standard_variable_data[:5]
#
#                     # Basic columns
#                     d['Location'] = standard_variable_data[0]
#                     d['SerialNumber'] = standard_variable_data[1]
#                     d['UnitType'] = standard_variable_data[2]
#
#                     # Parse RtcDate and RtcTime
#                     try:
#                         # Convert RtcDate to a proper date format
#                         raw_date = standard_variable_data[3]
#                         d['RtcDate'] = datetime.strptime(raw_date, "%y:%m:%d").date()  # Adjust format here if needed
#
#                         # Convert RtcTime to a proper time format
#                         raw_time = standard_variable_data[4]
#                         d['RtcTime'] = datetime.strptime(raw_time, "%H:%M:%S").time()  # Adjust format here if needed
#                     except ValueError as e:
#                         print(f"Error parsing date or time in file {file}: {e}")
#                         d['RtcDate'] = raw_date  # Keep raw value if parsing fails
#                         d['RtcTime'] = raw_time
#
#
#                 attribute_column_name = {
#                     'a': 'ON TIME',
#                     'b': 'BATTERY VOLTAGE',
#                     'c': 'BATTERY CURRENT',
#                     'd': 'BATTERY W',
#                     'e': 'ONTIME WH',
#                     'f': 'INVERTER VOLTAGE',
#                     'g': 'INVERTER CURRENT',
#                     'h': 'INVERTER POWER',
#                     'i': 'INVERTER ONTIME KWH',
#                     'j': 'TEMPERATURE',
#                     'k': 'TAP INFO',
#                     'l': 'FAULTS',
#                     's': 'SEQUENCE NUMBER'
#                 }
#
#
#                 # Handle attribute variables
#                 for i in data.values():
#                     attribute_variable = i.split('|')
#                     attribute_variable = attribute_variable[5:]
#
#                     # Extract numeric and alphabetic values
#                     numeric_values = [int("".join(filter(str.isdigit, item))) for item in attribute_variable]
#                     alphabetic_values = ["".join(filter(str.isalpha, item)) for item in attribute_variable]
#
#                     for j in range(len(alphabetic_values)):
#                         # Check if the alphabetic value exists in the attribute_column_name dictionary
#                         if alphabetic_values[j] in attribute_column_name:
#                             # Use the dictionary value as the column name
#                             column_name = attribute_column_name[alphabetic_values[j]]
#                             d[column_name] = numeric_values[j]
#
#                 # Default values
#                 # default_values = {
#                 #     'Attribute1': 'ON TIME',
#                 #     'Attribute2': 'BATTERY VOLTAGE',
#                 #     'Attribute3': 'BATTERY CURRENT',
#                 #     'Attribute4': 'BATTERY W',
#                 #     'Attribute5': 'ONTIME WH',
#                 #     'Attribute6': 'INVERTER VOLTAGE',
#                 #     'Attribute7': 'INVERTER CURRENT',
#                 #     'Attribute8': 'INVERTER POWER',
#                 #     'Attribute9': 'INVERTER ONTIME KWH',
#                 #     'Attribute10': 'TEMPERATURE',
#                 #     'Attribute11': 'TAP INFO',
#                 #     'Attribute12': 'FAULTS',
#                 #     'Attribute13': 'SEQUENCE NUMBER'
#                 # }
#
#
#
#
#                 #d.update(default_values)
#
#                 # Create a DataFrame for the current file
#                 df = pd.DataFrame([d])
#
#                 # Save as CSV (each file will have a separate output file)
#                 output_file = os.path.join("D:/Navaantrix/ThetaControls/Output", f"{os.path.splitext(file)[0]}.txt")
#                 df.to_csv(output_file, sep="|", index=False, date_format="%Y-%m-%d %H:%M:%S")
#                 print(f"Saved {output_file}")
#
#
# if __name__ == "__main__":
#     a = JSONToCSV()
#     a.main()
#





import json
from datetime import datetime
import os
import pandas as pd


class JSONToCSV:
    def main(self):
        folder_path = "D:/Navaantrix/ThetaControls/ThetaControlsData"

        # Make sure the output directory exists
        output_folder = "D:/Navaantrix/ThetaControls/Output"
        os.makedirs(output_folder, exist_ok=True)

        for file in os.listdir(folder_path):
            d = {}
            file_path = os.path.join(folder_path, file)

            # Skip non-JSON files or empty files
            if not file.endswith(".json"):
                print(f"Skipping non-JSON file: {file}")
                continue

            if os.path.getsize(file_path) == 0:
                print(f"Skipping empty file: {file}")
                continue

            try:
                # Open and load JSON file
                with open(file_path, "r", encoding='utf-8') as f:
                    data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON file {file}: {e}")
                continue

            for i in data.values():
                standard_variable_data = i.split('|')
                standard_variable_data = standard_variable_data[:5]

                # Basic columns
                d['Location'] = standard_variable_data[0]
                d['SerialNumber'] = standard_variable_data[1]
                d['UnitType'] = standard_variable_data[2]

                # Parse RtcDate and RtcTime
                try:
                    raw_date = standard_variable_data[3]
                    d['RtcDate'] = datetime.strptime(raw_date, "%y:%m:%d").date()
                    raw_time = standard_variable_data[4]
                    d['RtcTime'] = datetime.strptime(raw_time, "%H:%M:%S").time()
                except ValueError as e:
                    print(f"Error parsing date or time in file {file}: {e}")
                    d['RtcDate'] = raw_date  # Keep raw value if parsing fails
                    d['RtcTime'] = raw_time

            # Attribute column name dictionary
            attribute_column_name = {
                'a': 'ON TIME',
                'b': 'BATTERY VOLTAGE',
                'c': 'BATTERY CURRENT',
                'd': 'BATTERY W',
                'e': 'ONTIME WH',
                'f': 'INVERTER VOLTAGE',
                'g': 'INVERTER CURRENT',
                'h': 'INVERTER POWER',
                'i': 'INVERTER ONTIME KWH',
                'j': 'TEMPERATURE',
                'k': 'TAP INFO',
                'l': 'FAULTS',
                's': 'SEQUENCE NUMBER'
            }

            # Handle attribute variables
            # Handle attribute variables
            for i in data.values():
                attribute_variable = i.split('|')
                attribute_variable = attribute_variable[5:]  # Assuming attributes start from index 5

                # Extract numeric and alphabetic values
                numeric_values = [int("".join(filter(str.isdigit, item))) for item in attribute_variable if
                                  any(char.isdigit() for char in item)]
                alphabetic_values = ["".join(filter(str.isalpha, item)) for item in attribute_variable if
                                     any(char.isalpha() for char in item)]

                # Match alphabetic values with attribute_column_name and assign numeric values
                for j in range(len(alphabetic_values)):
                    key = alphabetic_values[j].lower()  # Convert to lowercase
                    if key in attribute_column_name:  # Check if key exists in dictionary
                        column_name = attribute_column_name[key]
                        d[column_name] = numeric_values[j]


                # print("Complete Row Data:", d)
            # Create a DataFrame for the current file
            df = pd.DataFrame([d])
            # print(d)

            # # Save as CSV (each file will have a separate output file)
            output_file = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.txt")
            df.to_csv(output_file, sep="|", index=False, date_format="%Y-%m-%d %H:%M:%S")
            print(f"Saved {output_file}")


if __name__ == "__main__":
    a = JSONToCSV()
    a.main()
