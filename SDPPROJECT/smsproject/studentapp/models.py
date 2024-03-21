from django.db import models

class QuizResult(models.Model):
    id = models.AutoField(primary_key=True)
    sid = models.CharField(max_length=15, blank=False)
    quiz_title = models.CharField(max_length=30, blank=False)
    quiz_score = models.IntegerField(blank=False)
    submit_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "quizresult_table"

