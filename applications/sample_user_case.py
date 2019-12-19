import json

from django.http import JsonResponse

from domains.rootcauses import sample_domain_service as sample_service


def sample(request):
    print(request.method)
    response = None
    if request.method == 'GET':
        response = mark_sample(request)
    if request.method == 'POST':
        response = create_sample(request)
    return response


def mark_sample(request):
    sample_id = request.GET['sampleId']
    sample = sample_service.get_by_id(sample_id)
    sample.mark()
    sample_service.update(sample)
    return JsonResponse(sample.__dict__)


def create_sample(request):
    sample_request = json.loads(request.body)
    sample_created = sample_service.save(sample_request["id"])
    return JsonResponse(sample_created.__dict__)
