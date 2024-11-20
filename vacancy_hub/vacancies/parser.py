import requests
from .models import Employer, Vacancy


class HHParser:

    @staticmethod
    def get_employers():
        params = {"per_page": 10, "sort_by": "by_vacancies_open"}
        response = requests.get("http://api.hh.ru/employers/", params)
        if response.status_code == 200:
            data = response.json()["items"]
            for employer_data in data:
                employer, created = Employer.objects.get_or_create(
                    employer_id=employer_data["id"],
                    defaults={"name": employer_data["name"]}
                )
            return Employer.objects.all()

    @staticmethod
    def get_vacancies_from_company(employer_id):
        params = {"per_page": 20, "employer_id": employer_id}
        response = requests.get("http://api.hh.ru/vacancies/", params)
        if response.status_code == 200:
            return response.json()["items"]

    @staticmethod
    def get_all_vacancies():
        employers = HHParser.get_employers()
        for employer in employers:
            employer_vacancies = HHParser.get_vacancies_from_company(employer.employer_id)
            for vacancy_data in employer_vacancies:
                salary_from = vacancy_data["salary"]["from"] if vacancy_data["salary"] else 0
                salary_to = vacancy_data["salary"]["to"] if vacancy_data["salary"] else 0
                Vacancy.objects.create(
                    vacancy_id=vacancy_data["id"],
                    name=vacancy_data["name"],
                    salary_from=salary_from,
                    salary_to=salary_to,
                    employer=employer,
                    url=vacancy_data["alternate_url"]
                )
