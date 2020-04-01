# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""MathREPL, a math expression evaluator using Python's eval() and math."""

from . import PS1, USAGE, WELCOME


class CliView:
    """Command-line interface."""

    def __init__(self, welcome_msg=WELCOME, usage_msg=USAGE):
        self.welcome_msg = welcome_msg
        self.usage_msg = usage_msg
        self.expression = None

    def print_welcome_msg(self):
        print(self.welcome_msg)

    def read_input(self):
        """Read user's input."""
        try:
            self.expression = input(f"{PS1} ")
        except (KeyboardInterrupt, EOFError):
            raise SystemExit()

    def handle_usage_command(self):
        """Handle usage command."""
        if self.expression.lower() == "help":
            print(self.usage_msg)

    def handle_exit_command(self):
        """Handle exit command."""
        if self.expression.lower() in {"quit", "q", "exit"}:
            raise SystemExit()

    @staticmethod
    def print_result(result):
        """Print the result of the evaluation"""
        print(f"The result is: {result}")
