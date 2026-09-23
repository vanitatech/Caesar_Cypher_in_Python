# Caesar_Cypher_in_Python
# Python Caesar Cipher

A command-line Caesar Cipher program built with Python. The program can **encrypt and decrypt messages** by shifting letters through the alphabet by a user-defined number of positions.

This project was created as part of my Python learning journey to practise **functions, loops, conditionals, lists, string manipulation, and modular arithmetic**.

## Features

* Encrypt messages using a Caesar Cipher
* Decrypt previously encrypted messages
* User-defined shift amount
* Preserves spaces and characters that are not in the alphabet
* Supports repeated encryption/decryption sessions
* Simple command-line interface
* ASCII-art logo using the `art` module

## How the Caesar Cipher Works

A Caesar Cipher shifts each letter in a message by a specified number of positions in the alphabet.

For example, with a shift of `3`:

```text
a → d
b → e
c → f
```

So:

```text
hello
```

becomes:

```text
khoor
```

To decrypt the message, the shift is reversed.

## Example

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
encode

Type your message:
hello world

Type the shift number:
3

Here is the encoded result: khoor zruog
```

The program can then decrypt the message by using the same shift amount.

## How It Works

The alphabet is stored in a Python list:

```python
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
```

For each letter in the message, the program finds its position in the alphabet and applies the shift:

```python
position = alphabet.index(letter)
new_position = (position + shift_amount) % 26
```

The `% 26` ensures that the position wraps around to the beginning of the alphabet when the shift goes beyond `z`.

For example:

```text
z + 1 → a
```

## Technologies Used

* Python 3
* `art` Python module

## What I Learned

Through this project, I practised:

* Defining and calling functions
* Function parameters
* `return` and variable assignment
* `for` loops
* `while` loops
* `if` / `else` statements
* Working with lists
* String manipulation
* Using `.index()` and `.lower()`
* User input with `input()`
* Converting input to integers using `int()`
* Modular arithmetic using `%`
* Importing and using a Python module
* Handling characters that are not part of a predefined list

## How to Run

Clone the repository and navigate to the project directory:

```bash
cd Python_Caesar_Cipher
```

Run the program:

```bash
python main.py
```

If the `art` module is not installed:

```bash
pip install art
```

## Future Improvements

Possible improvements include:

* Add support for uppercase letters
* Add validation for invalid shift numbers
* Handle invalid encode/decode choices
* Fix input handling for unexpected characters
* Add automated tests
* Improve error handling
* Separate the encryption/decryption logic from user interaction
* Add a graphical user interface
