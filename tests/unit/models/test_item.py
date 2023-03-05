from tests.unit.models.base_item_test import BaseItemTest


class TestItem(BaseItemTest):
    def test_create_item(self):
        def err_msg(property: str) -> str:
            return f"The {property} of the item after creation does not equal the constructor argument."

        self.assertEqual(self.dummy_item.name, 'Test Item', err_msg("name"))
        self.assertEqual(self.dummy_item.price, 73.57, err_msg("price"))

    def test_item_json(self):
        expected = {'name': 'Test Item', 'price': 73.57}
        test_input = self.dummy_item.json()
        err_msg = f"The JSON export of the item is incorrect. Received: {test_input}, Expected: {expected}"

        self.assertDictEqual(expected, test_input, err_msg)
