import conversiontables

# Unit Class
class Unit:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def change_value(self, value):
        self.value = value

#Weight Classes
class Weight(Unit):
    def __init__(self, value):
        super().__init__(value)
        self.kind = "Weight"

    def convert(self, output):
        try:
            kgs = self.value * conversiontables.tokg[self.name]
            return kgs * conversiontables.fromkg[output]
        except KeyError:
            return "Not a supported unit!"

class Kilograms(Weight):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "kg"
        self.name = "kilograms"


class Pounds(Weight):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "lb"
        self.name = "pounds"


class Stone(Weight):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "st"
        self.name = "stone"


class Imperial_Ton(Weight):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "ton"
        self.name = "imperial ton"


class US_Ton(Weight):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "US ton"
        self.name = "US ton"


class Ounce(Weight):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "oz"
        self.name = "ounce"

#Length Classes
class Length(Unit):
    def __init__(self, value):
        super().__init__(value)
        self.kind = "Length"

    def convert(self, output):
        try:
            meters = self.value * conversiontables.tom[self.name]
            return meters * conversiontables.fromm[output]
        except KeyError:
            return "Not a supported unit!"

class Metres(Length):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "m"
        self.name = "metre"

class Foot(Length):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "ft"
        self.name = "foot"

class Yard(Length):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "yd"
        self.name = "yard"

class Furlong(Length):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "fur"
        self.name = "furlong"

class Inch(Length):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "in"
        self.name = "inch"

class Mile(Length):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "mi"
        self.name = "mile"

class Kilometre(Length):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "km"
        self.name = "kilometre"

#Velocity Classes
class Velocity(Unit):
    def __init__(self, value):
        super().__init__(value)
        self.kind = "Velocity"

    def convert(self, output):
        try:
            metres = self.value * conversiontables.to_m_per_s[self.name]
            return metres * conversiontables.from_m_per_s[output]
        except KeyError:
            return "Not a supported unit!"

class Metres_Per_Second(Velocity):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "m/s"
        self.name = "metres per second"

class Miles_Per_Hour(Velocity):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "mph"
        self.name = "miles per hour"

class Kilometres_Per_Hour(Velocity):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "kmph"
        self.name = "kilometres per hour"

class Feet_Per_Second(Velocity):
    def __init__(self, value):
        super().__init__(value)
        self.symbol = "fps"
        self.name = "feet per second"

mass = Pounds(25)
velocity = Metres_Per_Second(25)
length = Furlong(25)

print(mass.convert("ounces"))
print(velocity.convert("feet per second"))
print(length.convert("inch"))

