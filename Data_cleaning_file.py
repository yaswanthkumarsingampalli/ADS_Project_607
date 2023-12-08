import pandas as pd
import requests
from io import StringIO

def download_dataset(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to download dataset from {url}")

def clean_dataset(input_data):
    # Your cleaning logic here
    # For example, removing missing values
    cleaned_data = input_data.dropna()
    return cleaned_data

def save_cleaned_dataset(cleaned_data, output_path):
    cleaned_data.to_csv(output_path, index=False)

if __name__ == "__main__":
    # GitHub URLs for input and output repositories
    input_url = "https://github.com/yaswanthkumarsingampalli/ADS_Project_607/raw/main/Data_sets/googleplaystore.csv"
    output_url = "https://github.com/yaswanthkumarsingampalli/ADS_Project_607/raw/main/Cleand_Data_sets/googleplaystore.csv"

    # Download the dataset from the input repository
    raw_data = download_dataset(input_url)

    # Convert the raw data into a DataFrame
    dataset = pd.read_csv(StringIO(raw_data))

    # Clean the dataset
    cleaned_dataset = clean_dataset(dataset)

    # Save the cleaned dataset to the output repository
    save_cleaned_dataset(cleaned_dataset, "cleaned_dataset.csv")

    print("Dataset cleaning and saving complete.")
