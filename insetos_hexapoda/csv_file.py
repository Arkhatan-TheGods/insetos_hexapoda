import pandas as pd
import csv


def read_data_frame(file: str):
    return pd.read_csv(file)


def read_by_column(file: str, column: str):
    return pd.read_csv(file, index_col=column)


def writing_csv(file, data) -> None:

    with open(file, 'w') as _file:
        writer = csv.writer(_file)
        writer.writerow(data)