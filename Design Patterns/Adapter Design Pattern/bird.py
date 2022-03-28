from abc import ABCMeta, abstractstaticmethod

class Cycle(metaclass=ABCMeta):
    @abstractstaticmethod
    def paddle():
        pass
    def make_sound():
        pass

class BiCycle(Cycle):
    def paddle():
        print('Paddling....')
    def make_sound():
        print('Tring.....')