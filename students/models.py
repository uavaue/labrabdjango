from django.db import models


# Create your models here.
class Group(models.Model):
    name_of_group = models.CharField(max_length=200, verbose_name="Название группы")
    faculty = models.ForeignKey("students.Faculties", on_delete=models.CASCADE, verbose_name="Факультет")

    def __str__(self):
        return self.name_of_group

    class Meta:
        verbose_name = "Группы"
        verbose_name_plural = "Группы"
        db_table = "group"


class Directions(models.Model):
    name_of_direction = models.CharField(max_length=200, verbose_name="Название направления")

    def __str__(self):
        return self.name_of_direction

    class Meta:
        verbose_name = "Направления"
        verbose_name_plural = "Направления"
        db_table = "direction"


class Subjects(models.Model):
    name_of_subject = models.CharField(max_length=200, verbose_name="Название дисциплины")
    direction = models.ForeignKey("students.Directions", on_delete=models.CASCADE, verbose_name="Направление")

    def __str__(self):
        return self.name_of_subject

    class Meta:
        verbose_name = "Дисциплины"
        verbose_name_plural = "Дисциплины"
        db_table = "subject"


class Faculties(models.Model):
    name_of_faculties = models.CharField(max_length=200, verbose_name="Название факультета")
    direction = models.ForeignKey("students.Directions", on_delete=models.CASCADE,
                                  verbose_name="Направление подготовки")

    def __str__(self):
        return self.name_of_faculties

    class Meta:
        verbose_name = "Факультеты"
        verbose_name_plural = "Факультеты"
        db_table = "faculty"


class Student(models.Model):
    FIO = models.CharField(max_length=200, verbose_name="ФИО")
    email = models.CharField(max_length=200, verbose_name="email")
    group = models.ForeignKey("students.Group", on_delete=models.CASCADE, verbose_name="Группа")

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = "Студенты"
        verbose_name_plural = "Студенты"
        db_table = "student"
