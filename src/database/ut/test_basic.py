import unittest

from parameterized import parameterized

from src.database.database import DataBase


class BasicTest(unittest.TestCase):
    """Test basic functionality for database."""

    def setUp(self):
        self.db = DataBase()

    @parameterized.expand(
        [
            [3, 4, 1, "asda"],
            [24, 1234, 1, "test"],
            [3, 4, 2, "uuu"],
            [239, 143, 14, "kek"],
        ]
    )
    def test_rw(self, s_id: int, t_id: int, hw_id: int, data: str):
        self.db.upload(s_id, t_id, hw_id, data)
        self.assertTrue(data in db.read(t_id, hw_id))

    @parameterized.expand(
        [
            [1, 1, 5],
            [1, 2, 4],
            [2, 1, 3],
            [2, 239, 2],
        ]
    )
    def test_mark(self, s_id: int, hw_id: int, mark: int):
        self.db.upload(s_id, 239, hw_id, "Data")
        self.db.set_mark(hw_id, s_id, mark)
        self.assertEqual(self.db.get_marks(s_id), {hw_id: mark})
