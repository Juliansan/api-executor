from typing import List, Dict, Any

from loguru import logger

from ..parsers.yaml_parser import retrieve_yaml_atributes

def list_available_apis() -> List[str]:
    """Return list of available API names."""
    logger.info("Loading available APIs from YAML")
    return retrieve_yaml_atributes('name')

def execute_api(api_name: str, api_key: str | None = None) -> Dict[str, Any]:
    """Execute the specified API and return results."""
    logger.info("Executing API: {api_name}", api_name=api_name)
    # Business logic here: validate, make request, process response
    return {"status": "pending", "api": api_name}  # placeholder