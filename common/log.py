import logging

class Log:

    @classmethod
    def create_logger(self):
        logging.basicConfig(
            format='%(asctime)s - [%(lineno)s] - %(module)s - %(levelname)s:  %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S %p',
            level=logging.INFO,
        )
        return logging.getLogger()

