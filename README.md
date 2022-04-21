# <p align="center">eval</p>

<p align="center">
  Mathematical expression calculator in Python.
</p>


## Usage
Read from a file:
```bash
$ cat text.txt
1**3+5
2**4**3
$ python -m eval -f text.txt
6.0
15625.0
```
Command-line input:
```bash
$ python -m eval 1 + 3**2 * 3
28.0
```
Interpreter:
```bash
$ python -m eval
```


## LICENSE
MIT
