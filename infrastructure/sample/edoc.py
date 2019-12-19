from domain.rootcause.sample import Sample
from infrastructure.sample.sample_models import SampleData

edoc_path = "/path"


def _to_sample(sample_data):
    return Sample(sample_data.id_name, sample_data.mark_result)


def query_from_edoc(sample_id):
    return _to_sample(SampleData.objects.get(id_name=sample_id))


def save(sample):
    data = SampleData.objects.create(id_name=sample.id, mark_result=sample.mark_result)
    data.save()
    return _to_sample(data)


def update(sample):
    data = SampleData.objects.get(id_name=sample.id)
    data.mark_result = sample.mark_result
    data.save()
