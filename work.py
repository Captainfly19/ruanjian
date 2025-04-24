import unittest
import random


class TestCalculator(unittest.TestCase):
    def setUp(self):
        from calculator import Calculator
        self.calculator = Calculator()

    def test_operator_generation(self):
        valid_ops = {'+', '-', '*', '/'}
        for _ in range(100):
            op = self.calculator.generate_operator()
            self.assertIn(op, valid_ops, f"无效运算符：{op}")

    def test_operand_range(self):
        for _ in range(100):
            a, b = self.calculator.generate_operands()
            self.assertTrue(1 <= a <= 100, f"a 超出范围：{a}")
            self.assertTrue(1 <= b <= 100, f"b 超出范围：{b}")

    def test_addition(self):
        a, b = 5, 3
        result = self.calculator.calculate(a, b, '+')
        self.assertEqual(result, 8, f"加法错误：{a} + {b} ≠ 8")

    def test_subtraction(self):
        a, b = 10, 4
        result = self.calculator.calculate(a, b, '-')
        self.assertEqual(result, 6, f"减法错误：{a} - {b} ≠ 6")

    def test_multiplication(self):
        a, b = 7, 2
        result = self.calculator.calculate(a, b, '*')
        self.assertEqual(result, 14, f"乘法错误：{a} * {b} ≠ 14")

    def test_division(self):
        a, b = 12, 3
        result = self.calculator.calculate(a, b, '/')
        self.assertEqual(result, 4.0, f"除法错误：{a} / {b} ≠ 4.0")

        for _ in range(100):
            a, b = self.calculator.generate_operands()
            self.assertNotEqual(b, 0, "除法时 b 不能为 0")

    def test_full_process(self):
        for _ in range(50):
            a, b = self.calculator.generate_operands()
            op = self.calculator.generate_operator()
            expected = self.calculator.calculate(a, b, op)
            self.assertTrue(b != 0 or op != '/', "除法时 b 为 0")


if __name__ == '__main__':
    unittest.main()

import random


class Calculator:
    def generate_operator(self):
        return random.choice(['+', '-', '*', '/'])

    def generate_operands(self):
        return random.randint(1, 100), random.randint(1, 100)

    def calculate(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        else:
            raise ValueError("无效运算符")

    def generate_question(self):
        a, b = self.generate_operands()
        op = self.generate_operator()
        result = self.calculate(a, b, op)
        return f"{a} {op} {b} = {result}", result

import random


class Calculator:
    def generate_operator(self):
        """生成随机运算符（+、-、*、/）"""
        return random.choice(['+', '-', '*', '/'])

    def generate_operands(self):
        """生成两个 1 - 100 的整数"""
        return random.randint(1, 100), random.randint(1, 100)

    def calculate(self, a, b, op):
        """根据运算符计算结果"""
        operations = {
            '+': lambda: a + b,
            '-': lambda: a - b,
            '*': lambda: a * b,
            '/': lambda: a / b
        }
        if op not in operations:
            raise ValueError("无效运算符")
        return operations[op]()

    def generate_question(self):
        """生成完整的运算问题（表达式 + 结果）"""
        a, b = self.generate_operands()
        op = self.generate_operator()
        result = self.calculate(a, b, op)
        return f"{a} {op} {b} = {result}", result
