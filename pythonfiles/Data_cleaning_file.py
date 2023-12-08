import pandas as pd
import requests
from io import StringIO
import os

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

def save_cleaned_dataset(cleaned_data, local_output_path):
    cleaned_data.to_csv(local_output_path, index=False)

def push_to_github(local_repo_path, local_output_path, commit_message):
    # Change to the directory of the local GitHub repository
    os.chdir(local_repo_path)

    # Add the cleaned dataset to the Git staging area
    os.system(f'git add {local_output_path}')

    # Commit the changes
    os.system(f'git commit -m "{commit_message}"')

    # Push the changes to the GitHub repository
    os.system('git push')

if __name__ == "__main__":
    # GitHub URLs for input and local output paths
    input_url = "https://github.com/yaswanthkumarsingampalli/ADS_Project_607/raw/main/Data_sets/googleplaystore.csv"
    local_output_path = "cleaned_dataset.csv"

    # Determine the current working directory (where the script is located)
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the local repository path by joining with the script directory
    local_repo_path = os.path.join(script_directory, "ADS_Project_607")

    # Download the dataset from the input repository
    raw_data = download_dataset(input_url)

    # Convert the raw data into a DataFrame
    dataset = pd.read_csv(StringIO(raw_data))

    # Clean the dataset
    cleaned_dataset = clean_dataset(dataset)

    # Save the cleaned dataset locally
    save_cleaned_dataset(cleaned_dataset, local_output_path)

    # Push the cleaned dataset to the GitHub repository
    push_to_github(local_repo_path, local_output_path, "Update cleaned dataset")

    print("Dataset cleaning, saving, and pushing to GitHub complete.")
