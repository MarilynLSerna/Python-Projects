# Parent class representing a generic zodiac sign
class ZodiacSign:
    def __init__(self, name, element):
        self.name = name  # Name of the zodiac sign
        self.element = element  # Element associated with that zodiac sign

    def display_info(self):
        # Basic information about the zodiac sign
        print("Zodiac Name: {}".format(self.name))
        print("Element: {}".format(self.element))

# Child class using western zodiac sign
class WesternZodiac(ZodiacSign):
    def __init__(self, name, element, start_date, end_date):
        # Calling __init__ method of the parent class
        super().__init__(name, element)
        self.start_date = start_date
        self.end_date = end_date

    def display_info(self):
        # Overriding the display_info method to include western zodiac
        super().display_info()
        print("Period: {} to {}".format(self.start_date, self.end_date))

# Creating western zodiac sign for Cancer
western_zodiac = WesternZodiac("Cancer", "Water", "June 21", "July 22")
western_zodiac.display_info()

print() 

# Child class using chinese zodiac sign
class ChineseZodiac(ZodiacSign):
    def __init__(self, name, element, year, animal):
        super().__init__(name, element)
        self.year = year
        self.animal = animal
        
    def display_info(self):
        # Overriding the display_info method to include chinese zodiac
        super().display_info()
        print("Year: {}".format(self.year))
        print("Animal: {}".format(self.animal))

# Creating chinese zodiac sign for the year 1996
chinese_zodiac = ChineseZodiac("Rat", "Water", 1996, "Rat")
chinese_zodiac.display_info()


        
