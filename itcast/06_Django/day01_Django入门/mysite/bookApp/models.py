from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=15)
    date = models.DateField()

    def __str__(self):
        return f'书名: {self.name}, 出版日期: {self.date}'


class Hero(models.Model):
    name = models.CharField(max_length=5)
    gender = models.BooleanField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)    # n:1

    def __str__(self):
        return f'姓名: {self.name}, 性别:{self.gender}, 所属书籍: {self.book}'


# 1.会自动添加id字段






























