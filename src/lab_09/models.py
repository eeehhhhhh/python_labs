from dataclasses import dataclass
from datetime import datetime, date
import json

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дата должна быть в формате YYYY-MM-DD")
        
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 5")

    def age(self) -> int:
        b = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - b.year
        # Проверяем, был ли уже день рождения в этом году
        if (today.month, today.day) < (b.month, b.day):
            age -= 1
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"]
        )

    def __str__(self):
         return f"студент: {self.fio}, группа: {self.group}, GPA {self.gpa}, возраст: {self.age()}"
    
s = Student(fio="Вася Васин", birthdate="2007-02-12", group="BIVT-25-3", gpa=3.2)
print(f"Возраст: {s.age()}")
print(f"{s.to_dict()}")
s.from_dict(s.to_dict())
print(f"{s.__str__()}")