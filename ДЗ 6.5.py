class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self, a):
        self.a = a
        print(self.a)
class Pen(Stationery):
    pass
class Pencil(Stationery):
    pass
class Handle(Stationery):
    pass

pen = Pen('pen')
pen.draw('Запуск рисования')
pencil = Pencil('pencil')
pencil.draw('Прорисовка')
handle = Handle('handle')
handle.draw('Рисуем')


