# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/22 16:40:58 by amamun          #+#    #+#               #
#  Updated: 2026/02/27 23:18:54 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def parse_scores() -> list[int]:
    if len(sys.argv) == 1:
        raise ValueError("No scores provided")
    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            raise ValueError(
                f"Invalid score: '{arg}'. Score can only be a number!"
            )
    return scores


def total_score(scores: list[int]) -> int:
    return sum(scores)


def average_score(scores: list[int]) -> float:
    return total_score(scores) / len(scores)


def score_analytics() -> None:
    try:
        scores = parse_scores()

        print("=== Player Score analytics ===")
        print(f"Score processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {total_score(scores)}")
        print(f"Average score: {average_score(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"score range: {max(scores) - min(scores)}")
    except ValueError as e:
        print("=== Player Score Analytics ===")
        print(
            f"{e}. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )


if __name__ == "__main__":
    score_analytics()
