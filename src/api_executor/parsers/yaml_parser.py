from pathlib import Path
from typing import Dict, Any, List
import yaml


def _get_yaml_file(file_name: str) -> Dict[str, Any]:
    """
    Return Config file based on search pattern

    :param file_name: name of the file
    :type file_name: str
    :return: Descripción
    :rtype: Dict[Any, Any]
    """
    start = Path.cwd()
    for parent in [start, *start.parents]:
        candidate = parent / file_name
        if candidate.exists():
            with candidate.open("r", encoding="utf-8") as f:
                return yaml.safe_load(f)

    raise FileNotFoundError("File does not exists or is found")


def retrieve_yaml_atributes(attribute: str) -> List[str]:
    file = _get_yaml_file("available_api.yaml")

    return [
        value for key, value in file["api_endpoints"][0].items() if key == attribute
    ]
