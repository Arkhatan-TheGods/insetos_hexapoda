from dotenv import dotenv_values
from typing import Callable, NoReturn, Tuple, Dict

XFailed = Callable[[str], NoReturn]

def load_env_time_tracking(fail: XFailed) -> Tuple[str, str, str]:

    config: Dict[str, str | None] = dotenv_values(".env_proto")

    data_temp = str(config.get("DATA_TEMP"))

    csv_file = str(config.get("CSV_FILE"))

    dump_tracking = str(config.get("DUMP_TRACKING"))

    if config == {}:
        fail("Erro ao carregar arquivo '.env_proto'")

    if not data_temp:
        fail("env 'data_temp' vazio")

    if not csv_file:
        fail("env 'csv_file' vazio")

    if not dump_tracking:
        fail("env 'dump_tracking' vazio")

    return data_temp, csv_file, dump_tracking


def load_env_csv_file(fail: XFailed) -> Tuple[str, str]:

    config: Dict[str, str | None] = dotenv_values(".env_proto")

    data_temp = str(config.get("DATA_TEMP"))

    csv_temp = str(config.get("CSV_TEMP"))

    if config == {}:
        fail("Erro ao carregar arquivo '.env_proto'")

    if not data_temp:
        fail("env 'data_temp' vazio")

    if not csv_temp:
        fail("env 'csv_temp' vazio")

    return data_temp, csv_temp
