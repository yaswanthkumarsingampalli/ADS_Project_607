import pandas as pd
import requests
from io import StringIO
import os
from git import Repo

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

def push_to_github(local_repo_path, file_path, commit_message):
    repo = Repo(local_repo_path)
    repo.index.add([file_path])
    repo.index.commit(commit_message)
    repo.remote().push()

if __name__ == "__main__":
    # GitHub URLs for input and local output paths
    input_url = "https://github.com/yaswanthkumarsingampalli/ADS_Project_607/raw/main/Data_sets/googleplaystore.csv"
    local_output_path = "cleaned_dataset.csv"
    local_repo_path = "https://github.com/yaswanthkumarsingampalli/ADS_Project_607.git"  # Change this to your local GitHub repository path

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
