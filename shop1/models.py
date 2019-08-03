import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class Book(models.Model):
    """本のモデル"""
    class Meta:
        db_table = 'book'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_('タイトル'), max_length=20)
    price = models.IntegerField(_('価格'), null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    