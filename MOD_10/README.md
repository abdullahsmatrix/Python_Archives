# Functional Programming (MOD_10)

## 📋 Description

MOD_10 introduces functional programming paradigms in Python. Learn lambda functions, map/filter/reduce, higher-order functions, closures, decorators, and functools for elegant, functional-style code.

## ✨ Features

- **Lambda Functions** - Anonymous functions for simple operations
- **Map/Filter Functions** - Functional data transformation
- **Higher-Order Functions** - Functions that work with functions
- **Closures** - Functions capturing outer scope
- **Decorators** - Function/class modification without subclassing
- **functools** - Partial application, reduce, lru_cache
- **Scope & Closures** - Understanding Python's scope chain
- **Function Composition** - Chaining functional operations

## 🏗️ Architecture

```
Functional Paradigm
    ├── Lambda Functions
    ├── Map/Filter/Reduce
    ├── Higher-Order Functions
    ├── Closures & Scope
    ├── Decorators
    └── functools utilities
```

## 🛠️ Tech Stack

- **Python**: 3.10+
- **Functional Tools**: functools, operator, itertools
- **Standard Library**: lambda, map, filter

## 📦 Installation

```bash
cd MOD_10
python --version
```

## 🚀 Usage

### Run Each Exercise

```bash
python ex0/lambda_spells.py
python ex1/higher_magic.py
python ex2/scope_mysteries.py
python ex3/functools_artifacts.py
python ex4/decorator_mastery.py
```

## 💡 API Examples

### Lambda Functions

```python
# Simple lambda
add = lambda x, y: x + y
print(add(5, 3))  # 8

# Lambda with conditionals
max_value = lambda x, y: x if x > y else y
print(max_value(10, 7))  # 10

# Lambda for sorting
artifacts = [
    {'name': 'Sword', 'power': 5},
    {'name': 'Shield', 'power': 8}
]
sorted_artifacts = sorted(artifacts, key=lambda x: x['power'], reverse=True)
```

### Map/Filter/Reduce

```python
from functools import reduce

# Map - transform all elements
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Filter - select elements matching condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# Reduce - aggregate to single value
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120
```

### Higher-Order Functions

```python
def apply_twice(func, value):
    """Apply function twice to value"""
    return func(func(value))

def multiply_by_2(x):
    return x * 2

result = apply_twice(multiply_by_2, 5)
print(result)  # 20 (5 * 2 * 2)
```

### Closures & Scope

```python
def make_multiplier(factor):
    """Return a function that multiplies by factor"""
    def multiplier(x):
        return x * factor
    return multiplier

times_3 = make_multiplier(3)
print(times_3(5))  # 15

times_10 = make_multiplier(10)
print(times_10(5))  # 50
```

### Decorators

```python
def logger(func):
    """Decorator that logs function calls"""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(5, 3)
# Calling add
# Result: 8
```

### functools Utilities

```python
from functools import partial, lru_cache

# Partial application
multiply = lambda x, y: x * y
times_5 = partial(multiply, 5)
print(times_5(3))  # 15

# LRU Cache for expensive operations
@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Cached results for performance
```

## 📁 Folder Structure

```
MOD_10/
├── ex0/
│   └── lambda_spells.py      # Lambda functions, map/filter
├── ex1/
│   └── higher_magic.py       # Higher-order functions
├── ex2/
│   └── scope_mysteries.py    # Closures and scope
├── ex3/
│   └── functools_artifacts.py # functools utilities
├── ex4/
│   └── decorator_mastery.py  # Decorators
├── generator/
│   └── data_generator.py     # Test data generation
├── README.md
└── Readme.md
```

## 🧪 Testing

```bash
# Test lambda functions
python ex0/lambda_spells.py

# Test higher-order functions
python ex1/higher_magic.py

# Test decorators
python ex4/decorator_mastery.py
```

## 💡 Common Patterns

### Decorator for Timing

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Executed in {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
```

### Decorator for Error Handling

```python
def safe_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("Cannot divide by zero")
            return None
        return func(a, b)
    return wrapper

@safe_divide
def divide(a, b):
    return a / b
```

### Compose Functions

```python
def compose(f, g):
    """Compose two functions: compose(f, g)(x) == f(g(x))"""
    return lambda x: f(g(x))

add_one = lambda x: x + 1
multiply_by_2 = lambda x: x * 2

add_then_multiply = compose(multiply_by_2, add_one)
print(add_then_multiply(5))  # (5 + 1) * 2 = 12
```

## 🚢 Deployment

### Functional Data Processing Pipeline

```python
from functools import reduce

data = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]

# Pipeline: filter high scores -> extract names -> join
high_scores = filter(lambda x: x['score'] >= 80, data)
names = map(lambda x: x['name'], high_scores)
result = ', '.join(names)
print(result)  # Alice, Bob
```

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Lambda too complex | Use regular function instead |
| Closure not capturing value | Use default argument: `lambda x, y=y: x + y` |
| Decorator not working | Ensure `@wraps(func)` from functools used |
| Map/filter returns iterator | Convert to list: `list(map(...))` |
| Recursive limit exceeded | Use `sys.setrecursionlimit()` or optimize |

## 🤝 Contributing

1. Use lambdas only for simple operations
2. Prefer regular functions for complex logic
3. Use `@functools.wraps` in decorators
4. Document decorator behavior
5. Consider performance with large datasets
6. Add type hints for clarity

## 📄 License

Part of Python training archives (42 School)

---

**Key Learning Outcomes:**
- ✅ Lambda functions and anonymous functions
- ✅ Map, filter, and reduce operations
- ✅ Higher-order functions
- ✅ Closures and scope management
- ✅ Decorator design pattern
- ✅ functools utilities (partial, lru_cache, wraps)
- ✅ Functional composition
