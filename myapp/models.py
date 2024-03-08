from django.db import models
class Test(models.Model):
    test_id = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)  # Assuming single character answers for simplicity
class Submission(models.Model):
    name = models.CharField(max_length=255)
    test_id = models.CharField(max_length=255)
    answers = models.CharField(max_length=255)
    user_answers= models.CharField(max_length=255)
    incorrect_answers = models.TextField()
    def __str__(self):
        return self.name