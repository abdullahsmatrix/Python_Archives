# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  test.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 18:43:45 by amamun          #+#    #+#               #
#  Updated: 2026/03/25 18:45:10 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from card_generator import CardGenerator

generator = CardGenerator()

print (generator.get_all_creatures())