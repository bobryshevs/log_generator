from loggers import BaseLogger


class LoggersFactory:
    def __init__(self) -> None:
        base = BaseLogger()
        self.name_to_logger = {
            base.__class__.__name__: base
        }

    def get_logger(self, logger_name: str):
        return self.name_to_logger[logger_name]
