# Abstract Base Classes & Data Streams (MOD_05)

## 📋 Description

MOD_05 introduces abstract base classes (ABC) and design patterns for data processing. Learn polymorphism, interface design, and building extensible data processing pipelines.

## ✨ Features

- **Abstract Base Classes** - Define interfaces with ABC
- **Abstract Methods** - Enforce implementation in subclasses
- **Data Processors** - Pluggable processing components
- **Stream Processing** - Handle continuous data flows
- **Custom Exceptions** - Domain-specific error handling
- **Polymorphism** - Multiple implementations of shared interface
- **Pipeline Architecture** - Chain processing steps

## 🏗️ Architecture

```
Abstract Interface (ABC)
    ├── Data Processor (Abstract)
    │   ├── Processor A (Concrete)
    │   ├── Processor B (Concrete)
    │   └── Processor C (Concrete)
    ├── Logger (Abstract)
    │   ├── Console Logger
    │   └── File Logger
    └── Stream Handler
        └── Pipeline
```

## 💡 REVISION

### Define Abstract Base Class

```python
from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        """Process input data and return result"""
        pass
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate input data"""
        pass
```

### Implement Concrete Processor

```python
class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return f"[LOG] {data}"
    
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data) > 0

# Usage
processor = LogProcessor()
if processor.validate("test"):
    result = processor.process("test")
    print(result)  # [LOG] test
```

### Custom Exception

```python
class InvalidLogEntry(Exception):
    def __init__(self, log_data: Any, message="Invalid log"):
        self.log_data = log_data
        self.message = f"{message}: '{log_data}'"
        super().__init__(self.message)

try:
    raise InvalidLogEntry(None, "Null entry")
except InvalidLogEntry as e:
    print(e.message)
```

### Processing Pipeline

```python
class DataPipeline:
    def __init__(self):
        self.processors = []
    
    def add_processor(self, processor: DataProcessor):
        self.processors.append(processor)
    
    def execute(self, data: Any) -> str:
        result = data
        for processor in self.processors:
            if processor.validate(result):
                result = processor.process(result)
        return result

pipeline = DataPipeline()
pipeline.add_processor(LogProcessor())
pipeline.execute("input data")
```

## 📁 Folder Structure

```
MOD_05/
├── ex0/
│   └── stream_processor.py       # ABC and abstract methods
├── ex1/
│   └── data_stream.py            # Stream implementation
├── ex2/
│   └── nexus_pipeline.py         # Processing pipeline
└── README.md
```


## 🚢 Deployment

### Production Pipeline

```python
# Create processors
log_proc = LogProcessor()
json_proc = JSONProcessor()
db_proc = DatabaseProcessor()

# Build pipeline
pipeline = DataPipeline()
pipeline.add_processor(log_proc)
pipeline.add_processor(json_proc)
pipeline.add_processor(db_proc)

# Process data stream
for data_item in data_stream:
    pipeline.execute(data_item)
```

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Can't instantiate ABC | Implement all abstract methods in subclass |
| TypeError on abstract method | Use `@abstractmethod` decorator |
| Method signature mismatch | Match parent class signature exactly |


**Key Learning Outcomes:**
- ✅ Abstract base classes (ABC)
- ✅ Abstract methods and interfaces
- ✅ Polymorphism and inheritance
- ✅ Custom exceptions
- ✅ Pipeline architecture
- ✅ Pluggable components
