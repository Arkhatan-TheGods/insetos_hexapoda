import pandas as pd
import csv


def read_data_frame(file: str):
    return pd.read_csv(file)


def read_by_column(file: str, column: str):
    return pd.read_csv(file, index_col=column)


def writing_csv(file: str, header, data) -> None:
    
    with open(file, 'w', encoding='UTF8') as _file:
        writer = csv.writer(_file)

        writer.writerow(header)

        writer.writerow(data)