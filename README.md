# MathREPL

MathREPL, a math expression evaluator using Python `eval()` and the `math` module.

MathREPL is an attempt to show how to use Python `eval()` to solve real-world problems while minimizing (but not removing) its security issues. So, the most important piece of code in this application is the function `evaluate()` which lives in the `evaluator` module.

MathREPL is a sample project based on the example I used in my [Real Python](https://realpython.com/) tutorial: [Python eval(): Evaluate Expressions Dynamically](https://realpython.com/python-eval-function/).

![Real Python Tutorial](real-python-image.jpeg)

## Installation

1. Clone the repo (`git clone https://github.com/lpozo/mathrepl.git`)
2. `cd` into the directory of the repo (`cd mathrepl`)
3. Run the main script (`python3 main.py`)

## Usage example

The steps in the previous section will preset you with a prompt like this:

```sh
MathREPL 1.0, your Python math expressions evaluator!
Enter a valid math expression after the prompt "mr>>".
Type "help" for more information.
Type "quit" or "exit" to exit.

mr>>
```

At `mr>>` type any math expression that follows Python syntax and uses the functionalities defined in the Python `math` module. For example:

```sh
mr>> (5 + 7) / 2
6.0
mr>> sqrt(pow(10, 2) + pow(15, 2))
18.027756377319946
mr>>
```

## Release History

- **Version 1.0**
  - Include basic functionalities to evaluate math-related expressions with Python `eval()` function and the `math` module.

## Contributing

1. Fork MathREPL from (<https://github.com/lpozo/mathrepl/fork>)
2. Clone your fork locally (`git clone https://github.com/your_user_name/mathrepl.git`)
3. Create your feature branch (`git checkout -b feature_awesome_feature`)
4. Commit your changes (`git commit -am 'Add some awesome feature'`)
5. Push to the branch (`git push -u origin feature_awesome_feature`)
6. Create a new Pull Request against the `develop` branch of MathREPL
7. Wait for code review and feedback

## Running the tests

You can run the tests for MathREPL using `pytest`. To do this, just open a command-line in MathREPL's root directory and run the following command:

```sh
$ pytest -v tests
```

You might need to include the current directory (`.`) in your Python path (`PYTHONPATH`) for this to work. A fast way to do that is by typing the following command in your command-line:

```sh
$ export PYTHONPATH="$PYTHONPATH:."
```

## Author

Leodanis Pozo Ramos – Twitter: [@lpozo78](https://twitter.com/lpozo78) – E-mail: lpozor78@gmail.com

## License

MathREPL is distributed under the MIT license. See [LICENSE](https://github.com/lpozo/mathrepl) for more information.
