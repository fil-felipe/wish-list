from django.db import models


class PresentUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        ordering = ['last_name', 'first_name']
        indexes = [models.Index(fields=['last_name', 'first_name'])]


class PresentList(models.Model):
    list_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    list_user = models.ForeignKey(PresentUser, on_delete=models.CASCADE, related_name='present_lists')

    class Meta:
        ordering = ['list_name']
        indexes = [models.Index(fields=['list_user'])]

    def __str__(self):
        return self.list_name


class Present(models.Model):
    present_list = models.ForeignKey(PresentList, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    offer_url = models.URLField()
    image_url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    reserved = models.BooleanField(default=False)
    reserved_user = models.ForeignKey(PresentUser, models.SET_NULL, blank=True, null=True,)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created'])]

    def __str__(self):
        return self.title
