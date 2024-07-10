from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class Time(models.Model):
    vaqti = models.CharField(max_length=20)

    def __str__(self):
        return self.vaqti

class Polyabron(models.Model):
    ismfamilya = models.CharField(max_length=100)
    jamo1 = models.CharField(max_length=100)
    jamo2 = models.CharField(max_length=100)
    kun = models.DateField()
    vaqti = models.ForeignKey(Time, on_delete=models.CASCADE)
    tel_raqam = models.CharField(max_length=15)
    tel_raqam2 = models.CharField(max_length=15)
    izoh = models.TextField(blank=True)

    def clean(self):
        if self.pk is not None:  # If the object is being updated
            return
        if self.kun < timezone.now().date():
            raise ValidationError({'kun': 'Sana bugundan oldin bo`lishi mumkin emas'})
        if Polyabron.objects.filter(kun=self.kun, vaqti=self.vaqti).exists():
            raise ValidationError({'vaqti': 'Bu vaqt band etilgan'})

    def __str__(self):
        return self.ismfamilya

    @staticmethod
    def get_available_slots():
        available_slots = {}
        today = timezone.now().date()
        all_slots = Time.objects.all()

        for i in range(30):
            date = today + timedelta(days=i)
            booked_slots = Polyabron.objects.filter(kun__gte=date).values_list('vaqti_id', flat=True)
            available_slots[date] = [slot for slot in all_slots if slot.id not in booked_slots]

        return available_slots
