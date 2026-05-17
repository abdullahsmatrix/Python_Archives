# Exception Handling (MOD_02)

## 📋 Description

MOD_02 covers exception handling fundamentals. Learn to catch errors, create custom exceptions, use finally blocks, and build robust error-handling patterns for production code.

## ✨ Features

- **Exception Catching** - Try/except blocks for error handling
- **Custom Exceptions** - Create domain-specific exceptions
- **Error Validation** - Input validation and error checking
- **Finally Blocks** - Cleanup code that always runs
- **Raising Errors** - Explicit error generation
- **Error Propagation** - Error handling patterns

## 🏗️ Architecture

```
Exception Handling Flow
    ├── Try Block (Code to test)
    ├── Except Block (Error handling)
    ├── Finally Block (Cleanup)
    └── Raise Statement (Error generation)
```

## 🛠️ Tech Stack

- **Python**: 3.10+
- **Standard Library**: Built-in exceptions


### Basic Exception Handling

```python
def check_temperature(temp_str: str) -> int:
    try:
        temperature = int(temp_str)
    except ValueError as exc:
        raise ValueError(f"Error: {temp_str} is not a valid number") from exc
    
    if temperature > 40:
        raise ValueError("Temperature too hot for plants (max 40°C)")
    if temperature < 0:
        raise ValueError("Temperature too cold for plants (min 0°C)")
    
    return temperature
```

### Custom Exception

```python
class PlantException(Exception):
    def __init__(self, plant_name: str, message: str):
        self.plant_name = plant_name
        self.message = f"Plant '{plant_name}': {message}"
        super().__init__(self.message)

try:
    raise PlantException("Rose", "Insufficient water")
except PlantException as e:
    print(e.message)
```

### Finally Block

```python
try:
    # Risky operation
    result = 10 / int(user_input)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Cleanup completed")  # Always runs
```

## 📁 Folder Structure

```
MOD_02/
├── ex0/
│   └── ft_first_exception.py     # Basic try/except
├── ex1/
│   └── ft_different_errors.py    # Multiple exception types
├── ex2/
│   └── ft_custom_errors.py       # Custom exception classes
├── ex3/
│   └── ft_finally_block.py       # Finally block usage
├── ex4/
│   └── ft_raise_errors.py        # Raising exceptions
├── ex5/
│   └── ft_garden_management.py   # Complex exception patterns
└── README.md
```

**Key Learning Outcomes:**
- ✅ Try/except/finally patterns
- ✅ Multiple exception types
- ✅ Custom exceptions
- ✅ Error validation
- ✅ Exception propagation
