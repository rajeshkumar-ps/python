Python Fundamentals — Intro Examples

This repository contains a small collection of short Python example scripts that demonstrate basic Python data types and operations. They are intended for beginners who want quick, runnable examples of lists, dictionaries, sets, strings, tuples, and numbers.

Prerequisites

- Python 3.6+ installed (on macOS use `python3`).

Quick start

1. Open a terminal in the repository root (this project assumes files live in the `Intro/` folder).
2. Run any example with:

```bash
python3 Intro/numbers_in_python.py
python3 Intro/list.py
python3 Intro/dict.py
```

Files and purpose

- `Intro/numbers_in_python.py` — shows numeric variables, constants, and integer division (floor division `//`).

  - Example: prints an integer `age`, the constant `PI`, and `20//3`.

- `Intro/list.py` — demonstrates Python lists: appending, removing, concatenation, and joining into a comma-separated string.

  - Example: `friends = ['rajesh','amrita']`, `friends.append('priti')`, `','.join(friends)`.

- `Intro/dict.py` — simple dictionary usage: create a dict, print it and add a new key-value pair.

  - Example: `friends_age = {"Rajesh": 30, "Amrita": 28}` then `friends_age['Priti'] = 25`.

- `Intro/sets.py` — demonstrates unordered sets, `add`, `difference`, `intersection`, `union`, and equality comparison of sets.

  - Example: `art_friends = {'rajesh','amrita','priti'}` and set operations comparing with `science_friends`.

- `Intro/string.py` — basic string formatting with f-strings and iterating a list containing mixed types.

  - Example: `name = 'Rajesh'` then `print(f"Hello {name}!")`.

- `Intro/tupples.py` — (tuple examples; file name has a small typo) shows tuple creation, immutability, concatenation to create a new tuple, and indexing.
  - Note: the filename is `tupples.py` (typo of "tuples").

Note about interpreter: On many macOS systems the system Python is `python3`. If `python` is not found, use `python3` or add an alias (`alias python=python3` in your `~/.zshrc`).

Next steps / suggestions

- Add brief comments or docstrings to each example to explain what each line does.
- Add a `Makefile` or small runner script to execute all examples (e.g., `./run_examples.sh`).
- Add unit tests or small assertions for some examples if you want to convert this to a learning exercise.

License

- This repository currently has no license file. Add a `LICENSE` if you intend to share the code publicly.

Contact / Help

- If you want the README expanded (more examples, screenshots, or a runner script), tell me which additions you want and I can add them.
