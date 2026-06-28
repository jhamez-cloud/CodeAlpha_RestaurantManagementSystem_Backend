from django.db import models

# Create your models here.
class Table(models.Model):
    class TableStatus(models.TextChoices):
        AVAILABLE = 'AVAILABLE','Available'
        OCCUPIED = 'OCCUPIED','Occupied'
        RESERVED = 'RESERVED','Reserved'
        CLEANING = 'CLEANING','Cleaning'

    table_id = models.CharField(max_length=100,unique=True,editable=False)
    table_number = models.CharField(max_length=100)
    table_status = models.CharField(max_length=100,choices=TableStatus.choices)
    capacity = models.PositiveIntegerField()
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        new = self.pk is None
        super().save(*args,**kwargs)

        if new and not self.table_id:
            self.table_id = f"TABLE-{self.pk:03d}"
            Table.objects.filter(pk=self.pk).update(table_id=self.table_id)

    def __str__(self):
        return f"Table--{self.table_number}"