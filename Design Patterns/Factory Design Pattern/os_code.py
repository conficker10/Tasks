from abc import ABCMeta, abstractstaticmethod

class OS(metaclass=ABCMeta):

    @abstractstaticmethod
    def specs():
        pass

class Android(OS):
    def specs(self):
        print('I am an Open Source OS')

class IOS(OS):
    def specs(self):
        print('I am not Open Source')