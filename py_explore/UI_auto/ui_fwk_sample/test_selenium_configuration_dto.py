
class TestSeleniumConfigurationDTO( object):
    def __init__(self, **params):
        for param in params.keys():
            setattr(self, param, params[param])

    def __repr__(self):
        return str(self.__dict__)


