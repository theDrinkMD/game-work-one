from tastypie.resources import ModelResource
from api.models import Question
from tastypie.authorization import Authorization

class QuestionResource(ModelResource):
    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'
        authorization = Authorization()
