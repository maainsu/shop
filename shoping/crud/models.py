from django.db import models

class Lecture(models.Model):
    lectureName = models.CharField(max_length=30)
    professor = models.CharField(max_length=10)
    separation = models.CharField(max_length=10)

    def __str__(self):
        return self.lectureName
class Eval(models.Model):
    lect = models.ForeignKey(Lecture, on_delete = models.CASCADE)
    title = models.CharField(max_length = 20)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(blank=True, null = True)
    body = models.TextField()
    def summary(self):
        return self.body[:50]