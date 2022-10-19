from ctypes.wintypes import HWINSTA
from typing import Dict


class DataBase:
    class Key:
        def __init__(self, hw: int, t: int, s: int) -> None:
            self.hw = hw
            self.t = t
            self.s = s

        def __hash__(self) -> int:
            return self.hw.__hash__() ^ self.s.__hash__() ^ self.t.__hash__()

    def __init__(self) -> None:
        self.data = {}

    def upload(self, student_id: int, teacher_id: int, hw_id: int, data: str):
        self.data[DataBase.Key(hw_id, teacher_id, student_id)] = [data, -1]

    def read(self, teacher_id: int, hw_id: int) -> Dict[int, str]:
        res = {}
        for k, v in self.data.items():
            if k.t == teacher_id and k.hw == hw_id:
                res[k.s] = v[0]
        return res

    def set_mark(self, teacher_id: int, hw_id: int, student_id: int, mark: int):
        k = DataBase.Key(hw_id, teacher_id, student_id)
        print(self.data[k])
        # self.data[k][1] = mark

    def get_marks(self, student_id: int, teacher_id: int) -> Dict[int, int]:
        res = {}
        for k, v in self.data.items():
            if k.s == student_id and k.t == teacher_id:
                res[k.hw] = v[1]
        return res


db = DataBase()
