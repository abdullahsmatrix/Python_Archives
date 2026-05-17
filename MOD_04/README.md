# File I/O & Data Management (MOD_04)

## 📋 Description

MOD_04 covers file operations and data management patterns. Learn file reading/writing, text processing, stream management, error recovery, and crisis response systems using Python's file I/O capabilities.

## ✨ Features

- **File Reading** - Text file operations and parsing
- **File Writing** - Data persistence and logging
- **Archive Creation** - Multi-file compression and storage
- **Stream Management** - Large file processing
- **Vault Security** - Access control and encryption basics
- **Crisis Response** - Error recovery and backup strategies
- **Text Processing** - Parsing and manipulation


## 💡 REVISION

### Read File with Error Handling

```python
filename = "data.txt"
try:
    with open(filename, "r") as file:
        print(f"Reading: {file.name}")
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: {filename} not found")
finally:
    print("File operation complete")
```

### Write to File

```python
data = ["Line 1", "Line 2", "Line 3"]
with open("output.txt", "w") as file:
    for line in data:
        file.write(line + "\n")
print("Data written successfully")
```

### Process Large Files

```python
def process_file_stream(filename):
    with open(filename, "r") as file:
        for line in file:
            # Process each line without loading entire file
            processed = line.strip().upper()
            print(processed)
```

### Work with Paths

```python
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

file_path = data_dir / "myfile.txt"
file_path.write_text("Hello, World!")
print(file_path.read_text())
```

## 📁 Folder Structure

```
MOD_04/
├── ex0/
│   └── ft_ancient_text.py       # Basic file reading
├── ex1/
│   └── ft_archive_creation.py   # Archive operations
├── ex2/
│   └── ft_stream_management.py  # Stream processing
├── ex3/
│   └── ft_vault_security.py     # Security patterns
├── ex4/
│   └── ft_crisis_response.py    # Backup/recovery
└── README.md
```

## 🚢 Deployment

### Production File Operations

```python
from pathlib import Path
import json

# Create backup
def backup_data(source_file):
    source = Path(source_file)
    backup = source.parent / f"{source.stem}_backup{source.suffix}"
    with open(source, "r") as src, open(backup, "w") as dst:
        dst.write(src.read())
    return backup

# Save JSON
def save_config(config_dict, filepath):
    with open(filepath, "w") as f:
        json.dump(config_dict, f, indent=2)
```

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| FileNotFoundError | Check file exists and path is correct |
| PermissionError | Check file permissions and directory access |
| File locked | Close file handles with context manager (`with`) |
| Encoding errors | Specify encoding: `open(file, encoding='utf-8')` |

**Key Learning Outcomes:**
- ✅ File reading and writing
- ✅ Context managers (with statement)
- ✅ Exception handling for I/O
- ✅ Path operations
- ✅ Stream processing
- ✅ Backup and recovery patterns
