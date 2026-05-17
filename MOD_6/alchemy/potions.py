# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  potions.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/17 16:38:07 by amamun          #+#    #+#               #
#  Updated: 2026/03/17 23:14:15 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from .elements import create_air, create_earth, create_fire, create_water


def healing_potion() -> str:
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    return (
        f"Invisibility potion brewed with {create_air()} "
        f"and {create_water()}"
    )


def wisdom_potion() -> str:
    return (
        "Wisdom potion brewed with all elements: "
        f"{create_air()}, {create_earth()}, {create_fire()}, {create_water()}"
    )
