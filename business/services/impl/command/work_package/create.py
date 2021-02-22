import model.work_package as wp
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.work_package.work_package_command import WorkPackageCommand
from util.URL import URL
from util.URLParameter import URLParameter


class Create(WorkPackageCommand):

    def __init__(self, connection, work_package, notify):
        """ Constructor for class Create, from WorkPackageCommand

        :param connection: The connection data
        :param work_package: The work package to create
        :param notify: Do you want to notify to watchers?
        """
        super().__init__(connection)
        self.work_package = work_package
        self.notify = notify

    def execute(self):
        try:
            json_obj = PostRequest(connection=self.connection,
                                   headers={"Content-Type": "application/json"},
                                   context=str(URL(f"{self.CONTEXT}",
                                                   [
                                                       URLParameter("notify", self.notify)
                                                   ])),
                                   json=self.work_package.__dict__).execute()
            return wp.WorkPackage(json_obj)
        except RequestError as re:
            raise BusinessError("Error creating work package") from re
