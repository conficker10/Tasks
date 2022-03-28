from toy import *
from bird import *

class BikeAdapter(MotorCycle):
    def __init__(self, cycle):
        self.cycle = cycle

    def accelerate(self):
        self.cycle.paddle()


if __name__ == '__main__':
    new_cycle = BiCycle
    new_bike = Bike
    new_bike_adapter = BikeAdapter(new_cycle)

    print('------Cycle-------')
    new_cycle.paddle()
    new_cycle.make_sound()

    print('------Bike-------')
    new_bike.accelerate()

    print('------Adapter Bike-------')
    new_bike_adapter.accelerate()