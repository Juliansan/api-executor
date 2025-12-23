# API Executor

A Python CLI tool for discovering and executing HTTP API endpoints defined in a YAML registry. This project provides a flexible framework for managing and interacting with multiple APIs through a unified command-line interface.

## Features

- **YAML-based API Registry**: Configure API endpoints, methods, and parameters in a single YAML file
- **CLI Interface**: User-friendly command-line interface built with Click
- **API Discovery**: List and explore available APIs and their configurations
- **Detailed API Information**: View comprehensive API details including methods, parameters, and response formats
- **Smart Configuration Loading**: Automatically searches for configuration files in parent directories
- **Structured Logging**: Comprehensive logging with Loguru (errors to console, detailed logs to files)
- **Extensible Architecture**: Modular design for easy addition of new APIs and functionality

## Requirements

- **Python** >= 3.12
- Dependencies managed via `pyproject.toml`:
  - `click` - CLI framework
  - `requests` - HTTP library
  - `pyyaml` - YAML parsing
  - `loguru` - Advanced logging
  - `pandas` - Data manipulation
  - `matplotlib` - Data visualization
  - `scikit-learn` - Machine learning utilities
  - `ruff` - Python linter

## Installation

### Using uv (recommended)

```bash
uv sync
# or
uv pip install -e .
```

### Using pip

```bash
python -m pip install -e .
```

## Usage

### Available Commands

The CLI provides three main commands:

#### 1. List Available APIs

Display all configured APIs:

```bash
api-executor list
```

#### 2. Get API Details

View comprehensive information about a specific API including endpoints, parameters, and response formats:

```bash
api-executor api-details <API_NAME>
```

Example:

```bash
api-executor api-details USGS
```

#### 3. Execute an API

Execute an API call (requires API key via environment variable or option):

```bash
api-executor api <API_NAME>
```

With API key:

```bash
api-executor api --api-key YOUR_KEY USGS
# or set environment variable
export API_KEY=YOUR_KEY
api-executor api USGS
```

### Examples

```bash
# List all available APIs
api-executor list

# Get detailed information about USGS API
api-executor api-details USGS

# Execute USGS API with API key
api-executor api --api-key abc123 USGS
```

## Configuration

### API Registry (available_api.yaml)

The `available_api.yaml` file contains the API registry. The system searches for this file starting from the current working directory and walking up through parent directories, allowing you to run commands from any subfolder.

Example configuration structure:

```yaml
api_endpoints: 
  - name: USGS
    full_name: United States Geological Survey
    base_url: https://earthquake.usgs.gov/fdsnws/event/1/
    description: Provides access to earthquake event data
    methods:
      - name: Query Events
        endpoint: query
        method: GET
        parameters:
          - name: starttime
            type: string
            description: Start time in ISO format (YYYY-MM-DDTHH:MM:SS)
          - name: endtime
            type: string
            description: End time in ISO format (YYYY-MM-DDTHH:MM:SS)
          - name: minmagnitude
            type: float
            description: Minimum magnitude of events
          - name: maxmagnitude
            type: float
            description: Maximum magnitude of events
          - name: format
            type: string
            description: Response format (geojson, xml, text)
        response_format: JSON or XML depending on format parameter
```

## Project Structure

```text
.
├── available_api.yaml          # API registry configuration
├── pyproject.toml              # Project metadata and dependencies
├── README.md                   # Project documentation
├── data/                       # Data storage
│   ├── dataframe/             # Processed data frames
│   └── responses/             # API responses
├── logs/                       # Application logs (auto-generated)
└── src/
    └── api_executor/
        ├── __init__.py
        ├── api/                # API implementation layer
        │   ├── __init__.py
        │   └── caller.py      # HTTP request handlers
        ├── cli/                # Command-line interface
        │   ├── __init__.py
        │   └── cli.py         # Click commands and CLI entry point
        ├── core/               # Core business logic
        │   ├── __init__.py
        │   ├── api_manager.py # API execution management
        │   └── cli_manager.py # CLI command handlers
        ├── parsers/            # Configuration parsers
        │   ├── __init__.py
        │   └── yaml_parser.py # YAML configuration loader
        └── utils/              # Shared utilities
            ├── __init__.py
            ├── formatter.py   # Output formatting helpers
            └── logger.py      # Logging configuration
```

## Logging

The application uses Loguru for structured logging:

- **Console**: Only ERROR and CRITICAL messages are displayed
- **Log Files**: Stored in `logs/` directory with timestamps
  - Rotation: 10 MB per file
  - Retention: 30 days
  - Compression: Automatic zip compression
  - Format: `logs/app-YYYY-MM-DD_HH-MM-SS.log`

## Development

### Project Scope

**Current Features:**
- YAML-based API registry management
- CLI commands for listing and viewing API details
- Configuration discovery with parent directory traversal
- Structured logging system
- API execution framework (execution logic in progress)

**Out of Scope (for now):**
- Full ETL/data warehousing pipeline
- Long-term data persistence (databases, parquet lakes)
- Advanced runtime features (automatic retries, exponential backoff, caching)
- Complex authentication flows (currently supports simple API key)

### Adding New APIs

1. Edit `available_api.yaml`
2. Add a new entry under `api_endpoints` with required fields:
   - `name`: Short identifier
   - `full_name`: Complete API name
   - `base_url`: API base URL
   - `description`: Brief description
   - `methods`: List of available endpoints with parameters

### Running in Development

```bash
# Install in editable mode
uv pip install -e .

# Run CLI commands
api-executor list
api-executor api-details USGS
```

## License

This is a learning project for exploring API integration patterns and CLI development in Python.

## Contributing

This is a personal learning project, but suggestions and improvements are welcome!
