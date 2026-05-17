# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  validator.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/17 20:56:11 by amamun          #+#    #+#               #
#  Updated: 2026/03/17 23:14:09 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def validate_ingredients(ingredients: str) -> str:
    valid_elements = ("fire", "air", "earth", "water")
    if any(element in ingredients for element in valid_elements):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
