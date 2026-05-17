# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_pathway_debate.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/17 20:36:26 by amamun          #+#    #+#               #
#  Updated: 2026/03/17 23:17:34 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life


def main() -> None:
    print("=== Pathway Debate Mastery ===")
    print()

    print("Testing Absolute Imports (from basic.py)")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")
    print()
    print("Testing Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")
    print()
    print("Testing Package Access:")
    result1 = lead_to_gold()
    print(f"alchemy.transmutation.lead_to_gold(): {result1}")
    result2 = philosophers_stone()
    print(f"alchemy.transmutation.philosophers_stone(): {result2}")


if __name__ == "__main__":
    main()
