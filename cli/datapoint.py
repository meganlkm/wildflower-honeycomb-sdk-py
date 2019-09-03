import os

import boto3
import click

from cli.utils import get_client, sdk_query


def get(ctx, data_id, file_path, file_name):
    """get datapoint"""
    variables = {
        "data_id": data_id
    }
    response = sdk_query(ctx.obj['client'], 'datapoint', 'get', variables)
    try:
        bucket = response['getDatapoint']['file']['bucketName']
        key = response['getDatapoint']['file']['key']
    except TypeError:
        # raise Exception('Datapoint not found.')
        return click.echo('Datapoint not found.', err=True)

    click.echo('Downloading: {}'.format(os.path.join(bucket, key)))
    if not file_path:
        file_path = os.getcwd()
    if not file_name:
        file_name = '{}-{}'.format(data_id, key.split('/').pop())
    file_ext = key.split('.').pop()
    if not file_name.endswith(file_ext):
        file_name += '.{}'.format(file_ext)
    save_path = os.path.join(file_path, file_name)

    s3 = boto3.resource('s3')
    s3.meta.client.download_file(bucket, key, save_path)
    return click.echo('File saved: {}'.format(save_path))


def list(ctx):
    """list datapoints"""
    response = sdk_query(ctx.obj['client'], 'datapoint', 'list')
    return click.echo(response)


def put(ctx):
    """upload datapoint"""
    return click.echo('TODO')


def delete(ctx):
    """delete datapoint"""
    return click.echo('TODO')
