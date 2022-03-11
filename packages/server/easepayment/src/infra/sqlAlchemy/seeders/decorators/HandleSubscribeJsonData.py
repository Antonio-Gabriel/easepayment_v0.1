import json
from typing import Union
from functools import wraps
from ..Path import path_root
from ..File import File

DIRNAME = path_root["root"]


class HandleSubscribeJsonData:
    def __init__(self, operator: any) -> None:
        wraps(operator)(self)
        self.__operator = operator

    def __call__(self, entity_properties: list = [], **kwargs) -> Union[list, dict]:

        read_seed_base = File.init(f"{DIRNAME}/seedsFile/{kwargs['name']}.json")
        entity = json.load(read_seed_base)

        if entity:

            if type(entity) == dict:
                response = entity
            else:
                response = entity_properties.append(entity)

        else:
            response = []

        return self.__operator(response)
