# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/28 16:35:18 by amamun          #+#    #+#               #
#  Updated: 2026/03/01 22:56:32 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


class FileOpenedError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    filename: str = "ancient_fragment.txt"
    try:
        with open(filename, "r") as file:
            print(f"Accessing Storage Vault: {file.name}")
            print("Connection established...")
            print("RECOVERED DATA:")
            for line in file:
                print(line, end="")
            print("\nData recovery complete.", end=" ")
        if file.closed:
            print("Storage unit disconnected")
        else:
            raise FileOpenedError("File not closed!")

    except FileNotFoundError:
        print(f"Accessing Storage Vault: {filename}")
        print("File does not exist")
    except FileOpenedError as err:
        print(err)


if __name__ == "__main__":
    main()
