from django.conf.urls import url, include
from django.contrib import admin
from api import views
from api.resources import QuestionResource, PlayerResource, PlayerResponseResource

question_resource = QuestionResource()
player_resource = PlayerResource()
player_response_resource = PlayerResponseResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(question_resource.urls)),
    url(r'^api/', include(player_resource.urls)),
    url(r'^api/', include(player_response_resource.urls)),
    url(r'^displayrandomquestion/', views.display_random_question),
    url(r'^player_response/', views.save_player_response),
    #url(r'^displayquestion/random/', views.display_random_question),
    url(r'^$', views.app_root)
]
