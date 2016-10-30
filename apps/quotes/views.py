from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Quote, Favorite


# Create your views here.
def index(request):
	if 'logged_user' not in request.session:
		return redirect('/')

	user = User.objects.get(id = request.session['logged_user'])
	allposts = Quote.objects.exclude(favorite__favoritedby = user)
	favorites = Favorite.objects.filter(favoritedby = user)
	context = {
		'allposts': allposts,
		'favorites': favorites
	}
	return render(request, 'quotes/index.html', context)

def addQuote(request):
	#if request method == POST
	post = request.POST
	user = User.objects.get(id = request.session['logged_user'])
	Quote.objects.create(postedby=user, quotedby=post['quotedby'], message=post['message'])
	return redirect('quotes:index')

def addFavorite(request,quoteid):
	post = Quote.objects.get(id = quoteid)
	user = User.objects.get(id = request.session['logged_user'])
	Favorite.objects.create(favoritequote = post, favoritedby = user)
	return redirect('quotes:index')

def removeFavorite(request, quoteid):
	toBeDeleted = Favorite.objects.get(id=quoteid)
	toBeDeleted.delete()
	return redirect('quotes:index')

def showUser(request, userid):
	user = User.objects.get(id = userid)
	allposts = Quote.objects.filter(postedby = user)
	alias = user.alias
	count = len(allposts)
	context = {
		'allposts': allposts,
		'count': count,
		'alias': alias
	}
	return render(request, 'quotes/showuser.html', context)