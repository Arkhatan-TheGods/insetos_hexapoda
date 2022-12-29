from dotenv import dotenv_values
from typing import Callable, NoReturn


def get_config_time_tracking(fail: Callable[[str], NoReturn]):

    config = dotenv_values(".env_proto")

    folder_data = str(config.get("FOLDER_DATA"))

    file_csv = str(config.get("FILE_CSV"))

    tracking_temp_pickle = str(config.get("TRACKING_TEMP_PICKLE"))

    if len(config) < 1:
        fail("Erro ao carregar arquivo '.env_proto'")

    if not folder_data:
        fail("Parâmetro 'folder_data' vazio")

    if not file_csv:
        fail("Parâmetro 'file_csv' vazio")

    if not tracking_temp_pickle:
        fail("Parâmetro 'tracking_temp_pickle' vazio")

    return folder_data, file_csv, tracking_temp_pickle
