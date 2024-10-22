from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class ChildUser(User):
    parent_user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='children', verbose_name="Rodzic"
    )

    email = None
    password = None

    class Meta:
        indexes = [models.Index(fields=["parent_user"])]
        verbose_name = "Użytkownik dziecko"
        verbose_name_plural = "Użytkownicy dziecko"

    def __str__(self):
        return f"Child: {self.username}, Parent: {self.parent_user.username}"


class WishList(models.Model):
    list_name = models.CharField(max_length=250, verbose_name="Nazwa listy")
    slug = models.SlugField(max_length=250)
    list_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gift_lists_user", verbose_name="Obdarowany")
    list_creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="gift_lists_creator")

    class Meta:
        ordering = ["list_name"]
        indexes = [models.Index(fields=["list_user"])]
        verbose_name = "Lista prezentowa"
        verbose_name_plural = "Listy prezentowe"

    def __str__(self):
        return self.list_name

    def get_absolute_url(self):
        return reverse("wish_list_app:gift_lists", args=[self.list_user.username, self.slug])

class Gift(models.Model):
    gift_list = models.ForeignKey(WishList, on_delete=models.CASCADE, related_name="gift_item", verbose_name="Lista prezentów")
    title = models.CharField(max_length=250, verbose_name="Co to za prezent")
    slug = models.SlugField(max_length=250)
    offer_url = models.URLField(null=True, blank=True, verbose_name="Link do oferty")
    image_url = models.URLField(null=True, blank=True, verbose_name="Link do zdjęcia")
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name="gift_creator")
    reserved = models.BooleanField(default=False)
    reserved_user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, verbose_name="Osoba rezerwująca")
    reserved_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["created"]
        indexes = [models.Index(fields=["created"])]
        verbose_name = "Prezent"
        verbose_name_plural = "Prezenty"

    def __str__(self):
        return self.title

    def get_user_name(self):
        return self.gift_list.list_user.username

    def get_absolute_url(self):
        return reverse("wish_list_app:gift_lists", args=[self.gift_list.list_user.username, self.gift_list.slug])

    def get_reserved_url(self):
        return reverse(
            "wish_list_app:reserve_gift", args=[self.gift_list.list_user.username, self.gift_list.slug, self.slug]
        )
