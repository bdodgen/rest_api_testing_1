from tests.base_test import BaseTest
from models.item import ItemModel


class TestItem(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('Test Item', 73.57)
            err_msg_file_found = f"Found an item with the name {item.name}, but did not expect to."
            err_msg_file_not_found = f"Did not find an item with the name {item.name}."

            self.assertIsNone(ItemModel.find_by_name('Test Item'), err_msg_file_found)

            item.save_to_db()
            self.assertIsNotNone(ItemModel.find_by_name('Test Item'), err_msg_file_not_found)

            item.delete_from_db()
            self.assertIsNone(ItemModel.find_by_name('Test Item'), err_msg_file_found)
