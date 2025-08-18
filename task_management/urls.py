from django.contrib import admin
from django.urls import path,include
from task.views import home
from task.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('contact/',contact),
    path('task/', include('task.urls'))
]
