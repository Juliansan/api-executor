import click
from ..core.cli_manager import list_apis
from ..core.cli_manager import execute_api
from ..utils.logger import setup_logging


@click.group()
def cli():
    click.echo("This is an application for calling API's available")
    setup_logging(debug=False)


@cli.command()
@click.option("--api-key", envvar="API_KEY")
@click.argument("api_name")
def api(api_name: str, api_key: str | None):
    """
    Execution of API's based on API name

    :param api_name: Name of the API to be executed
    """
    result = execute_api(api_name, api_key)
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
def get_details(api_name: str):
    pass


if __name__ == "__main__":
    cli()
