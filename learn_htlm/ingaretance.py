class Persons:
    name = 'hemedi'
    heights = 23
    weight = 78

class Details(Persons):
    def man(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.heights}")

details = Details()
details.man()

    