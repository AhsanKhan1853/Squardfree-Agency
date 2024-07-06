from django.urls import path
from . import views
urlpatterns = [
    path("booking/",views.booking,name="booking"),
    path("booking/signUp/",views.signUP,name="signUp"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("about/",views.about,name="about"),
    path("whatwedo/",views.whatwedo,name="WeDo"),
    path("portfolio/",views.portfolio,name="portfolio")

]
