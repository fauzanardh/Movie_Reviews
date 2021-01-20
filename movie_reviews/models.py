from enum import Enum

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


class MovieReviewState(Enum):
    UNKNOWN = -1
    NOT_ADDING_REVIEW = 0
    ADDED_SUCCESSFULLY = 1
    ALREADY_REVIEWED = 2
    INVALID_FORM = 3


class Movies(models.Model):
    name = models.CharField(max_length=128, verbose_name=_("movie title").title(), default=_("unknown movie"))
    synopsis = models.TextField(verbose_name=_("synopsis").title())

    class Meta:
        verbose_name = _("movie")
        verbose_name_plural = _("movies")
        ordering = ("id",)

    def __str__(self):
        return self.name


# class Users(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name="Id")
#     uname = models.CharField(max_length=32, verbose_name="Username")
#     pwd_hash = models.CharField(max_length=32, verbose_name="Hashed Password")
#     f_name = models.CharField(max_length=32, verbose_name="First Name")
#     l_name = models.CharField(max_length=32, verbose_name="Last Name")
#
#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "Users"
#         ordering = ("id",)
#
#     def __str__(self):
#         return f"{self.uname} ({self.f_name} {self.l_name})"


class Reviews(models.Model):
    title = models.CharField(max_length=64, verbose_name=_("review title").title(), default=_("missing title"))
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name=_("reviewed movies").title())
    text = models.TextField(verbose_name=_("review text").title())
    star_rating = models.FloatField(verbose_name=_("star rating").title())
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("movie reviewer").title())
    created_on = models.DateField(auto_now=True, verbose_name=_("reviewed on").title())

    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")
        ordering = ("id",)

    def __str__(self):
        return f"[{self.movie.name}] {self.star_rating}★ -{self.created_by}"
