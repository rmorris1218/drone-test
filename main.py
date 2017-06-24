class Car(object):

    def __init__(self, **kwargs):
        if not kwargs.get('wheels'):
            self.wheels = 4
        else:
            self.wheels = kwargs.get('wheels')
