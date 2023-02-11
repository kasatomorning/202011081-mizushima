class Expr:
    def __init__(self, type) -> None:
        self.type = type


class BinExpr(Expr):
    def __init__(self, op, lhs, rhs) -> None:
        super().__init__("BinExpr")
        self.operator = op
        self.lhs = lhs
        self.rhs = rhs


class Int(Expr):
    def __str__(self) -> str:
        return str(self.value)

    def __init__(self, value) -> None:
        super().__init__("Int")
        self.value = value
