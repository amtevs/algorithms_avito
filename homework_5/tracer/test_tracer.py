import io
import unittest
from contextlib import redirect_stdout
from tracer import trace_recursion


class TestTraceRecursion(unittest.TestCase):
    def capture(self, func, *args):
        output = io.StringIO()
        with redirect_stdout(output):
            result = func(*args)
        return result, output.getvalue().splitlines()

    def test_factorial(self):
        @trace_recursion
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)
        result, lines = self.capture(factorial, 3)
        self.assertEqual(result, 6)
        self.assertEqual(lines, [
            "Вызов factorial: (3,), {}",
            "    Вызов factorial: (2,), {}",
            "        Вызов factorial: (1,), {}",
            "        Возврат factorial: 1",
            "    Возврат factorial: 2",
            "Возврат factorial: 6",
        ])

    def test_base_case(self):
        @trace_recursion
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)
        result, lines = self.capture(factorial, 0)
        self.assertEqual(result, 1)
        self.assertEqual(lines, [
            "Вызов factorial: (0,), {}",
            "Возврат factorial: 1",
        ])

    def test_branching_recursion(self):
        @trace_recursion
        def fib(n):
            if n <= 1:
                return n
            return fib(n - 1) + fib(n - 2)
        result, lines = self.capture(fib, 2)
        self.assertEqual(result, 1)
        self.assertEqual(lines, [
            "Вызов fib: (2,), {}",
            "    Вызов fib: (1,), {}",
            "    Возврат fib: 1",
            "    Вызов fib: (0,), {}",
            "    Возврат fib: 0",
            "Возврат fib: 1",
        ])