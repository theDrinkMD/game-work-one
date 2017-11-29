from django.conf.urls import url, include
from django.contrib import admin
from api import views
from api.resources import QuestionResource

question_resource = QuestionResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(question_resource.urls)),
    url(r'^$', views.app_root)
]
