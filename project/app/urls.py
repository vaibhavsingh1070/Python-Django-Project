from django.urls import path
from app import views


urlpatterns = [
   path('',views.index,name="index"),
   path('about',views.about,name="about"),
   path('create',views.create, name="create"),
   path('insert',views.insert,name="insert"),
   path('update/<id>',views.update,name="update"),
   path('delete/<id>',views.delete,name="delete"),
   path('updatepage',views.updatepage,name="updatepage"),
   path('deletepage',views.deletepage,name="deletepage"),
   path('deleteview/<id>',views.deleteview,name="deleteview"),
   path('test',views.test,name="test"),
]