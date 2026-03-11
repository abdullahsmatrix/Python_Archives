# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  stream_processor.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/03 16:13:08 by amamun          #+#    #+#               #
#  Updated: 2026/03/04 02:00:13 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, Union

from abc import ABC, abstractmethod


class InvalidLogEntry(Exception):
    def __init__(self, log_data: Any, message="Invalid log"):
        self.log_data = log_data
        self.message = f"{message}: '{log_data}'"
        super().__init__(self.message)


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return (f"{result}")


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if self.validate(data):
            total: Union[int, float] = sum(data)
            length: int = len(data)
            avg: float = total / length

            result_str = (f"Processed {length} numeric values, "
                          f"sum={total}, avg={avg:.2f}")
            return self.format_output(result_str)
        else:
            raise ValueError("ERROR Output: Contains invalid data type!")

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for i in data:
                if not isinstance(i, (int, float)):
                    return False
            return True
        return False


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        else:
            return False

    def process(self, data: Any) -> str:
        if self.validate(data):
            length: int = len(data)
            word_count: int = len(data.split(' '))
            result_str: str = (f"Processed text: {length} characters, "
                               f"{word_count} words")
            return self.format_output(result_str)
        else:
            raise ValueError("ERROR Output: Invalid data type. Not a string!")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            if data.startswith("ERROR: ") or data.startswith("INFO: "):
                return True
            return False
        return False

    def process(self, data: Any) -> str:
        if self.validate(data):
            data_splitted: list[str] = data.split(':', 1)
            log_type: str = data_splitted[0]
            log_msg: str = data_splitted[1].strip()
            if log_type == "ERROR":
                res: str = (f"[ALERT] {log_type} level detected: {log_msg}")
            else:
                res: str = (f"[INFO] {log_type} level detected: {log_msg}")
            return self.format_output(res)
        else:
            raise InvalidLogEntry(data)


def handle_num_process(data: list[int]) -> None:
    print("Initializing Numeric Processor...")
    print(f"Processing data: {data}")
    num_process = NumericProcessor()
    try:
        output: str = num_process.process(data)
        print("Validation: Numeric data verified")
        print(f"Output: {output}")
        print()
    except ValueError as Error:
        print(Error)
        print()


def handle_text_process(data: str) -> None:
    print("Initializing Text Processor...")
    print(f"Processing data: '{data}'")
    try:
        text_process = TextProcessor()
        output: str = text_process.process(data)
        print("Validation: Text data verified")
        print(f"Output: {output}")
        print()
    except ValueError as Error:
        print(Error)
        print()


def handle_log_process(data: str) -> None:
    print("Initializing Log Processor...")
    print(f"Processing data: '{data}'")
    try:
        log_process = LogProcessor()
        output: str = log_process.process(data)
        print("Validation: Log entry verified")
        print(f"Output: {output}")
        print()
    except InvalidLogEntry as Error:
        print(Error)
        print()


def poly_process_demo() -> None:
    print("=== Polymorphic Processing Demo ===")
    result: int = 1
    data: list[Union[int, str]] = [[1, 2, 3, 4], "I Love 42",
                                   "INFO: System ready"]
    instances = [NumericProcessor(), TextProcessor(), LogProcessor()]
    for processor, input_data in zip(instances, data):
        print(f"Result {result}: {processor.process(input_data)}")
        result += 1


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    data: list[Union[int, str]] = [[1, 2, 3, 4, 5], "Hello Nexus World",
                                   "ERROR: Connection timeout"]

    handle_num_process(data[0])
    handle_text_process(data[1])
    handle_log_process(data[2])
    poly_process_demo()
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
