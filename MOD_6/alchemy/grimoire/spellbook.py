# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  spellbook.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/17 21:01:26 by amamun          #+#    #+#               #
#  Updated: 2026/03/17 22:19:42 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    validation_result: str = validate_ingredients(ingredients)
    if "INVALID" in validation_result:
        return f"Spell rejected: {spell_name} ({validation_result})"
    return f"Spell recorded: {spell_name} ({validation_result})"
