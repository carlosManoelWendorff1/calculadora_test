import pytest
from Calculadora.Calculadora import Calc
import math

def test_soma():
    val1 = 1;
    val2 = 1;
    soma = val1 + val2;
    assert Calc.soma(val1,val2) == soma;

def test_sub():
    val1 = 1;
    val2 = 1;
    sub = val1 - val2;
    assert Calc.sub(val1,val2) == sub

def test_mult():
    val1 = 1;
    val2 = 1;
    mult = val1 * val2;
    assert Calc.mult(val1,val2) == mult

def test_div():
    val1 = 1;
    val2 = 1;
    div = val1 * val2;
    assert Calc.div(val1,val2) == div

def test_pot():
    val1 = 1;
    val2 = 1;
    pot = val1 ** val2;
    assert Calc.pot(val1,val2) == pot

def test_raiz():
    val1 = 1;
    raiz = math.sqrt(val1)
    assert Calc.raiz(val1) == raiz
