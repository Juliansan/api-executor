import requests
from datetime import datetime
from typing import Dict, Optional
from pathlib import Path
from loguru import logger


def caller(
    api_name: str,
    url: str,
    params: Dict[str, str],
    return_format: str,
    api_key: Optional[str] = None,
) -> None:
    """
    Make HTTP request to API and save response.

    :param url: Base URL of the API
    :param params: Query parameters as dictionary
    :param return_format: Expected response format (json, geojson, xml, etc.)
    :param api_key: Optional API key for authentication
    """
    logger.info(f"Making API request to: {url}")
    logger.debug(f"Parameters: {params}")

    try:
        # Add API key to headers if provided
        headers = {}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"

        # Make the API request
        response = requests.get(url, params=params, headers=headers, timeout=30)
        response.raise_for_status()

        logger.success(f"API request successful. Status code: {response.status_code}")

        # Save response to file
        output_dir = Path(f"data/responses/{api_name}")
        output_dir.mkdir(parents=True, exist_ok=True)

        # Determine file extension based on format
        extension_map = {
            "json": "json",
            "geojson": "geojson",
            "xml": "xml",
            "text": "txt",
            "csv": "csv",
        }
        extension = extension_map.get(return_format.lower(), "txt")

        output_file = output_dir / f"{api_name}-{datetime.now().strftime('%Y-%m-%d')}.{extension}"
        output_file.write_text(response.text, encoding="utf-8")

        logger.info(f"Response saved to: {output_file}")
        print(f"✓ Response saved to: {output_file}")

    except requests.exceptions.RequestException as e:
        logger.error(f"API request failed: {e}")
        print(f"✗ API request failed: {e}")
        raise
