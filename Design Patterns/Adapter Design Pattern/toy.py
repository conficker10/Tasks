from abc import ABCMeta, abstractstaticmethod

class MotorCycle(metaclass=ABCMeta):
    @abstractstaticmethod
    def accelerate():
        pass



class Bike(MotorCycle):
    def accelerate():
        print('Broom Vroom...')