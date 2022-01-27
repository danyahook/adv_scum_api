from django.db import models
from django.core.validators import MaxValueValidator


class SiteSettings(models.Model):
    ads_url = models.URLField(unique=True)
    min_day_viewers = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(1000)])
    max_day_viewers = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(1000)])
    click_per_views = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])

    class Meta:
        db_table = 'Site settings'
