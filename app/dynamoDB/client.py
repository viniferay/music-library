from uuid import uuid4

import boto3


class DynamoDBClient:

    def __init__(self, app=None):
        if app:
            self.init_client(app)

    def init_client(self, app):
        self.aws_secret_access_key = app.config.get('AWS_SECRET_ACCESS_KEY', None)
        self.aws_access_key_id = app.config.get('AWS_ACCESS_KEY_ID', None)

        self.resource = boto3.resource('dynamodb', region_name='us-east-2',
                                   aws_access_key_id=self.aws_access_key_id,
                                   aws_secret_access_key=self.aws_secret_access_key)

    def put_data(self, artist_name):
        self.resource.Table('artists').put_item(Item={'id': str(uuid4()), 'artist_name': artist_name})