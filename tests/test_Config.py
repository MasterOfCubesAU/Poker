from typing import Dict, Any
import yaml
import pytest
import os
from src.utils.ConfigHandler import ConfigHandler

from src.exceptions.ConfigError import ConfigError


@pytest.fixture(autouse=True)
def run_around_tests():
    generateFile({"bruh": 1, "hello": "world"}, "whatever.yaml")
    assert os.path.exists("whatever.yaml")
    yield
    deleteFile("whatever.yaml")
    assert not os.path.exists("whatever.yaml")


def generateFile(JSON: Dict[str, Any], filename: str):
    with open(filename, "w") as file:
        file.write(yaml.dump(JSON))


def deleteFile(path: str):
    os.remove(path)


def test_load_config_valid():
    ConfigHandler.load("whatever.yaml")

    assert ConfigHandler.get("bruh") == 1
    assert ConfigHandler.get("hello") == "world"


def test_load_config_invalid():
    with pytest.raises(ConfigError):
        ConfigHandler.load("invalid.yaml")

    ConfigHandler.load("whatever.yaml")

    with pytest.raises(ConfigError):
        ConfigHandler.get("key")
        ConfigHandler.get("invalid")

    ConfigHandler.clear()
    with pytest.raises(ConfigError):
        ConfigHandler.get("test")


def test_config_clear():
    ConfigHandler.clear()
    assert ConfigHandler.config is None
