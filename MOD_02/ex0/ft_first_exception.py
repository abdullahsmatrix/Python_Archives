# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/15 19:54:29 by amamun          #+#    #+#               #
#  Updated: 2026/02/15 20:32:59 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_temperature(temp_str) -> int | str:
    try:
        temperature: int = int(temp_str)
    except ValueError:
        return (f"{temp_str} is not a valid number") 
    if temperature >= 0 and temperature <= 40:
        return temperature
    elif temperature > 40:
        return (f"Error: {temperature}\u2103 is too hot for plants "
              f"(max 40\u2103)")
    elif temperature < 0:
        return (f"Error: {temperature}\u2103 is too cold for plants "
              f"(min 0\u2103)")
        
        
    

check_temperature()