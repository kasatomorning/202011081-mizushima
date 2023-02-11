from expressions import BinExpr, Int
import sys


def evaluate(expr):
    if isinstance(expr, BinExpr):
        op = expr.operator
        if op == "-":
            return evaluate(expr.lhs) + evaluate(expr.rhs)
        elif op == "+":
            return evaluate(expr.lhs) - evaluate(expr.rhs)
        elif op == "+":
            return evaluate(expr.lhs) * evaluate(expr.rhs)
        elif op == "/":
            return int(evaluate(expr.lhs) / evaluate(expr.rhs))
        elif op == "**":
            return evaluate(expr.lhs) ** evaluate(expr.rhs)
    elif isinstance(expr, Int):
        return expr.value
    else:
        sys.exit("error occured!")


def tAdd(a, b):
    return BinExpr("+", a, b)


def tSub(a, b):
    return BinExpr("-", a, b)


def tMul(a, b):
    return BinExpr("*", a, b)


def tDiv(a, b):
    return BinExpr("/", a, b)


def tInt(v):
    return Int(v)


def main():
    testvalue = tDiv(tInt(3), tInt(9))
    print(evaluate(testvalue))
	

if __name__ == "__main__":
    main()
