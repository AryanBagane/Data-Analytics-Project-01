import requests
import openpyxl
import csv
import pandas as pd
from io import StringIO

def get_data_from_api(api_url):
    response = requests.get(api_url)
    
    # Check if the response status code is OK (200)
    if response.status_code == 200:
        try:
            # Assuming the response is in CSV format
            csv_data = response.text
            data = list(csv.DictReader(StringIO(csv_data)))
            return data
        except Exception as e:
            print(f"Error processing CSV data: {e}")
            print("API Response:")
            print(response.text)
    else:
        print(f"Error fetching data from API. Status code: {response.status_code}")

    return None

def append_data_to_excel(data, excel_file):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Assuming the CSV data has the same header as the Excel sheet
    header = list(data[0].keys())
    sheet.append(header)

    for row_data in data:
        row_values = [row_data.get(column, "") for column in header]
        sheet.append(row_values)

    workbook.save(excel_file)
    print("Data appended successfully.")

def convert_xlsx_to_csv(excel_file, csv_file):
    df = pd.read_excel(excel_file)
    df.to_csv(csv_file, index=False)
    print("Conversion from XLSX to CSV completed successfully.")

# Replace these values with your actual API endpoint and Excel file details
api_url = "https://api.example.com/data"
excel_file = "/home/user/Desktop/Data Analytics Project/Fetched_data.xlsx"
csv_file = "/home/user/Desktop/Data Analytics Project/Fetched_data.csv"

# Get data from API
api_data = get_data_from_api(api_url)

if api_data:
    # Append data to Excel file
    append_data_to_excel(api_data, excel_file)

    # Convert Excel to CSV
    convert_xlsx_to_csv(excel_file, csv_file)

