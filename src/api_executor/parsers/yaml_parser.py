from pathlib import Path
from typing import Dict, Any, List
import yaml


def _get_data(file_name: str) -> Dict[str, Any]:
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


def get_attributes(attribute: str) -> List[str]:
    """
    Retrive data from yaml

    :param attribute: Descripción
    :type attribute: str
    :return: Descripción
    :rtype: List[str]
    """
    file = _get_data("available_api.yaml")

    return [
        value for key, value in file["api_endpoints"][0].items() if key == attribute
    ]


def parse_details(attribute: str) -> Dict[str, Any]:
    return _get_data("available_api.yaml")['api_endpoints'][0]

