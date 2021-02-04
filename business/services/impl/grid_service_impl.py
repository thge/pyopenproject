from business.services.grid_service import GridService
from business.services.impl.command.grid.create import Create
from business.services.impl.command.grid.create_form import CreateForm
from business.services.impl.command.grid.find import Find
from business.services.impl.command.grid.find_all import FindAll
from business.services.impl.command.grid.update import Update
from business.services.impl.command.grid.update_form import UpdateForm


class GridServiceImpl(GridService):
    def __init__(self, connection):
        super().__init__(connection)

    def find(self, grid):
        return Find(self.connection, grid).execute()

    def find_all(self, offset=None, page_size=None, filters=None, sort_by=None):
        return list(FindAll(self.connection, offset, page_size, filters, sort_by).execute())

    def create(self, grid):
        return Create(self.connection, grid).execute()

    def update(self, grid):
        return Update(self.connection, grid).execute()

    def create_form(self, grid):
        return CreateForm(self.connection, grid).execute()

    def update_form(self, grid, grid_form):
        return UpdateForm(self.connection, grid, grid_form).execute()
