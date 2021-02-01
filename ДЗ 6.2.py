class Road:
    def __init__(self, _longitude, _width):
        self._long = _longitude
        self._wid = _width
    def general_mas(self, mas_asphalt, thickness ):
        self.mas = mas_asphalt
        self.thick = thickness
        b = self._long * self._wid * self.mas * self.thick
        return b

r = Road(30, 25)

c = r.general_mas(25, 5)
print(f'Масса асфальта, требуемая для данной территории:{round(c / 1000, 2)} тонн')

