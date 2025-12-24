from typing import List, Dict, Any, Optional

from loguru import logger
from ..api.caller import caller
from ..parsers.yaml_parser import get_attributes, parse_details


def _retrieve_yaml_attributes(key_name: str, attribute: str) -> List[str]:
    """
    Retrieve data from yaml

    :param params: parameters to retrieve
    :param type: list
    """
    flattened: List[str] = []
    for key, value in get_attributes(key_name):
        if key == attribute:
            flattened.append(value)
    return flattened


def list_apis() -> List[str]:
    """Return list of available API names."""
    logger.info("Loading available APIs from YAML")
    return _retrieve_yaml_attributes("name", "name")


def execute_api(api_name: str, api_key: Optional[str], params: Dict[str, str]) -> None:
    """Execute the specified API and save data in /data/responses/source_name."""
    logger.info(
        "Executing API: {api_name} with api_key: {api_key} and params: {params}",
        api_name=api_name,
        api_key=api_key,
        params=params,
    )

    # Get API configuration from YAML
    api_details = parse_details(api_name)
    base_url = api_details.get('url', '')
    return_format = api_details.get('format', 'json')
    
    # Get the first method's endpoint (for now, assuming single endpoint per API)
    methods = api_details.get('methods', [])
    if methods:
        endpoint = methods[0].get('endpoint', '')
        full_url = f"{base_url}{endpoint}"
    else:
        full_url = base_url
    
    logger.info(f"Full URL: {full_url}")
    
    caller(api_name, full_url, params, return_format, api_key)


def get_details(api_name: str) -> Dict[str, Any]:
    logger.info(f"Parsing YAML data for {api_name}")
    return parse_details(api_name)
