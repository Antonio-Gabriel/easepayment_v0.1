from uuid import uuid4
from .decorators import HandleSubscribeJsonData
from ..models import engine, classe


class ResolvingSeeder:
    @HandleSubscribeJsonData
    def load_entities_from_json_file(entity_properties: list = []):

        instance = engine.connect()

        if type(entity_properties["data"]) == dict:
            result = instance.execute(
                classe.insert(), {"id": uuid4(), **entity_properties["data"]}
            )

        elif type(entity_properties["data"]) == list:

            for items in entity_properties["data"]:
                result = instance.execute(classe.insert(), {"id": uuid4(), **items})

                print(f"[Classe] > {items}")

        return result
