from food import *

class FoodDecorator(VegFood):
    new_food = VegFood()
    def __init__(self, new_food):
        self.new_food = new_food
    
    def prepare_food(self):
        return self.new_food.prepare_food()
    
    def food_price(self):
        return self.new_food.food_price()


class NonVegFood(FoodDecorator):

    def __init__(self, new_food):
        super(new_food)

    def prepare_food(self):
        return super().prepare_food() + ' with Chicken Gravy'

    def food_price(self):
        return super().food_price() + 150