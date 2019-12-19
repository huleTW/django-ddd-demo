from domain.rootcause import algorithm
from domain.rootcause.sample import Sample
from infrastructure.sample import edoc as repo


def get_by_id(sample_id):
    return repo.query_from_edoc(sample_id)


def update(sample):
    return repo.update(sample)


def save(sample_id):
    if algorithm.analysis("analysis content"):
        return repo.save(Sample(algorithm.rest_call(sample_id)))
    else:
        return Sample("invalid")
