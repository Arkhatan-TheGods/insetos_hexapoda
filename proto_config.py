from dotenv import dotenv_values
from typing import Callable, NoReturn

def load_config_tracking(fail:Callable[[str], NoReturn]):

    config = dotenv_values(".env_proto")

    folder_data = config.get("FOLDER_DATA") or ""

    file_csv = config.get("FILE_CSV") or ""

    tracking_temp_pickle = config.get("TRACKING_TEMP_PICKLE") or ""
    
    if not folder_data:
        fail("Parâmetro 'folder_data' vazio")

    if not file_csv:
        fail("Parâmetro 'file_csv' vazio")

    if not tracking_temp_pickle:
        fail("Parâmetro 'tracking_temp_pickle' vazio")

    return folder_data, file_csv, tracking_temp_pickle


