import os

import click

from cli import datapoint as dp
from cli.utils import get_client

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--token-uri', default=os.getenv('HC_TOKEN_URI', ''), help="Default environment var HC_TOKEN_URI")
@click.option('--audience', default=os.getenv('HC_AUDIENCE', ''), help="Default environment var HC_AUDIENCE")
@click.option('--client-id', default=os.getenv('HC_CLIENT_ID', ''), help="Default environment var HC_CLIENT_ID")
@click.option('--client-secret', default=os.getenv('HC_CLIENT_SECRET', ''), help="Default environment var HC_CLIENT_SECRET")
@click.option('--url', default=os.getenv('HC_URL', ''), help="Default environment var HC_URL")
@click.pass_context
def cli(ctx, token_uri, audience, client_id, client_secret, url):
    """command line interface for the honeycomb sdk."""
    ctx.ensure_object(dict)
    ctx.obj['client'] = get_client(token_uri, audience, client_id, client_secret, url)


@cli.group()
@click.pass_context
def datapoint(ctx):
    """datapoint functions"""


@datapoint.command('get')
@click.argument('data_id')
@click.option('--file-path', help="Save the downloaded file in this path. Default is the current working directory.")
@click.option('--file-name', help="Save the file as this. Default is the last part of the key being downloaded.")
@click.pass_context
def datapoint_get(ctx, data_id, file_path, file_name):
    """get datapoint"""
    dp.get(ctx, data_id, file_path, file_name)


@datapoint.command('list')
@click.pass_context
def datapoint_list(ctx):
    """list datapoints"""
    dp.list(ctx)


@datapoint.command('put')
@click.pass_context
def datapoint_put(ctx):
    """upload datapoint"""
    dp.put(ctx)


@datapoint.command('delete')
@click.pass_context
def datapoint_delete(ctx):
    """delete datapoint"""
    dp.delete(ctx)
