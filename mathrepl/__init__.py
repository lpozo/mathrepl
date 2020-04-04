# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""MathREPL, a math expression evaluator using Python eval() and the math module."""

import math

__version__ = "1.0"
__author__ = "Leodanis Pozo Ramos"

ALLOWED_NAMES = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}

PS1 = "mr>>"

WELCOME = f"""
MathREPL {__version__}, your Python math expressions evaluator!
Enter a valid math expression after the prompt "{PS1}".
Type "help" for more information.
Type "quit" or "exit" to exit.
"""

USAGE = f"""
Usage:
Build math expressions using numeric values and operators.
Use any of the following functions and constants:

{', '.join(ALLOWED_NAMES.keys())}
"""
