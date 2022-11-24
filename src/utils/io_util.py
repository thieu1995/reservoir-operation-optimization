# !/usr/bin/env python
# Created by "Thieu" at 16:06, 24/02/2021 ----------%
#       Email: nguyenthieu2102@gmail.com            %
#       Github: https://github.com/thieu1995        %
# --------------------------------------------------%

import numpy as np
import pandas as pd
from csv import DictWriter
from pathlib import Path


def array_to_csv(data, header:list, filename=None, pathsave=None):
    ## Check the parent directories
    Path(pathsave).mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(data, columns=header)
    df.to_csv(f"{pathsave}/{filename}.csv", index=False, header=True)
    return None


def save_to_csv(data:list, header:list, filename=None, pathsave=None):
    ## Check the parent directories
    Path(pathsave).mkdir(parents=True, exist_ok=True)
    # Convert data and header to dictionary
    mydict = {}
    for idx, h in enumerate(header):
        mydict[h] = np.array(data[idx]).reshape(-1)
    df = pd.DataFrame(mydict, columns=header)
    df.to_csv(f"{pathsave}/{filename}.csv", index=False, header=True)
    return None


def save_to_csv_dict(data:dict, filename=None, pathsave=None):
    ## Check the parent directories
    Path(pathsave).mkdir(parents=True, exist_ok=True)
    ## Reshape data
    data_shaped = {}
    for key, value in data.items():
        data_shaped[key] = np.array(value).reshape(-1)
    df = pd.DataFrame(data_shaped, columns=data_shaped.keys())
    df.to_csv(f"{pathsave}/{filename}.csv", index=False, header=True)
    return None


def save_results_to_csv(data:dict, filename=None, pathsave=None):
    ## Check the parent directories
    Path(pathsave).mkdir(parents=True, exist_ok=True)
    with open(f"{pathsave}/{filename}.csv", 'a') as file:
        w = DictWriter(file, delimiter=',', lineterminator='\n', fieldnames=data.keys())
        if file.tell() == 0:
            w.writeheader()
        w.writerow(data)
    return None


def load_dataset(name_folder=None, name_file=None, name_input=None, name_output=None):
    dataset = pd.read_csv(f"{name_folder}/{name_file}")
    X = dataset[name_input].values                      # Input variables
    if name_output is not None:
        Y = dataset[name_output].values.reshape(-1, 1)  # Output variable
        return X, Y
    return X, None


def save_data_to_excel(data=list, sheet_names=list, pathfile=str, columns=list):
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(f'{pathfile}.xlsx', engine='xlsxwriter')

    # Write each dataframe to a different worksheet.
    for idx, (sheet_name, sheet_data) in enumerate(zip(sheet_names, data)):
        df_x = pd.DataFrame(sheet_data, columns=columns)
        df_x.to_excel(writer, sheet_name=sheet_name, index=False)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    return None

