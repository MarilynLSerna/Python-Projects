
# Parent Class Bungo Stray Dogs
class BungoStrayDogs:
    genre = "Action, Mystery"
    description = "A story about the Armed Detective Agency solving unusual cases."

    # Method describing the anime 
    def describe_anime(self):
        print("Genre: {}, Description: {}".format(self.genre, self.description))

    # Method describing the character
    def describe(self):
        print("Character: {}, Ability: {}".format(self.c_name, self.ability))

# Defining the first child class
class OsamuDazai(BungoStrayDogs):
    character_name = "Osamu Dazai"
    ability = "No Longer Human"
    affiliation = "Armed Detective Agency"
    weakness = "Suicidal tendencies"

    def describe(self):
        print("Character: {}, Ability: {}, Affiliation: {}, Weakness: {}".format(
            self.character_name, self.ability, self.affiliation, self.weakness))
        
# Defining the second child class
class ChuuyaNakahara(BungoStrayDogs):
    character_name = "Chuuya Nakahara"
    ability = "Upon the Tainted Sarrow"
    affiliation = "Port Mafia"
    weakness = "Utter hatred for Dazai"

    def describe(self):
        print("Character: {}, Ability: {}, Affiliation: {}, Weakness: {}".format(
            self.character_name, self.ability, self.affiliation, self.weakness))

# Instances for OsamuDazai and ChuuyaNakahara
dazai = OsamuDazai()
chuuya = ChuuyaNakahara()

# Polymorphism using print statements
dazai.describe_anime()
dazai.describe()
chuuya.describe_anime()
chuuya.describe()


        
    
    
    
