from tastypie.resources import ModelResource
from api.models import Question, Player, PlayerResponse
from tastypie.authorization import Authorization

class QuestionResource(ModelResource):
    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'
        authorization = Authorization()

class PlayerResource(ModelResource):
    class Meta:
        queryset = Player.objects.all()
        resource_name = 'player'
        authorization = Authorization()

class PlayerResponseResource(ModelResource):
    class Meta:
        queryset = PlayerResponse.objects.all()
        resource_name = 'player_response'
        authorization = Authorization()
