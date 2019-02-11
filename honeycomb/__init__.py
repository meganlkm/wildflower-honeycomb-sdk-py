from honeycomb.models import Query, Mutation, DatapointInput, Datapoint
from gqlpycgen.client import FileUpload, Client


class HoneycombClient:

    def __init__(self, uri=None, accessToken=None, client_credentials=None):
        self.uri = uri
        if self.uri is None:
            self.uri = "https://honeycomb.apparatus.wildflowertesting.org/graphql"
        self.accessToken = accessToken
        self.client_credentials = client_credentials
        assert self.accessToken is not None or self.client_credentials is not None
        self.client = Client(self.uri, self.accessToken, self.client_credentials)
        self.mutation = HoneycombMutation(self.client)
        self.query = HoneycombQuery(self.client)

    def raw_query(self, query, variables):
        return self.query.query(query, variables)


class HoneycombQuery(Query):
    pass


class HoneycombMutation(Mutation):

    def createDatapoint(self, datapoint: DatapointInput) -> Datapoint:
        variables = dict()
        var_types = dict()

        if datapoint is None:
            raise Exception("datapoint is required")
        var_types["datapoint"] = DatapointInput
        if hasattr(datapoint, "to_json"):
            variables["datapoint"] = datapoint.to_json()
        else:
            variables["datapoint"] = datapoint

        query = """mutation createDatapoint ($datapoint: DatapointInput) { createDatapoint(datapoint: $datapoint) {
    data_id
        format
        file {
            name
            filename
            mime
            encoding
            contentType
            size
            created
        }
        observed_time
        system {
            type_name
            created
            last_modified
        }
    }
}
"""
        print(query)
        files = FileUpload()
        filename = datapoint.get("file", {}).get("data")
        if filename is None:
            raise Exception("filename not specified in datapoint.file.data")
        # TODO - make this more robust
        files.add_file("variables.datapoint.file.data", filename, open(filename, 'rb'), 'text/plain')
        results = self.client.execute(query, variables, files)
        print(results)
        return Datapoint.from_json(results.get("createDatapoint"))
