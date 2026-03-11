# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/28 22:08:53 by amamun          #+#    #+#               #
#  Updated: 2026/03/01 22:56:42 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import typing


def write_into_file(file: typing.TextIO) -> None:
    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    file.write("[ENTRY 003] Archived by Data Archivist trainee\n")


def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    filename: str = "new_dictionary.txt"
    try:
        with open(filename, "x+") as file:
            print(f"Initializing new storage unit: {filename}")
            print("Storage unit created successfully...\n")
            write_into_file(file)

        with open(filename, "r") as file:
            print(file.read())
        print('Data inscription complete. Storage unit sealed.')
        print("Archive 'new_dictionary.txt' ready for long-term preservation.")
    except FileExistsError:
        print(f"Storage: '{filename}' already exist")


if __name__ == "__main__":
    main()
