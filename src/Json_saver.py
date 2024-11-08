from abc import ABC, abstractmethod
from json import JSONDecodeError

from src.Vacancy import Vacancy
import os

import json

# class JSONABC(ABC):

    # @abstractmethod
    # def json_add(self):
    #     pass
    #
    # @abstractmethod
    # def json_del(self):
    #     pass


class JSONSaver:

    def __init__(self, name="data.json"):
        self.name = name
        self.path = os.path.join(os.path.dirname(__file__), "..", "data", self.name)

    def __save_to_file(self, vacancies: list[dict]) -> None:
        """Сохраняет данные в json-файл"""
        with open(self.path, "a", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False)

    def __read_file(self) -> list[dict]:
        """Считывает данные из json-файла"""
        try:
            with open(self.path, encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        except JSONDecodeError:
            data = []
            return data

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавляет вакансию в файл"""
        vacancies_list = self.__read_file()
        print(vacancies_list)
        # if vacancy.alternate_url not in [vac["alternate_url"] for vac in vacancies_list]:
        vacancies_list.append(vacancy.to_dict())
        self.__save_to_file(vacancies_list)
        # else:
        #     print("Ошибка")

    # @staticmethod
    # def open_json(name):
    #     with open(name) as f:
    #         return json.load(f)
    #
    # def add_vacancy(self, vacancy):
    #     dict_vac = {"name": vacancy.name,
    #                 "alternate_url": vacancy.alternate_url,
    #                 "salary": vacancy.salary,
    #                 "requirement": vacancy.requirement}
    #     with open(self.path, "a") as file:
    #         json.dump(dict_vac, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
                      "Опыт работы от 3 лет...")
    j = JSONSaver("makenzy.json")
    print(j.add_vacancy(vacancy))

