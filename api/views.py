from django.http import JsonResponse

def app_root(request):
    data = {
        'directory': {
            'admin': request.build_absolute_uri('/admin'),
            'api': {
                'question': request.build_absolute_uri('/api/question')
            }
        }
    }
    return JsonResponse(data)
