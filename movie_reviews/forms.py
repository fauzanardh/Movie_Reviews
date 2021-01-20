from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

from movie_reviews.models import Reviews


def validate_star_rating(value):
    if value < 0.0 or value > 5.0:
        raise ValidationError(
            _('Enter number between 0.0 and 5.0'),
        )


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'username':
                self.fields[field].widget.attrs.update({'autofocus': 'autofocus'})
            if self.fields[field].help_text != '':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'aria-describedby': field,
                })


class LoginForm(forms.Form):
    username = forms.CharField(
        label=_('Username'),
        strip=True,
    )
    password = forms.CharField(
        label=_('password'),
        strip=False,
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'username':
                self.fields[field].widget.attrs.update({'autofocus': 'autofocus'})
            if self.fields[field].help_text != '':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'aria-describedby': field,
                })


class ReviewForm(forms.Form):
    title = forms.CharField(
        max_length=64,
        label=_('Title'),
        help_text=_('Review title, max 64 characters'),
    )
    review = forms.CharField(
        max_length=512,
        label=_('Review'),
        help_text=_('Enter your review here, max 512 characters'),
        widget=forms.Textarea
    )
    star = forms.FloatField(
        label=_('Star Rating'),
        help_text=_('Star rating for this movie 0.0 - 5.0'),
        validators=[validate_star_rating]
    )

    class Meta:
        model = Reviews
        fields = ('title', 'review', 'star')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].help_text != '':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'aria-describedby': field,
                })

    def save_form(self, user, movie, commit=True):
        review = Reviews(
            title=self.cleaned_data.get('title'),
            movie=movie,
            text=self.cleaned_data.get('review'),
            star_rating=self.cleaned_data.get('star'),
            created_by=user
        )
        if commit:
            review.save()
        return review

