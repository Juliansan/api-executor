
# Earthquakes — API Executor

Small learning project to **discover and execute HTTP API endpoints** defined in a YAML registry.

At the moment, the CLI can:

- List configured APIs from `available_api.yaml`
- Accept an API name for execution (execution logic is a placeholder)

## Scope

**In scope**

- Maintain a simple YAML registry of available APIs (names + base URLs)
- Provide a CLI entry point to list available APIs
- Provide a CLI entry point to execute an API by name (to be implemented)
- Keep configuration discoverable from the current working directory (searches upward for `available_api.yaml`)

**Out of scope (for now)**

- Full ETL/data warehousing pipeline
- Long-term persistence (DB, parquet lake, etc.)
- Robust runtime concerns (retries, backoff, caching, auth flows beyond a simple API key)

## Requirements

- Python `>= 3.12`

Key dependencies are defined in `pyproject.toml` (including `click`, `requests`, `pyyaml`).

## Install

Use whichever workflow you prefer:

- With `uv`:
	- `uv sync`
	- or `uv pip install -e .`
- With `pip` (inside a venv):
	- `python -m pip install -e .`

## Usage

After installing the package, the CLI entry point is:

- `api-executor list-apis`
- `api-executor execute-api <api_name>`

Example:

```bash
api-executor list-apis
api-executor execute-api USGS
```

## Configuration

The file `available_api.yaml` contains the API registry.

The YAML loader searches for this file starting from the current working directory and walking up through parent directories, so you can run commands from subfolders.

## Folder structure

```text
.
├── available_api.yaml              # API registry (YAML)
├── pyproject.toml                  # Project metadata + dependencies
└── src/
		└── api_executor/
				├── __init__.py
				├── api/                    # API-specific implementations (currently placeholder)
				├── cli/                    # Click-based CLI entry points
				├── core/                   # Core application logic (currently placeholder)
				├── parsers/                # Parsers/loaders (YAML config loader)
				└── utils/                  # Shared helpers (currently placeholder)
```

