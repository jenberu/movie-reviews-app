from django.shortcuts import render , get_object_or_404,redirect
from django.http import HttpResponse
from .models import Movie, Review,Like,Movie_Like
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def home(request):
  searchTerm = request.GET.get('searchMovie')
  if searchTerm:
    movies=Movie.objects.filter(title__icontains=searchTerm)
    if movies:
        return render(request, 'home.html',{'searchTerm':searchTerm, 'movies': movies})
    else:
      return render(request, 'home.html',{'searchTerm':searchTerm, 'movies': movies, 'nodata': 'there is no related movie'})
  else:
    movies=Movie.objects.all()
    return render(request, 'home.html',{'searchTerm':searchTerm, 'movies': movies})
# Create your views here.
def about(request):
 return HttpResponse('<h1>Welcome to About Page</h1>')
def signup(request):
 email = request.GET.get('email')
 return render(request, 'signup.html', {'email':email})
def detail(request,movie_id):
  movie=get_object_or_404(Movie,pk=movie_id)
  
  if request.method=='POST':
   like,created=Movie_Like.objects.get_or_create(user=request.user,movie=movie)
   if not created:
     like.delete() 
  reviews=Review.objects.filter(movie=movie)
  total_comments=reviews.count()
 
  return render(request, 'detail.html', {'movie':movie,'reviews':reviews,'total_comments':total_comments})
"""We use get_object_or_404 to get the specific movie object we want. 
We provide movie_id as the primary key, pk=movie_id. If there is a match, 
get_object_or_404, as its name suggests, returns us the object or the not 
found (404) object """
@login_required
def createreview(request, movie_id):
  movie=get_object_or_404(Movie,pk=movie_id)
  if request.method=='GET':
    return render(request,'createreview.html',{'form':ReviewForm(), 'movie':movie})
  else:
    try:
      form=ReviewForm(request.POST)
      newReview=form.save(commit=False)# set additional fields on the model instance before saving it to the database
      newReview.user=request.user  # Assign the currently logged-in user to the review
      newReview.movie=movie
      newReview.save()
      return redirect('detail',newReview.movie.id)
    except ValueError:
      return render(request,'createreview.html',{'form':ReviewForm(),'error':'bad data passed in'})
@login_required
def updatereview(request,review_id):
  review=get_object_or_404(Review,pk=review_id,user=request.user)
  if request.method=='GET':
    form=ReviewForm(instance=review)
    return render(request,'updatereview.html',{'review':review,'form':form})
  else:
    try:
      form=ReviewForm(request.POST,instance=review)
      form.save()
      return redirect('detail',review.movie.id)
    except ValueError:
      return render(request,'updatereview.html',{'review': review,'form':form,'error':'Bad data in form'})
    
@login_required
def deletereview(request,review_id):
  review=get_object_or_404(Review,pk=review_id,user=request.user)
  review.delete()
  return redirect('detail', review.movie.id)

@login_required
def like_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    # Check if the user has already liked the review
    like, created = Like.objects.get_or_create(user=request.user, review=review)
    if not created:
      like.delete()
        # If the like is created, increment the review's like count

    return redirect('detail', review.movie.id)

    
      




