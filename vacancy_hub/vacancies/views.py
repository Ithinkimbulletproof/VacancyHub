from django.shortcuts import render
from .models import Vacancy
from .forms import VacancySearchForm


def vacancy_list(request):
    form = VacancySearchForm(request.GET)
    vacancies = Vacancy.objects.all()

    if form.is_valid():
        keyword = form.cleaned_data.get("keyword")
        salary_from = form.cleaned_data.get("salary_from")
        salary_to = form.cleaned_data.get("salary_to")

        if keyword:
            vacancies = vacancies.filter(name__icontains=keyword)
        if salary_from:
            vacancies = vacancies.filter(salary_from__gte=salary_from)
        if salary_to:
            vacancies = vacancies.filter(salary_to__lte=salary_to)

    return render(request, 'vacancies/vacancy_list.html', {'vacancies': vacancies, 'form': form})
