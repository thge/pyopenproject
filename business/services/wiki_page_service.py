from abc import ABCMeta, abstractmethod

from business.services.abstract_service import AbstractService


class WikiPageService(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, connection):
        """ Constructor for class WikiPageService, from AbstractService
        :param connection: The connection data
        """
        super().__init__(connection)

    @abstractmethod
    def find(self, wiki_page): raise NotImplementedError

    @abstractmethod
    def find_attachments(self, wiki_page): raise NotImplementedError

    @abstractmethod
    def add_attachment(self, wiki_page, attachment, file_path): raise NotImplementedError
