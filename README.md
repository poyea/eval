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
$ ./main.py -f text.txt
6.0
15625.0
```
Command-line input:
```bash
$ ./main.py 1 + 3**2 * 3
28.0
```
Interpreter:
```bash
$ ./main.py
```

# Run tests
```bash
$ python -m unittest discover -s test -p '*_test.py'
```

## LICENSE
MIT
