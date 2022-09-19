
from graphene.test import Client
from bib.schema import schema
from snapshottest import TestCase


class AuthorTestCase(TestCase):
    client = Client(schema)
    def testBookById(self):
        query = ''' query { bookById(bookId: 1) { id titel } } '''
        
        response = self.client.execute(query)
        expected = {'data': {'bookById': {'id': '1', 'titel': 'C++ New Release'}}}
        # print("------------: ", response)
        self.assertEqual(response, expected)
        self.assertMatchSnapshot(self.client.execute(query))

    def testAllAuthors(self):
        query = ''' query { allAuthors { id vorname name } } '''
        response = self.client.execute(query)
        expected = {'data': {'allAuthors': [{'id': '1', 'vorname': 'Muster', 'name': 'Max'}, {'id': '2', 'vorname': 'Rabin', 'name': 'Mueller'}]}}
        # print("------------: ", response)
        self.assertEqual(response, expected)
        self.assertMatchSnapshot(self.client.execute(query))
    
