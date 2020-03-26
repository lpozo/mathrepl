# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""MathREPL, a math expression evaluator using Python's eval() and math."""

from mathrepl import PS1, USAGE, WELCOME
from mathrepl.mathrepl import evaluate


def main():
    """Main loop: Read and evaluate user's input."""
    print(WELCOME)
    while True:
        # Read user's input
        try:
            expression = input(f"{PS1} ")
        except (KeyboardInterrupt, EOFError):
            raise SystemExit()

        # Handle special commands
        if expression.lower() == "help":
            print(USAGE)
            continue
        if expression.lower() in {"quit", "exit"}:
            raise SystemExit()

        # Evaluate the expression and handle errors
        try:
            result = evaluate(expression)
        except SyntaxError:
            # If the user enters an invalid expression
            print("Invalid input expression syntax")
            continue
        except NameError as err:
            # If the user tries to use a name that isn't allowed
            print(err)
            continue

        # Print the result if no error occurs
        print(f"The result is: {result}")


if __name__ == "__main__":
    main()
