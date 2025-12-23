from typing import List, Dict, Any, Optional

from loguru import logger
from .api_manager import api_caller
from ..parsers.yaml_parser import retrieve_yaml_attributes


def _retrieve_yaml_attributes(*params: str) -> List[str]:
    """
    Retrieve data from yaml

    :param params: parameters to retrieve
    :param type: list
    """
    flattened: List[str] = []
    for attributes in params:
        flattened.extend(retrieve_yaml_attributes(attributes))
    return flattened


def list_apis() -> List[str]:
    """Return list of available API names."""
    logger.info("Loading available APIs from YAML")
    return _retrieve_yaml_attributes('name')


def execute_api(api_name: str, api_key: Optional[str]) -> Dict[str, Any]:
    """Execute the specified API and return results."""
    logger.info("Executing API: {api_name} with api_key: {api_key}", api_name=api_name, api_key=api_key)
    # Business logic here: validate, make request, process response
    return {"status": "pending", "api": api_name, "api_key": api_key}  # placeholder
