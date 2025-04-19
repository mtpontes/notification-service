from os import path

from dotenv import load_dotenv


class DotEnvUtils:
    @staticmethod
    def load():
        dot_env_path: str = path.abspath('./envs/.env')
        load_dotenv(dot_env_path)