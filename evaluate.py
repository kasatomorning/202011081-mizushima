from expressions import BinExpr, Int
import sys


def evaluate(expr):
    if isinstance(expr, BinExpr):
        op = expr.operator
        if op == "+":
            return evaluate(expr.lhs) + evaluate(expr.rhs)
        elif op == "-":
            return evaluate(expr.lhs) - evaluate(expr.rhs)
        elif op == "*":
            return evaluate(expr.lhs) * evaluate(expr.rhs)
        elif op == "/":
            return int(evaluate(expr.lhs) / evaluate(expr.rhs))
        # 四則演算に加えて、べき乗を追加
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


def tPower(a, b):
    return BinExpr("**", a, b)


def tInt(v):
    return Int(v)


def main():
    test = tAdd(tInt(1), tInt(1))
    assert evaluate(test) == 2, "error occured!"
    print("1 + 1 == 2")

    test = tAdd(tAdd(tInt(1), tInt(2)), tInt(3))
    assert evaluate(test) == 6, "error occured!"
    print("1 + 2 + 3 == 6")

    test = tSub(tInt(1), tInt(1))
    assert evaluate(test) == 0, "error occured!"
    print("1 - 1 == 0")

    test = tMul(tInt(2), tInt(2))
    assert evaluate(test) == 4, "error occured!"
    print("2 * 2 == 4")

    test = tDiv(tInt(6), tInt(2))
    assert evaluate(test) == 3, "error occured!"
    print("6 / 2 == 3")

    test = tPower(tInt(2), tInt(3))
    assert evaluate(test) == 8, "error occured!"
    print("2 ** 3 == 8")

    test = tDiv(tSub(tAdd(tInt(1), tMul(tInt(2), tInt(3))), tInt(1)), tInt(2))
    assert evaluate(test) == 3, "error occured!"
    print("(1 + (2 * 3) - 1) / 2 == 3")


if __name__ == "__main__":
    main()
