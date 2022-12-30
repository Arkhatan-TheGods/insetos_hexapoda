from dotenv import dotenv_values


class ConfigProto:

    def __init__(self, data_temp: str,
                 csv_file: str,
                 csv_temp: str,
                 dump_tracking: str) -> None:

        self.data_temp = data_temp

        self.csv_file = csv_file

        self.csv_temp = csv_temp

        self.dump_tracking = dump_tracking


def load_env(dotenv_path) -> ConfigProto:

    config: dict[str, str | None] = dotenv_values(dotenv_path)

    if not config:
        raise FileNotFoundError("Erro ao carregar arquivo '.env_proto'")

    if config.get("DATA_TEMP") is None:
        raise NameError("Erro ao carregar campo DATA_TEMP")

    if config.get("CSV_FILE") is None:
        raise NameError("Erro ao carregar campo CSV_FILE")

    if config.get("CSV_TEMP") is None:
        raise NameError("Erro ao carregar campo CSV_TEMP")

    if config.get("DUMP_TRACKING") is None:
        raise NameError("Erro ao carregar campo DUMP_TRACKING")

    return ConfigProto(str(config.get("DATA_TEMP")),
                       str(config.get("CSV_FILE")),
                       str(config.get("CSV_TEMP")),
                       str(config.get("DUMP_TRACKING")))
