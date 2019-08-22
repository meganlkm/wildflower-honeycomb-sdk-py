from honeycomb import HoneycombClient

QUERIES = {
    "datapoint": {
        "get": """query getDP($data_id: ID!) {
            getDatapoint(data_id: $data_id) {
            data_id file {key bucketName}}}""",
        "list": "query {datapoints {data {data_id format}}}"
    }
}


def get_client(token_uri, audience, client_id, client_secret, url):
    client_credentials = {
        "token_uri": token_uri,
        "audience": audience,
        "client_id": client_id,
        "client_secret": client_secret,
    }
    return HoneycombClient(url, client_credentials=client_credentials)


def sdk_query(client, obj_type, query, variables=None):
    return client.raw_query(QUERIES[obj_type][query], variables)
