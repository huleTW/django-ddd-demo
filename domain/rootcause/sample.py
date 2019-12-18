class Sample(object):
    def __init__(self, id_ex):
        self.id = id_ex
        self.mark_result = False

    def mark(self):
        self.mark_result = True
