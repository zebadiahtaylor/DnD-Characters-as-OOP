"""
Characters class, for dnd_dpr_calc

Inherits from the base Character Class. 

D&D's 'Subclasses' (e.g., Eldritch Knight, Battle Master, etc.) are represented here as Pythonic subclasses as well, which inherit the base characteristics, attributes and methods of the Fighter class
"""

from math import floor

from .features import fighting_styles
from .base_class import Character

fighter_styles = fighting_styles.fighter_styles


class Fighter(Character):
    """
    This subclass represents a DnD 5e "class": 
    https://www.dndbeyond.com/classes/fighter
    """

    def __init__(self, level=False):
        """
        Handles bonuses all fighter classes receive, 
        regardless of subclass. 
        """
        Character.__init__(self)
        if level:
            self.fighter_class = level
            self.total_levels += level
        self.name = ["fighter"]
        self.class_names_and_level["fighter"] = level
        self.second_wind_uses = 1 # Per short rest
        self.action_surge_uses = 0 # Per short rest
        self.indomitable_uses = 0 # Per long rest


    def level_up_class(self, level=0):
        """
        Automatically called in self.level_up()
        See superclass, Character, for implementation.
        """
        self.fighter_class = level
        if self.fighter_class >= 1 and not self.fighting_styles:
            self.update_player_choices("Choose a fighting style",
                                "fighting_styles",
                                self.get_available_fighting_styles)
        if self.fighter_class >= 2:
            self.action_surge_uses = 1
        if self.fighter_class >= 5:
            self.attack_num = 2
        if self.fighter_class >= 9:
            self.indomitable_uses = 1
        if self.fighter_class >= 11:
            self.attack_num = 3
        if self.fighter_class >= 13:
            self.indomitable_uses = 2
        if self.fighter_class >= 17:
            self.action_surge_uses = 2
            self.indomitable_uses = 3
        if self.fighter_class >= 20:
            self.attack_num = 4


    def get_available_fighting_styles(self):
        available_styles = []
        available_styles.append([style for style in fighter_styles 
                            if style not in self.fighting_styles]) 
        return available_styles


class Champion(Fighter, Character):
    """
    This subclass of a subclass and superclass (Fighter, Chamption) represents a D&D 'Fighter Subclass'
    https://www.dndbeyond.com/classes/fighter#Champion
    """

    def __init__(self, level=False):
        if level:
            self.fighter_level = level       
            # Character.__init__(self) # Should init when Fighter inits.
            Fighter.__init__(self)
            self.level_up(self)


    def level_up_subclass(self, level=3):
        """
        Handles perks that require user choices. 
        """
        self.fighter_level = level
        if self.fighter_level >= 3:
            self.critical_range = [19,20]
        if self.fighter_level >= 10 and fighting_styles < 2:
            self.benefits_dict["All Done"] = False
            self.benefits_dict["Message"] = "Choose a second Fighting Style"
            self.benefits_dict["Available Styles"] = self.get_available_fighting_styles
        if self.fighter_level >= 15:
            self.critical_range = [18, 19, 20]



class Battle_Master(Fighter, Character):
    """
    https://www.dndbeyond.com/classes/fighter#BattleMaster
    Not Implemented
    """
    maneuvers = []

    def __init__(self, fighter_level, fighting_style):
        super().__init__(fighter_level, fighting_style)


    
# Ozzie = Champion(15, 'defense')
# print(f"Ozzie's proficiency bonus = {Ozzie.proficiency_bonus()}")
# print(f"Ozzie can attack {Ozzie.attack_num} times.")
# print(f"Ozzies critical range is {Ozzie.critical_range}+")
# print(Ozzie.fighting_styles)
# print(Ozzie.level_up())

Ozzie = Champion(level=5)
# print(Ozzie.total_levels)
# print(Ozzie.apply_player_choices({'total_levels':4}))
# print(Ozzie.total_levels)
# print(Ozzie.return_class_or_subclass(Champion))
