from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^addquote$', views.addQuote, name="addquote"),
	url(r'^addfavorite/(?P<quoteid>\d+)$', views.addFavorite, name="addfavorite"),
	url(r'^removefavorite/(?P<quoteid>\d+)$', views.removeFavorite, name="removefavorite"),
	url(r'^users/(?P<userid>\d+)$', views.showUser, name="showuser"),
]
