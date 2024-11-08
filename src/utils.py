from src.Vacancy import Vacancy
from src.work_with_HH import HeadHunterAPI


def get_top_vacancies(sorted_vacancies, top_n):
    """Топ вакансий"""
    if top_n == '':
        return sorted_vacancies
    else:
        return sorted_vacancies[0:int(top_n)]


def filter_vacancies(vacancies_list, filter_words):
    """Фильтрация вакансий по ключевому слову"""
    filter_list_new = []
    for word in filter_words:
        for vac in vacancies_list:
            print(type(word))
            print(vac)
            if word in vac.get("description"):
                print("аовыал")
                filter_list_new.append(vac)
    return filter_list_new


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    salary_list = salary_range.split(" - ")
    print(salary_list)
    new_list = []
    for vac in filtered_vacancies:
        if int(salary_list[0]) <= vac["salary"] <= int(salary_list[1]):
            new_list.append(vac)
    return new_list


def filter_by_salary(vacancies_list):
    sorted_vacancies = sorted(vacancies_list, key=lambda vacancies_list: vacancies_list["salary"], reverse=True)
    return sorted_vacancies


if __name__ == "__main__":
    hh_api = HeadHunterAPI()

    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.load_vacancies("Python")
    # print(hh_vacancies)
    # print(type(hh_vacancies))
    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    print(vacancies_list)
    sorted_vacancies = filter_by_salary(vacancies_list)
    # print(get_top_vacancies(sorted_vacancies, "5"))
    print(filter_vacancies(vacancies_list, ["Python"]))
    print(get_vacancies_by_salary(vacancies_list, "100000 - 150000"))
