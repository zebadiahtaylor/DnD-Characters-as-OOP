"""
Forms the basis for all character classes in D & D

In Pythonic terms, this is a "Super Class" from which all other classes (e.g., 'Fighter', 'Wizard', or 'Battle Master') will inherit common characteristics, called attributes and methods.

This class is 'inherited' by the Fighter class in the fighter.py file.
"""
from math import floor


"""
but will return_class_or_subclass(arg)???
remember to add .name attributes to each subclass and sub subclass
fix player_has_chosen 
"""


class Character():
    """
    Basic template for all D&D character classes.
    Methods that very from subclass to subclass are marked.
    The only change in functionality from subclass to subclass
    are in 
    """

    def __init__(self, strength=10, dexterity=10): 
        self.total_levels = 0
        self.class_names_and_level = {} # uhhh, double check judgment
        self.attack_num = 1
        self.fighting_styles = []
        self.critical_range = 20
        self.proficiency_bonus = 2
        self.player_choices = {"choices": False, 
                            "message": [],
                            }
        self.strength = strength
        self.dexterity = dexterity
        self.combat_bonuses = {
                "bonus_name": {
                    "damage_die": 8,
                    "damage_bonus": 0,
                    "uses_per_encounter": 0, # False for attacks
                    "action_type": ["main", 
                                "bonus", 
                                "reaction",],
                    "limit_per_round": 1 # Sometimes = to # of attacks
                }}

    def __repr__(self) -> str:
        self.__iter__(self)


    def level_up(self, class_level=False, subclass_level=False):
        """
        Updates object to reflect all level_related attributes. 
        """
        self.level_up_class(class_level)
        self.level_up_subclass(subclass_level)
        self.proficiency_bonus = self.return_proficiency_bonus()


    def return_proficiency_bonus(self):
        """
        Returns Proficiency Bonus.
        This starts at 2 and increments by 1 every 4 levels. 
        Auto-called in level_up_general_character().
        """
        if self.total_levels % 4 == 0:
            proficiency_bonus = int(self.total_levels/4 + 1)
        else:
            proficiency_bonus = floor(self.total_levels/4) + 2
        return proficiency_bonus


    def level_up_class():
        """
        Only implemented at the "class" subclassess (Fighter, Barbarian, etc.)
        """
        NotImplemented


    def level_up_subclass():
        """
        Only implemented at the "subclass" subclassess (Fighter, Barbarian, etc.)
        """
        NotImplemented


    def update_player_choices(self, message="", key=False, value=None):
        """
        Takes 2 strings, an object, a then updates player_choices. 
        player choices should look like {"option1":True, "option2":}
        Note that the key variable
        """
        if message and key and value: 
            self.player_choices["choices"] = True
            self.player_choices["message"].append(message)
            self.player_choices[key] = value


    def return_player_choices(self):
        """
        Returns a dict of choices for handling special character
        class behaviors where player choices are necessary.
        """
        self.update_player_choices()
        return self.player_choices


    def apply_player_choices(self, player_has_chosen = {}):
        """
        Takes users' choices as dict and updates object attributes. 
        dict should appear as {"attribute_name": "value_values_or_bool"}
        """
        for key, value in player_has_chosen.items():
            print(key, value)
            if key in vars(self).keys():
                vars(self)[key] = value

    @staticmethod
    def return_class_or_subclass(character_class):
        for primary_class in Character.__subclasses__():
            if primary_class.name == character_class:
                return primary_class()
            else:
                subclass = [subclass for subclass in primary_class.__subclasses__() if subclass.name == character_class]
                if subclass:
                    return subclass()
    
