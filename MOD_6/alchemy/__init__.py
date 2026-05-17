# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __init__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/16 23:33:01 by amamun          #+#    #+#               #
#  Updated: 2026/03/17 23:13:46 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# Version and author:
__version__ = "1.0.0"
__author__ = "Master Pythonicus"

# We declare exposed functions here
from .elements import create_fire, create_water

# Define the all variable:
__all__ = ["create_fire", "create_water"]
