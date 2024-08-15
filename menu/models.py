from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']  # On ordonne les éléments par le champ 'order'

    def __str__(self):
        return self.title