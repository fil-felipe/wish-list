from django.db import models
from django.urls import reverse


class GiftUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    email = models.EmailField()

    class Meta:
        ordering = ['slug', 'last_name', 'first_name']
        indexes = [models.Index(fields=['slug', 'last_name', 'first_name'])]
        verbose_name = "Obdarowany"
        verbose_name_plural = "Obdarowani"

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("wish_list_app:user_lists", args=[self.slug])


class GiftList(models.Model):
    list_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    list_user = models.ForeignKey(GiftUser, on_delete=models.CASCADE, related_name='gift_lists')

    class Meta:
        ordering = ['list_name']
        indexes = [models.Index(fields=['list_user'])]
        verbose_name = "Lista prezentowa"
        verbose_name_plural = "Listy prezentowe"

    def __str__(self):
        return self.list_name

    def get_absolute_url(self):
        return reverse("wish_list_app:gift_lists", args=[self.list_user.slug, self.slug])


class Gift(models.Model):
    gift_list = models.ForeignKey(GiftList, on_delete=models.CASCADE, related_name='gift_item')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    offer_url = models.URLField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    reserved = models.BooleanField(default=False)
    # reserved_user = models.ForeignKey(PresentUser, models.SET_NULL, blank=True, null=True)
    reserved_user = models.CharField(max_length=250, blank=True, null=True)
    reserved_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created'])]
        verbose_name = "Prezent"
        verbose_name_plural = "Prezenty"

    def __str__(self):
        return self.title

    def get_user_name(self):
        return self.gift_list.list_user.slug

    def get_absolute_url(self):
        return reverse("wish_list_app:gift_lists", args=[self.gift_list.list_user.slug, self.gift_list.slug])

    def get_reserved_url(self):
        return reverse("wish_list_app:reserve_gift", args=[self.gift_list.list_user.slug, self.gift_list.slug, self.slug])
