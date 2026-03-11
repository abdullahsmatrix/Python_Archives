# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/01 21:35:57 by amamun          #+#    #+#               #
#  Updated: 2026/03/01 22:56:51 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    file1: str = "classified_data.txt"
    file2: str = "security_protocols.txt"
    print("Initiating secure vault access...\n")
    try:
        with open(file1, "r") as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            for line in file:
                print(line, end="")
            print("\n")

    except FileNotFoundError:
        print(f"File: {file1} not found!")
    try:
        with open(file2, "a") as file:
            file.write("\n[CLASSIFIED] New protocols added")
    except FileNotFoundError:
        print(f'File: {file2} not found!')

    try:
        with open(file2, "r") as file:
            print("SECURE PRESERVATION:")
            for line in file:
                print(line, end="")
            print()
            print("Vault automatically sealed upon completion")
            print()
    except FileNotFoundError:
        print(f'File: {file2} not found!')
    finally:
        print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
