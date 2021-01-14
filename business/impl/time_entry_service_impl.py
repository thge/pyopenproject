from business.impl.command.time_entry.create import Create
from business.impl.command.time_entry.create_form import CreateForm
from business.impl.command.time_entry.delete import Delete
from business.impl.command.time_entry.find import Find
from business.impl.command.time_entry.find_all import FindAll
from business.impl.command.time_entry.find_between_days import FindBetweenDays
from business.impl.command.time_entry.find_by_context import FindByContext
from business.impl.command.time_entry.find_projects import FindProjects
from business.impl.command.time_entry.find_schema import FindSchema
from business.impl.command.time_entry.update_form import UpdateForm
from business.time_entry_service import TimeEntryService


class TimeEntryServiceImpl(TimeEntryService):

    def find_projects(self):
        return FindProjects().execute()

    def create_form(self, form):
        return CreateForm(form).execute()

    def update_form(self, time_entry, form):
        return UpdateForm(time_entry, form).execute()

    def find_by_context(self, context):
        return FindByContext(context).execute()

    def find_between_days(self, start_date, end_date):
        return FindBetweenDays(start_date, end_date).execute()

    def find(self, time_entry):
        return Find(time_entry).execute()

    def delete(self, time_entry):
        return Delete(time_entry).execute()

    def create(self, time_entry):
        return Create(time_entry).execute()

    def find_all(self, offset, pageSize, filters, sortBy):
        return FindAll(self, offset, pageSize, filters, sortBy).execute()

    def find_schema(self):
        return FindSchema().execute()