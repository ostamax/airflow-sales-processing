import os
import json
from fastavro import writer

def convert_and_save(raw_dir: str, stg_dir:str) -> None:
    """
    Convert json files from raw_dir to avro format and save to stg_dir

    Args:
        raw_dir (str): path to the raw data folder
        stg_dir (str): path to the converted data folder
    """


    if raw_dir and stg_dir:

        files_list = os.listdir(raw_dir)

        for file_name in files_list:
            json_path= os.path.join(raw_dir, file_name)
            avro_path = os.path.join(stg_dir, file_name[:-4] + "avro")

            os.makedirs(os.path.dirname(avro_path), exist_ok=True)

            with open(json_path, "r") as json_file:
                json_object = json.load(json_file)
            
            schema = {
                'name': 'Sales',
                'namespace': 'de2022',
                'type': 'record',
                'fields': [
                    {'name': 'client', 'type': 'string'},
                    {'name': 'purchase_date', 'type': 'string'},
                    {'name': 'product', 'type': 'string'},
                    {'name': 'price', 'type': 'int'},
                ],
            }

            with open(avro_path, "wb") as avro_file:
                writer(avro_file, schema, json_object)
            
        return "ok"

    return "unknown"

    


