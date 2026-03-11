# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/15 19:54:29 by amamun          #+#    #+#               #
#  Updated: 2026/02/18 22:47:02 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def check_temperature(temp_str: str) -> int:
    try:
        temperature: int = int(temp_str)
    except ValueError as exc:
        raise ValueError(
            f"Error: {temp_str} is not a valid number") from exc

    if temperature > 40:
        raise ValueError(
            f"Error: {temperature}{chr(176)}C is too hot for "
            f"plants(max 40{chr(176)}C)")
    if temperature < 0:
        raise ValueError(
            f"Error: {temperature}{chr(176)}C is too cold for plants "
            f"(min 0{chr(176)}C)")
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    test_values: list[str] = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"Testing temperature: {value}")
        try:
            temp: int = check_temperature(value)
            print(f"Temperature {temp}{chr(176)}C is perfect for plants!")
            print()
        except ValueError as error:
            print(error)
            print()
    print("All tests completed - peogram didn't crash!")


if __name__ == "__main__":
    test_temperature()
