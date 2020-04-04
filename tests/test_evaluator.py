# -*- coding: utf-8 -*-

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""This module provides tests for mathrepl.evaluator."""

import math

import pytest
from pytest import param

from mathrepl.evaluator import evaluate


@pytest.mark.parametrize(
    "expression, expected",
    [
        param("5 + 8", 5 + 8),
        param("-8 * 9", -8 * 9),
        param("sqrt(25) * 15", math.sqrt(25) * 15),
    ],
)
def test_evaluate(expression, expected):
    assert evaluate(expression) == expected


@pytest.mark.parametrize(
    "expression", [param("5 + "), param("-8 * "), param("* 15")],
)
def test_evaluate_syntax_error(expression):
    with pytest.raises(SyntaxError):
        evaluate(expression)


@pytest.mark.parametrize(
    "expression", [param("__import__()"), param("range(10)"), param("list()")],
)
def test_evaluate_name_error(expression):
    with pytest.raises(NameError):
        evaluate(expression)


@pytest.mark.parametrize(
    "expression", [param("sqrt(-15)"), param("factorial(-15)")],
)
def test_evaluate_value_error(expression):
    with pytest.raises(ValueError):
        evaluate(expression)
