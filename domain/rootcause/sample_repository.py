from infrastructure.sample import edoc


def get_by_id(sample_id):
    return edoc.query_from_edoc(sample_id)


def save(sample):
    return edoc.save(sample)


def update(sample):
    return edoc.update(sample)
