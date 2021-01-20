import statistics

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from movie_reviews.forms import SignUpForm, LoginForm, ReviewForm
from movie_reviews.models import Movies, Reviews, MovieReviewState


def root(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'index.html.j2')


def home(request):
    if request.user.is_authenticated:
        all_movies = Movies.objects.all()
        movies_parsed = []
        for movie in all_movies:
            reviews = [review.star_rating for review in list(Reviews.objects.filter(movie=movie))]
            reviews = [0.0] if len(reviews) == 0 else reviews
            snippet = movie.synopsis[:128] + "..."
            movies_parsed.append((movie.id, movie.name, snippet, f"{statistics.mean(reviews):.2f}"))
        return render(request, 'home.html.j2', {'movies': movies_parsed})
    else:
        return redirect('login')


def movie_redirect(request):
    return redirect('home')


def movies(request, **kwargs):
    if request.user.is_authenticated:
        state = MovieReviewState.NOT_ADDING_REVIEW
        pid = kwargs.pop("pid", 1)
        try:
            selected_movie = Movies.objects.get(id=pid)
        except Movies.DoesNotExist:
            selected_movie = Movies(id=-1, name="Movie not found", synopsis="Movie not found!")

        reviews = Reviews.objects.filter(movie__id=pid)

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                if len(reviews.filter(created_by=request.user)) == 0:
                    form.save_form(request.user, selected_movie)
                    state = MovieReviewState.ADDED_SUCCESSFULLY
                else:
                    state = MovieReviewState.ALREADY_REVIEWED
            else:
                state = MovieReviewState.INVALID_FORM
        return render(
            request,
            'movies.html.j2',
            {
                'movie': selected_movie,
                'reviews': reviews,
                'review_state': state,
                'review_form': ReviewForm()
            }
        )
    else:
        return redirect('login')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'login.html.j2', {'form': form, 'login_failed': True})
        else:
            form = LoginForm()
        return render(request, 'login.html.j2', {'form': form, 'login_failed': False})
    else:
        return redirect('home')


def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.clean_password2()
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('home')
        else:
            form = SignUpForm()
        return render(request, 'signup.html.j2', {'form': form})
    else:
        return redirect('home')
