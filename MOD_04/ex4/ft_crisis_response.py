# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_crisis_response.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/01 22:41:50 by amamun          #+#    #+#               #
#  Updated: 2026/03/01 22:58:37 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def crisis_handler(filename: str, is_routine: bool = False) -> None:
    try:
        if is_routine:
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        with open(filename, "r") as file:
            content: str = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: Unexpected anomaly detected - {type(e).__name__}")
        print("STATUS: Crisis handled, investigating further")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    crisis_handler("lost_archive.txt")
    print()
    crisis_handler("classified_vault.txt")
    print()
    crisis_handler("standard_archive.txt", is_routine=True)
    print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
