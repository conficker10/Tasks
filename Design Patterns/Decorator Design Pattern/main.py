from food import *
from decorator_food import *

if __name__ == '__main__':
    vf = VegFood()
    print(vf.prepare_food())
    print(vf.food_price())

    nvf = NonVegFood(VegFood)
    print(nvf.prepare_food()) 
    print(nvf.food_price())