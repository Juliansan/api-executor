import click
from ..core.cli_manager import list_apis
from ..core.cli_manager import execute_api, get_details
from ..utils.logger import setup_logging
from ..utils.formatter import format_api_details


@click.group()
def cli():
    click.echo("\n------------------------")
    click.echo("| API automation calls |")
    click.echo("------------------------\n")
    setup_logging(debug=False)


@cli.command()
@click.option("--api-key", envvar="API_KEY", help="API key for authentication")
@click.option(
    "--param",
    "-p",
    multiple=True,
    help="Query parameters as key=value pairs (e.g., starttime=2024-01-01, minmagnitude=5.0)",
)
@click.argument("api_name")
def run_api(api_name: str, api_key: str | None, param: tuple[str, ...]):
    """
    Execution of API's based on API name

    :param api_name: Name of the API to be executed
    :param param: Query parameters as key=value pairs
    """
    # Parse key=value pairs into a dictionary
    params_dict = {}
    for p in param:
        if '=' in p:
            key, value = p.split('=', 1)
            params_dict[key.strip()] = value.strip()
        else:
            click.echo(f"Warning: Ignoring invalid parameter format '{p}'. Expected key=value format.")
    
    result = execute_api(api_name, api_key, params_dict)
    click.echo(result)


@cli.command()
def list():
    """
    List available API's
    """
    click.echo("Avaliable API's:")
    click.echo("-----------------")
    for value in list_apis():
        click.echo(f"- {value}")


@cli.command()
@click.argument("api_name")
def api_details(api_name: str):
    data = get_details(api_name)
    click.echo(format_api_details(data))


if __name__ == "__main__":
    cli()
