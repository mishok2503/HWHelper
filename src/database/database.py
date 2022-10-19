from typing import Dict


class DataBase:
    def upload(self, student_id: int, teacher_id: int, hw_id: int, data: str):
        pass

    def read(self, teacher_id: int, hw_id: int) -> str:
        pass

    def set_mark(self, hw_id: int, student_id: int, mark: int):
        pass

    def get_marks(self, student_id: int) -> Dict[int, int]:
        pass


db = DataBase()
