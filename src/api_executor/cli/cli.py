import click
from ..core.api_manager import list_available_apis
from ..utils.logger import setup_logging


@click.group()
def cli():
    setup_logging(debug=False)


@cli.command()
@click.option("--api-key", envvar="API_KEY")
@click.argument("api_name")
def execute_api(api_name: str):
    """
    Execution of API's based on API name

    :param api_name: Name of the API to be executed
    """
    print(api_name)


@cli.command()
def list_apis():
    """
    List available API's
    """
    click.echo("Avaliable API's:")
    click.echo("-----------------")
    for value in list_available_apis():
        click.echo(f"- {value}")
    


if __name__ == "__main__":
    cli()
