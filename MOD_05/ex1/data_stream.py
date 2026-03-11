# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_stream.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: amamun <amamun@student.42warsaw.pl>       +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/10 20:26:07 by amamun          #+#    #+#               #
#  Updated: 2026/03/11 20:17:08 by amamun          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import List, Any, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type: str = stream_type
        self.processed_count: int = 0
        self.failed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_batch(self,data_batch: List[Any], 
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch

        filtered_batch: List[Any] = []
        for item in data_batch:
            if criteria.lower() in str(item).lower():
                filtered_batch.append(item)
        return filtered_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "processed": self.processed_count,
            "failed": self.failed_count
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        accepted_data: List[str] = []
        temps: List[Union[int, float]] = []
        for item in data_batch:
            for k, v in item.items():
                if (
                    k not in ["temp", "humidity", "pressure"]
                    or not isinstance(v, (int, float))
                ):
                    self.failed_count += 1
                    raise TypeError("Invalid sensor data type!"
                                    "Not an environmental data!")
                else:
                    accepted_data.append(f"{k}:{v}")
                    if k == "temp":
                        temps.append(v)
        analysis: str = (
            f"Sensor analysis: {len(accepted_data)} readings processed, "
            f"avg temp: {sum(temps) / len(temps)}{chr(176)}C"
        )
        self.processed_count = len(accepted_data)
        return analysis


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        accepted_data: List[str] = []
        bought: List[Union[int, float]] = []
        sold: List[Union[int, float]] = []
        for item in data_batch:
            for k, v in item.items():
                if k not in ["buy", "sell"] or not isinstance(v, (int, float)):
                    self.failed_count += 1
                    raise TypeError("Invalid data type!"
                                    "Not a Financial Data!")
                else:
                    accepted_data.append(f"{k}:{v}")
                    if k == "buy":
                        bought.append(v)
                    elif k == "sell":
                        sold.append(v)
        self.processed_count = len(accepted_data)
        analysis: str = (
            f"Transaction analysis: {self.processed_count} "
            f"operations, net flow: {sum(bought) - sum(sold)} units"
        )
        return analysis


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        accepted_data: List[str] = []
        errors: int = 0
        for item in data_batch:
            if item not in ["login", "logout", "error"]:
                self.failed_count += 1
                raise TypeError("Invalid data type! Not a system event")
            else:
                if item == "error":
                    errors += 1
                accepted_data.append(item)
        self.processed_count = len(accepted_data)
        analysis: str = (
            f"Event analysis: {self.processed_count} "
            f"events, {errors} error detected"
        )
        return analysis


class StreamProcessor:
    def __init__(self, data_batch: List[Any]) -> None:
        self.stream_list: List[DataStream] = []
        self.data_batch = data_batch

    def add_stream(self, stream: DataStream) -> None:
        self.stream_list.append(stream)

    def process_streams(self):
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")
        stat: dict = {}
        for stream in self.stream_list:
            try:
                if isinstance(stream, SensorStream):
                    filtered = [
                        d for d in self.data_batch
                        if isinstance(d, dict)
                        and any(
                            k in ["temp", "humidity", "pressure"]
                            for k in d
                        )
                    ]
                elif isinstance(stream, TransactionStream):
                    filtered = [
                        d for d in self.data_batch
                        if isinstance(d, dict)
                        and any(k in ["buy", "sell"] for k in d)
                    ]
                elif isinstance(stream, EventStream):
                    filtered = [
                        d for d in self.data_batch if isinstance(d, str)
                    ]
                else:
                    filtered = []

                stream.process_batch(filtered)
                stat = stream.get_stats()

                if isinstance(stream, SensorStream):
                    print(
                        f"Sensor Data: {stat['processed']} readings processed"
                    )
                elif isinstance(stream, TransactionStream):
                    print(
                        f"Transaction Data: {stat['processed']} "
                        "operations processed"
                    )
                else:
                    print(
                        f"Event Data: {stat['processed']} events processed"
                    )

            except Exception as e:
                print(f"Error processing stream {stream.stream_id}: {e}")


def main():
    # ========== DATABASE ==========
    sensor_data = [{"temp": 12}, {"humidity": 56}, {"pressure": 1010}]
    event_data = ["login", "logout", "error", "login"]
    fin_data = [{"buy": 120}, {"sell": 40}, {"buy": 90}]

    # ======== Mixed Database ========
    data_batch: List[Any] = [
        {"temp": 29},
        "login",
        {"buy": 120},
        "error",
        {"humidity": 61},
        {"sell": 40},
        "logout",
        {"pressure": 1009}
    ]

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(
        "Processing sensor batch: "
        f"{', '.join(str(item) for item in sensor_data)}"
    )
    print(sensor.process_batch(sensor_data))
    print()

    print("Initializing Transaction Stream...")
    print(
        "Processing transaction batch: "
        f"{', '.join(str(item) for item in fin_data)}"
    )
    trans = TransactionStream("TRANS_001")
    print(trans.process_batch(fin_data))
    print()

    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Processing event batch: {event_data}")
    print(event.process_batch(event_data))
    print()

    processor = StreamProcessor(data_batch)
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)
    processor.process_streams()

    print("\nStream filtering active: High-priority data only")
    sensor_entries: List[Any] = sensor.filter_batch(data_batch, "temp")
    critical_sensor_entries: List[Any] = [
        d for d in sensor_entries
        if isinstance(d, dict) and d.get("temp", 0) >= 28
    ]
    transaction_entries: List[Any] = trans.filter_batch(data_batch, "buy")
    large_transactions: List[Any] = [
        d for d in transaction_entries
        if isinstance(d, dict) and d.get("buy", 0) >= 100
    ]
    print(f"Filtered results: {len(critical_sensor_entries)} critical sensor "
          f"alerts, {len(large_transactions)} large transaction")


if __name__ == "__main__":
    main()
