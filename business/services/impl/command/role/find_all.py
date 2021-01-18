import json

from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.get_request import GetRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.role.role_command import RoleCommand
from model.role import Role


class FindAll(RoleCommand):

    def __init__(self, connection, filters):
        super().__init__(connection)
        self.filters = filters

    def execute(self):
        try:
            json_obj = GetRequest(self.connection, f"{self.CONTEXT}?{self.filters}").execute()
            for tEntry in json.loads(json_obj):
                yield Role(tEntry)
        except RequestError as re:
            raise BusinessError(f"Error finding all roles with filters: {self.filters}") from re
