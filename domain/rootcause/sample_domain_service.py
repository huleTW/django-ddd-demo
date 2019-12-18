from domain.rootcause import sample_repository
from domain.rootcause.sample import Sample


def get_by_id(sample_id):
    return sample_repository.get_by_id(sample_id)


def update(sample):
    return sample_repository.update(sample)


def save(sample_id):
    return sample_repository.save(Sample(sample_id))
