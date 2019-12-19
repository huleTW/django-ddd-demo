class Sample(object):
    def __init__(self, id_ex, mark_result=None):
        self.id = id_ex
        if mark_result == None:
            self.mark_result = False
        else:
            self.mark_result = mark_result

    def mark(self):
        self.mark_result = True
