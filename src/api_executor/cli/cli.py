import click
from ..parsers.yaml_parser import retrieve_yaml_atributes


@click.group()
def cli():
    pass


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
    for value in retrieve_yaml_atributes('name'):
        click.echo(f"- {value}")
    


if __name__ == "__main__":
    cli()
