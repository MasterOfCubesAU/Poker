from typing import Union, List, Dict, Any
import yaml
import os
from src.exceptions.ConfigError import ConfigError


class ConfigHandler:
    config: Union[Dict[str, Any], None] = None

    @staticmethod
    def load(path: str) -> None:
        if not os.path.exists(path):
            raise ConfigError(f"{path} does not exist.")
        with open(path, "r") as f:
            ConfigHandler.config = yaml.safe_load(f)

    @staticmethod
    def get(key: str) -> Union[str, int, bool, List[Any], Dict[str, Any], None]:
        if ConfigHandler.config is None:
            raise ConfigError("Config not set/loaded")
        if ConfigHandler.config.get(key, None) is None:
            raise ConfigError(f"{key} key does not exist in config")
        return ConfigHandler.config.get(key)

    @staticmethod
    def clear() -> None:
        ConfigHandler.config = None
