from django import forms


class VacancySearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, required=False, label="Search by keyword")
    salary_from = forms.IntegerField(required=False, label="Min Salary")
    salary_to = forms.IntegerField(required=False, label="Max Salary")
