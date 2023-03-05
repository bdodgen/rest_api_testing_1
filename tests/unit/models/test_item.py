from tests.unit.models.base_item_test import BaseItemTest


class TestItem(BaseItemTest):
    def test_create_item(self):
        self.assertEqual(self.dummy_item.name, 'Test Item')
        self.assertEqual(self.dummy_item.price, 73.57)

    def test_json(self):
        expected = {'name': 'Test Item', 'price': 73.57}

        self.assertDictEqual(expected, self.dummy_item.json())
