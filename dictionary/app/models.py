from django.db import models
import uuid

class Word(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word

class Meaning(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # word = models.ForeignKey(Word, on_delete=models.CASCADE)
    word = models.OneToOneField(Word, on_delete=models.CASCADE, related_name='meaning')
    meaning = models.TextField()

    def __str__(self):
        # return f"{self.word}: {self.meaning}"
        return self.meaning

