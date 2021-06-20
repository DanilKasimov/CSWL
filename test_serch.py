import unittest
from Db import Db


class SearchTestCase(unittest.TestCase):
    def test_search(self):
        self.assertEqual(Db().Search('Поставщик', '89349502738', 1), [[1, 'ООО ТТБуБу', '89349502738']])


if __name__ == '__name__':
    unittest.main()
