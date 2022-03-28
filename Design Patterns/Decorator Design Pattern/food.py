from abc import ABCMeta, abstractstaticmethod

class Food(metaclass=ABCMeta):
    @abstractstaticmethod
    def prepare_food():
        pass

    def food_price():
        pass

class VegFood(Food):
    def prepare_food(self):
        return "Veg Food"
    
    def food_price(self):
        return 50