import os
import json
import shutil
from typing import List, Dict, Any


def save_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    """
    Save json content to disk.

    Args:
        json_content (List[Dict[str, Any]]): data from sales API
        path (str): path to save file in
    """
    if json_content and path:
        filename = path + ".json"
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w') as json_file:
            json.dump(json_content, json_file,
                            indent=4,
                            separators=(',',': '))

        json_file.close()
        return "ok"

    return "unknown"
