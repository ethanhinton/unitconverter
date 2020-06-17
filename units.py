import conversiontables

# Unit Class
class Unit:
    def __init__(self, value):
        self.value = float(value)

    def get_value(self):
        return self.value

    def change_value(self, value):
        self.value = value

#Weight Classes
class Weight(Unit):
    KIND = "Weight"
    NAME = None
    SYMBOL = None

    def convert(self, output):
        try:
            kgs = self.value * conversiontables.tokg[self.NAME]
            return kgs * conversiontables.fromkg[output]
        except KeyError:
            return "Not a supported unit!"

class Kilograms(Weight):
    NAME = "Kilograms"
    SYMBOL = "kg"


class Pounds(Weight):
    NAME = "Pounds"
    SYMBOL = "lb"


class Stone(Weight):
    SYMBOL = "st"
    NAME = "Stone"


class Imperial_Ton(Weight):
    SYMBOL = "ton"
    NAME = "Imperial Tons"


class US_Ton(Weight):
    SYMBOL = "US ton"
    NAME = "US Tons"



class Ounce(Weight):
    SYMBOL = "oz"
    NAME = "Ounces"

#Length Classes
class Length(Unit):
    KIND = "Length"
    NAME = None
    SYMBOL = None

    def convert(self, output):
        try:
            metres = self.value * conversiontables.tom[self.NAME]
            return metres * conversiontables.fromm[output]
        except KeyError:
            return "Not a supported unit!"

class Metres(Length):
    SYMBOL = "m"
    NAME = "Metres"


class Foot(Length):
    SYMBOL = "ft"
    NAME = "Feet"


class Yard(Length):
    SYMBOL = "yd"
    NAME = "Yards"


class Furlong(Length):
    SYMBOL = "fur"
    NAME = "Furlong"


class Inch(Length):
    SYMBOL = "in"
    NAME = "Inches"


class Mile(Length):
    SYMBOL = "mi"
    NAME = "Miles"


class Kilometre(Length):
    SYMBOL = "km"
    NAME = "Kilometres"


#Velocity Classes
class Velocity(Unit):
    KIND = "Velocity"
    SYMBOL = None
    NAME = None

    def convert(self, output):
        try:
            metres = self.value * conversiontables.to_m_per_s[self.NAME]
            return metres * conversiontables.from_m_per_s[output]
        except KeyError:
            return "Not a supported unit!"

class Metres_Per_Second(Velocity):
    SYMBOL = "m/s"
    NAME = "Metres per Second"


class Miles_Per_Hour(Velocity):
    SYMBOL = "mph"
    NAME = "Miles per Hour"


class Kilometres_Per_Hour(Velocity):
    SYMBOL = "kmph"
    NAME = "Kilometres per Hour"


class Feet_Per_Second(Velocity):
    SYMBOL = "fps"
    NAME = "Feet per Second"



stringtoclass = {"Miles per Hour":Miles_Per_Hour,
                 "Kilometres per Hour":Kilometres_Per_Hour,
                 "Metres per Second":Metres_Per_Second,
                 "Feet per Second":Feet_Per_Second,
                 "Feet":Foot,
                 "Inches":Inch,
                 "Metres":Metres,
                 "Yards":Yard,
                 "Furlong":Furlong,
                 "Miles":Mile,
                 "Kilometres":Kilometre,
                 "Pounds":Pounds,
                 "Kilograms":Kilograms,
                 "Ounces":Ounce,
                 "Stone":Stone,
                 "Imperial Tons":Imperial_Ton,
                 "US Tons":US_Ton}
# mass = Pounds(25)
# velocity = Metres_Per_Second(25)
# length = Furlong(25)
#
# print(mass.convert("ounces"))
# print(velocity.convert("feet per second"))
# print(length.convert("inch"))

