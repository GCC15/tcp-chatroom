import json


def _load_config_dict():
    return json.load(open('config.json'))


_config_dict = _load_config_dict()


def get(key):
    return _config_dict[key]
