from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    kafedra = models.ForeignKey(Kafedra, null=True, on_delete=models.SET_NULL)


class Group(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    faculty = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images', null=True)
