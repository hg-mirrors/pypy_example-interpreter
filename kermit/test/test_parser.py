
from kermit.sourceparser import parse, Stmt, Block, ConstantInt, BinOp,\
     Variable, Assignment

def test_parse_basic():
    assert parse('13;') == Block([Stmt(ConstantInt(13))])
    assert parse('1 + 2;') == Block([Stmt(BinOp("+", ConstantInt(1),
                                                ConstantInt(2)))])
    assert parse('1 + a;') == Block([Stmt(BinOp('+', ConstantInt(1),
                                                Variable('a')))])

def test_multiple_statements():
    assert parse('''
    1 + 2;
    c;
    e;
    ''') == Block([Stmt(BinOp("+", ConstantInt(1), ConstantInt(2))),
                   Stmt(Variable('c')),
                   Stmt(Variable('e'))])

def test_assignment():
    assert parse('a = 3;') == Block([Assignment('a', ConstantInt(3))])
