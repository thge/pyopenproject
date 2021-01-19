import json

from model.query import Query
from tests.test_cases.openproject_test_case import OpenProjectTestCase


class QueryServiceTestCase(OpenProjectTestCase):

    def setUp(self):
        super().setUp()
        self.querySer = self.factory.get_query_service()
        with open('../data/query.json') as f:
            self.query = Query(json.load(f))

    def test_update(self):
        self.assertIsNotNone(self.querySer.update(self.query))

    def test_find(self):
        self.assertIsNotNone(
            self.querySer.find(self.query, offset, pageSize, filters, columns, sortBy, groupBy, showSums,
                               timelineVisible,
                               timelineLabels, timelineZoomLevel, highlightingMode, highlightedAttributes,
                               showHierarchies))

    def test_delete(self):
        self.assertIsNotNone(self.querySer.delete(self.query))

    def test_star(self):
        self.assertIsNotNone(self.querySer.star(self.query))

    def test_unstar(self):
        self.assertIsNotNone(self.querySer.unstar(self.query))

    def test_find_all(self):
        self.assertIsNotNone(self.querySer.find_all(filters))

    def test_create(self):
        self.assertIsNotNone(self.querySer.create(self.query))

    def test_create_form(self):
        self.assertIsNotNone(self.querySer.create_form(form))

    def test_schema(self):
        self.assertIsNotNone(self.querySer.schema())
