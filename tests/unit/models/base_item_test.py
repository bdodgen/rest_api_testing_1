from unittest import TestCase

from models.item import ItemModel

class BaseItemTest(TestCase):
    def setUp(self):
        self.dummy_item = ItemModel('Test Item', 73.57)