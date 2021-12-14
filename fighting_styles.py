"""
Many classes in D&D inherits a sub-set of fighting styles 
from a greater list. 
"""

# fighting_styles = gf.fighting_styles

all_fighting_styles = ['Archery',
                        'Blessed Warrior',
                        'Blind Fighting',
                        'Close Quarters Shooter',
                        'Defense',
                        'Druidic Warrior',
                        'Dueling',
                        'Great Weapon Fighting',
                        'Interception',
                        'Protection', 
                        'Superior Technique',
                        'Thrown Weapon Fighting',
                        'Two-Weapon Fighting',
                        'Unarmed Fighting',
]

not_fighter_styles = ['Blessed Warrior', 'Druidic Warrior']

fighter_styles = [style for style in all_fighting_styles 
                        if style not in not_fighter_styles]

