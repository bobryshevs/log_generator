from random import choice
from time import sleep, time
from hashlib import md5

from loggers_factory import LoggersFactory
from loggers import BaseLogger


class Main:
    def __init__(self) -> None:
        self.levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        self.logger: BaseLogger = LoggersFactory().get()

    def get_random_level(self) -> str:
        return choice(self.levels)

    def run(self):
        while True:
            self.logger.log(message=md5(str(time()).encode()).hexdigest(),
                            level=self.get_random_level())
            sleep(7)


if __name__ == "__main__":
    main = Main()
    try:
        main.run()
    except KeyboardInterrupt:
        print("\n\n\n[[     ` Bye! `    ]]")
