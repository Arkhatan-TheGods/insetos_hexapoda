from dotenv import dotenv_values
from typing import Callable, NoReturn, Tuple, Dict

XFailed = Callable[[str], NoReturn]
ConfigHighlights = Dict[str, str | None]


def get_env_values() -> ConfigHighlights:
    return dotenv_values(".env_proto")


def load_env_time_tracking(config: ConfigHighlights, fail: XFailed) -> Tuple[str, str, str]:

    if config == {}:
        fail("Erro ao carregar arquivo '.env_proto'")

    data_temp = str(config.get("DATA_TEMP"))

    csv_file = str(config.get("CSV_FILE"))

    dump_tracking = str(config.get("DUMP_TRACKING"))

    if not data_temp:
        fail("env 'data_temp' vazio")

    if not csv_file:
        fail("env 'csv_file' vazio")

    if not dump_tracking:
        fail("env 'dump_tracking' vazio")

    return data_temp, csv_file, dump_tracking


def load_env_csv_file(config: ConfigHighlights, fail: XFailed) -> Tuple[str, str]:

    if config == {}:
        fail("Erro ao carregar arquivo '.env_proto'")

    data_temp = str(config.get("DATA_TEMP"))

    csv_temp = str(config.get("CSV_TEMP"))

    if not data_temp:
        fail("env 'data_temp' vazio")

    if not csv_temp:
        fail("env 'csv_temp' vazio")

    return data_temp, csv_temp
