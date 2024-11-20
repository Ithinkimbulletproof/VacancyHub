from django.db import models


class Employer(models.Model):
    employer_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    vacancy_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    salary_from = models.IntegerField(null=True, blank=True)
    salary_to = models.IntegerField(null=True, blank=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.name
