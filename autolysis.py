# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "httpx",
#   "pandas",
#   "numpy",
#   "requests",
#   "seaborn",
#   "matplotlib",
#   "chardet",
#   "python-dotenv",
# ]
# ///

import sys
import os
import pandas as pd
import numpy as np
import requests
import json
import seaborn as sns
import matplotlib.pyplot as plt
import chardet
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')


def create_visualization(df, column_data, filename):

    scatter_column = column_data["scatter_column"]
    hist_column = column_data["hist_column"]
    line_column = column_data["line_column"]

    x_col, y_col = scatter_column
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[x_col], y=df[y_col])
    plt.title(f"Scatter Plot of {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)

        # Ensure the folder exists
    if not os.path.exists(filename):
        os.makedirs(filename)

    # Save the plot
    scatter_file_path = os.path.join(filename, 'scatter_plot.png')
    plt.savefig(scatter_file_path, bbox_inches='tight')
    plt.close()

    hist_file_path = os.path.join(filename, 'histogram_plot.png')
    sns.histplot(df[hist_column], kde=True)
    plt.savefig(hist_file_path)
    plt.close()

    line_file_path = os.path.join(filename, 'line_plot.png')
    sns.lineplot(data=df, x=line_column[0], y=line_column[1])
    plt.savefig(line_file_path)
    plt.close()
    

def analysis(csv_file):
    try:
        df = pd.read_csv(csv_file)
    except:

        with open(csv_file, 'rb') as file:
            result = chardet.detect(file.read())

        df = pd.read_csv(csv_file, encoding=result['encoding'])

    # perform basic analysis on the dataset
    filename = os.path.basename(csv_file)
    columns = df.columns
    summary = df.describe(include='all')
    missing_values = df.isnull().sum()
    sample_rows = df.head()
    shape = df.shape
    correlation_m = df.corr(numeric_only=True)
    info = df.info()

    # openai requests using requests library
    params = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": "Analyze the following dataset summary and provide key insights, unique charateristics etc. and analyses in the readme.md format:\n\nFilename: {}\nShape: {}\nColumns: {}\nSummary: {}\nMissing Values: {}\nSample Rows: {}".format(filename, shape, columns, summary, missing_values, sample_rows)}
        ],
    }

    request = requests.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}, json=params)

    response = request.json()

    folder_name = filename.split('.')[0]

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    readme_path = os.path.join(folder_name, 'README.md')
    with open(readme_path, 'w') as readme:
        readme.write(response['choices'][0]['message']['content'])

    visualization_params = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "Analyze the following data suggest columns for creating visualizations:\n\nFilename: {}\nShape: {}\nColumns: {}\nSummary: {}\nMissing Values: {}\nSample Rows: {}\nCorrelation matrix: {}\nInfo: {}".format(filename, shape, columns, summary, missing_values, sample_rows,correlation_m, info)}
    ],
        "functions": [
        {
            "name": "visualization_columns",
            "description": "Provide the column name for creating visualizations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "scatter_column": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Provide the 2 correct and important columns name from the dataset for scatter plot."
                    },
                    "hist_column": {
                        "type": "string",
                        "description": "The column name to use for the x-axis in the histplot."
                    },
                    "line_column": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Provide the 2 correct and important columns name from the dataset for line plot."
                    },
                },
                "required": ["scatter_column", "hist_column", "line_column"]
            }
    }
    ],
    "function_call": {"name": "visualization_columns"}
    }

    get_columns = requests.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}, json=visualization_params)

    get_columns_json = get_columns.json()
    column_data = json.loads(get_columns_json["choices"][0]['message']["function_call"]["arguments"])

    create_visualization(df, column_data, folder_name)
    
    print("Analysis completed.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python autolysis.py <dataset_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    analysis(csv_file)