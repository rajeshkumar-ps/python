# Python Learning Tutorial - Complete Guide

Welcome to this comprehensive Python learning repository! This tutorial is designed to take you from Python basics to more advanced concepts through hands-on examples and clear explanations.

## 📚 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Getting Started](#getting-started)
3. [Learning Path](#learning-path)
   - [Introduction to Python Data Types](#1-introduction-to-python-data-types)
   - [Fundamentals: Control Flow](#2-fundamentals-control-flow)
   - [Functions](#3-functions)
   - [Classes and Object-Oriented Programming](#4-classes-and-object-oriented-programming)
   - [Inheritance](#5-inheritance)
   - [Error Handling](#6-error-handling)
   - [File Operations](#7-file-operations)
   - [Mutability in Python](#8-mutability-in-python)
   - [Default Values](#9-default-values)
   - [Modules and Imports](#10-modules-and-imports)
   - [Project Milestones](#11-project-milestones)
4. [How to Use This Repository](#how-to-use-this-repository)
5. [Best Practices](#best-practices)

---

## Prerequisites

- **Python 3.6+** installed on your system
- On macOS/Linux, use `python3` command
- A text editor or IDE (VS Code, PyCharm, etc.)
- Basic understanding of programming concepts (helpful but not required)

### Verify Your Installation

```bash
python3 --version
# Should output: Python 3.x.x
```

---

## Getting Started

1. **Clone or navigate to this repository**
   ```bash
   cd /path/to/python
   ```

2. **Run your first Python script**
   ```bash
   python3 Intro/string.py
   ```

3. **Follow the learning path** below, starting with the Introduction section

---

## Learning Path

### 1. Introduction to Python Data Types

**Location:** `Intro/`

Start here! These examples introduce Python's fundamental data types and basic operations.

#### Topics Covered:

- **Numbers** (`numbers_in_python.py`)
  - Integer and floating-point numbers
  - Mathematical operations
  - Floor division (`//`) vs regular division (`/`)
  - Constants and variables

- **Strings** (`string.py`)
  - String creation and manipulation
  - f-string formatting (modern Python string interpolation)
  - Iterating over mixed-type collections
  ```python
  name = 'Rajesh'
  print(f"Hello {name}!")
  ```

- **Lists** (`list.py`)
  - Creating and modifying lists
  - Adding/removing elements (`append()`, `remove()`)
  - List concatenation
  - Converting lists to strings with `join()`

- **Dictionaries** (`dict.py`)
  - Key-value pairs
  - Adding and accessing dictionary elements
  - Dictionary as a data structure for structured information

- **Sets** (`sets.py`)
  - Unordered collections of unique elements
  - Set operations: `union()`, `intersection()`, `difference()`
  - Comparing sets

- **Tuples** (`tupples.py`)
  - Immutable sequences
  - Tuple creation and indexing
  - When to use tuples vs lists

**Run examples:**
```bash
python3 Intro/string.py
python3 Intro/list.py
python3 Intro/dict.py
python3 Intro/sets.py
python3 Intro/tupples.py
python3 Intro/numbers_in_python.py
```

---

### 2. Fundamentals: Control Flow

**Location:** `fundamentals/`

Learn how to control the flow of your program with conditionals and loops.

#### Topics Covered:

- **Conditional Statements** (`if.py`)
  - `if`, `elif`, `else` statements
  - Truthiness in Python (how Python evaluates conditions)
  - Comparison operators (`<`, `>`, `==`, `!=`)

- **While Loops** (`while.py`)
  - Iterating with `while` loops
  - Loop control and termination conditions
  - Avoiding infinite loops

- **Enumerate** (`enumurate.py`)
  - Using `enumerate()` to get both index and value
  - Iterating with indices efficiently

- **Comprehensions** (`comp.py`)
  - List comprehensions (concise list creation)
  - Dictionary comprehensions
  - Generator expressions

**Run examples:**
```bash
python3 fundamentals/if.py
python3 fundamentals/while.py
python3 fundamentals/enumurate.py
python3 fundamentals/comp.py
```

---

### 3. Functions

**Location:** `fn/`

Functions are reusable blocks of code that perform specific tasks.

#### Key Concepts:

- **Function Definition**
  ```python
  def greet():
      print("Hello, World!")
  ```

- **Function Assignment**
  - Functions are first-class objects in Python
  - You can assign functions to variables
  ```python
  test = greet
  print(test)  # Shows function object
  ```

- **Parameters and Arguments**
  - Passing data to functions
  - Return values

**Run example:**
```bash
python3 fn/app.py
```

---

### 4. Classes and Object-Oriented Programming

**Location:** `class/`

Learn object-oriented programming (OOP) with Python classes.

#### Key Concepts:

- **Class Definition**
  ```python
  class Student:
      def __init__(self, name, age):
          self.name = name
          self.age = age
  ```

- **Instance Methods**
  - Methods that operate on class instances
  - The `self` parameter

- **`__init__` Constructor**
  - Initializing object attributes
  - Setting up object state

- **`__name__` Variable**
  - Understanding module execution context
  - `if __name__ == "__main__":` pattern

**Run example:**
```bash
python3 class/app.py
```

---

### 5. Inheritance

**Location:** `inheritence/`

Inheritance allows you to create new classes based on existing ones.

#### Key Concepts:

- **Parent and Child Classes**
  ```python
  class Student:
      # Parent class
      pass
  
  class WorkingStudent(Student):
      # Child class inherits from Student
      pass
  ```

- **`super()` Function**
  - Calling parent class methods
  - Initializing parent class attributes

- **Decorators**
  - `@property`: Convert methods to properties
  - `@classmethod`: Methods that work with the class itself
  - `@staticmethod`: Methods that don't need class or instance

**Example:**
```python
@property
def weekly_salary(self):
    return self.salary * 40
```

**Run example:**
```bash
python3 inheritence/app.py
```

---

### 6. Error Handling

**Location:** `error/`

Learn how to handle and create custom errors in Python.

#### Common Python Errors:

- **IndexError**: Accessing list/string index that doesn't exist
- **KeyError**: Accessing dictionary key that doesn't exist
- **NameError**: Using undefined variables
- **TypeError**: Operations on incompatible types
- **ValueError**: Wrong value type for operation

#### Custom Errors:

- Creating your own exception classes
- Inheriting from built-in exceptions
- Adding custom error messages and codes

**Example:**
```python
class MyCustomError(TypeError):
    def __init__(self, message, code):
        super().__init__(f'Error Message: {message} | Error Code: {code}')
```

**Run example:**
```bash
python3 error/app.py
```

---

### 7. File Operations

**Location:** `files/`

Learn how to read from and write to files in Python.

#### Topics Covered:

- **Opening Files**
  - `open()` function
  - File modes: `'r'` (read), `'w'` (write), `'a'` (append)

- **Reading Files**
  - `read()` method
  - Reading entire file content
  - File cursor positioning

- **Writing Files**
  - `write()` method
  - Overwriting vs appending

- **File Context Managers** (Best Practice)
  ```python
  with open('file.txt', 'r') as file:
      content = file.read()
  # File automatically closes
  ```

- **CSV Files** (`csv_read.py`)
  - Reading CSV data
  - Parsing structured data

- **JSON Files** (`json_file.py`)
  - Working with JSON format
  - Serialization and deserialization

**Run examples:**
```bash
python3 files/app.py
python3 files/csv_read.py
python3 files/json_file.py
```

---

### 8. Mutability in Python

**Location:** `mutability/`

Understanding which objects can be modified in-place and which create new objects.

#### Key Concepts:

- **Mutable Objects** (can be changed in-place)
  - Lists: `[1, 2, 3]`
  - Dictionaries: `{'key': 'value'}`
  - Sets: `{1, 2, 3}`
  - Same `id()` before and after modification

- **Immutable Objects** (create new objects when "modified")
  - Tuples: `(1, 2, 3)`
  - Strings: `"hello"`
  - Integers, floats
  - Different `id()` after operation

**Understanding `id()`:**
- `id()` returns the memory address of an object
- Same `id` = same object (mutable)
- Different `id` = new object (immutable)

**Run example:**
```bash
python3 mutability/app.py
```

---

### 9. Default Values

**Location:** `deafult_value/`

Learn about default parameter values in functions.

#### Key Concepts:

- **Default Arguments**
  ```python
  def greet(name="Guest"):
      print(f"Hello, {name}!")
  ```

- **When to Use Defaults**
  - Making parameters optional
  - Providing sensible defaults
  - Avoiding repetitive code

**Run example:**
```bash
python3 deafult_value/app.py
```

---

### 10. Modules and Imports

**Location:** `import_project/`

Learn how to organize code into modules and import them.

#### Key Concepts:

- **Creating Modules**
  - Organizing code into separate files
  - The `utils/` directory structure

- **Importing Modules**
  ```python
  from utils.file_operation import some_function
  import utils.file_operation
  ```

- **Package Structure**
  - `__init__.py` files
  - Organizing related modules

**Run example:**
```bash
python3 import_project/app.py
```

---

### 11. Project Milestones

**Location:** `milestone_1/`, `milestone_2/`

These folders contain more complex projects that combine multiple concepts.

- **Milestone 1** (`milestone_1/`)
  - Basic project structure
  - Combining learned concepts

- **Milestone 2** (`milestone_2/`)
  - Advanced project structure
  - Using utilities and modules
  - Database operations (`utils/database.py`)

**Run examples:**
```bash
python3 milestone_1/app.py
python3 milestone_2/app.py
```

---

## How to Use This Repository

### Recommended Learning Order

1. **Start with Basics** → `Intro/` folder
2. **Control Flow** → `fundamentals/` folder
3. **Functions** → `fn/` folder
4. **OOP Basics** → `class/` folder
5. **Advanced OOP** → `inheritence/` folder
6. **Error Handling** → `error/` folder
7. **File Operations** → `files/` folder
8. **Advanced Topics** → `mutability/`, `deafult_value/`, `import_project/`
9. **Projects** → `milestone_1/`, `milestone_2/`

### Running Examples

Each folder contains example scripts. Run them individually:

```bash
# Run a specific example
python3 Intro/string.py

# Or navigate to the folder first
cd Intro
python3 string.py
```

### Experimenting

**Don't just run the code—experiment with it!**

1. **Modify values** and see what happens
2. **Add print statements** to understand flow
3. **Break things intentionally** to learn from errors
4. **Combine concepts** from different examples

### Tips for Learning

- **Read the code** before running it
- **Predict the output** before executing
- **Modify examples** to test your understanding
- **Create your own variations** of the examples
- **Use Python's interactive shell** (`python3` or `ipython`) for quick tests

---

## Best Practices

### Code Organization

- Keep related code in the same module
- Use meaningful variable and function names
- Add comments to explain complex logic
- Use docstrings for functions and classes

### File Handling

- Always close files (or use `with` statements)
- Handle file errors gracefully
- Use appropriate file modes

### Error Handling

- Anticipate potential errors
- Use try-except blocks for error handling
- Provide meaningful error messages
- Create custom exceptions when appropriate

### Object-Oriented Programming

- Use classes to model real-world entities
- Keep classes focused (single responsibility)
- Use inheritance to avoid code duplication
- Leverage properties and decorators appropriately

---

## Common Python Commands

```bash
# Check Python version
python3 --version

# Run a Python script
python3 path/to/script.py

# Enter Python interactive shell
python3

# Install packages (if needed)
pip3 install package_name

# Run Python with verbose output
python3 -v script.py
```

---

## Troubleshooting

### "command not found: python"

On macOS/Linux, use `python3` instead of `python`:
```bash
python3 script.py
```

### Import Errors

Make sure you're running scripts from the correct directory:
```bash
# From repository root
python3 Intro/string.py

# Or navigate first
cd Intro
python3 string.py
```

### File Not Found Errors

Check that you're in the correct directory and file paths are relative to your current location.

---

## Next Steps

After completing this tutorial:

1. **Build Your Own Projects**
   - Start with small scripts
   - Gradually increase complexity
   - Apply concepts from multiple topics

2. **Explore Python Libraries**
   - `requests` for HTTP requests
   - `pandas` for data analysis
   - `flask` or `django` for web development
   - `numpy` for numerical computing

3. **Practice on Coding Platforms**
   - LeetCode
   - HackerRank
   - Codewars
   - Project Euler

4. **Read Python Documentation**
   - [Official Python Docs](https://docs.python.org/3/)
   - [Python Tutorial](https://docs.python.org/3/tutorial/)

5. **Join Python Communities**
   - r/learnpython on Reddit
   - Python Discord servers
   - Local Python meetups

---

## Repository Structure

```
python/
├── Intro/              # Basic data types
├── fundamentals/       # Control flow and loops
├── fn/                # Functions
├── class/             # Classes and OOP
├── inheritence/       # Inheritance
├── error/             # Error handling
├── files/             # File operations
├── mutability/        # Mutable vs immutable
├── deafult_value/     # Default parameters
├── import_project/    # Modules and imports
├── milestone_1/       # First project
├── milestone_2/       # Second project
└── README.md          # This file
```

---

## Contributing

This is a learning repository. Feel free to:
- Add more examples
- Improve existing code
- Fix typos or errors
- Add comments and documentation

---

## License

This repository is for educational purposes. Feel free to use and modify the code for learning.

---

## Contact & Support

If you have questions or need help:
- Review the code comments in each file
- Experiment with the examples
- Refer to Python documentation
- Search for specific error messages online

---

**Happy Learning! 🐍**

Remember: The best way to learn Python is by writing code. Don't just read—practice, experiment, and build!
