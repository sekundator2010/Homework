from abc import ABC, abstractmethod
class Clothes(ABC):
    @abstractmethod
    def coat(self):
        pass
    def costume(self):
        pass

class BestClothes(Clothes):
    def __init__(self, v, h):
        self.v = v
        self.h = h
    @property
    def coat(self):
        return round(self.v / 6.5 + 0,5)

    @property
    def costume(self):
        return round(self.h * 2 + 0,3)

bclothes = BestClothes(6,7)
print(f'Расход ткани для пальто {bclothes.coat}, для костюма {bclothes.costume}, а общий расход ткани '
      f'{round(bclothes.coat + bclothes.costume)}')



