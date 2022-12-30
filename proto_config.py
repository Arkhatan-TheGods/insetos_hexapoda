from dotenv import dotenv_values


class ConfigProto:

    def __init__(self, data_temp: str,
                 csv_file: str,
                 dump_tracking: str) -> None:

        self.data_temp = data_temp

        self.csv_file = csv_file

        self.dump_tracking = dump_tracking


def load_env() -> ConfigProto:

    config: dict[str, str | None] = dotenv_values(".env_proto")

    if not config:
        raise FileNotFoundError("Erro ao carregar arquivo '.env_proto'")

    data_temp: str | None = config.get("DATA_TEMP")

    csv_file: str | None = config.get("CSV_FILE")

    dump_tracking: str | None = config.get("DUMP_TRACKING")

    if data_temp is None:
        raise NameError("Erro ao carregar campo DATA_TEMP")

    if csv_file is None:
        raise NameError("Erro ao carregar campo CSV_FILE")

    if dump_tracking is None:
        raise NameError("Erro ao carregar campo DUMP_TRACKING")

    return ConfigProto(data_temp,
                       csv_file,
                       dump_tracking)
