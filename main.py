#!/usr/bin/env python3

import sys
from sympy import latex
from sympy import sympify
from sympy.parsing.latex import parse_latex

def LatexToMath(expr):
    """Convert LaTeX expression to math format"""
    try:
        result = str(parse_latex(expr))
        return result
    except Exception as e:
        print(f"Error parsing LaTeX: {e}")
        return None

def MathToLatex(expr):
    """Convert math expression to LaTeX format"""
    try:
        result = latex(sympify(expr, evaluate=False))
        return result
    except Exception as e:
        print(f"Error parsing math expression: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <latex_expression>")
        print("Example: python main.py \"\\frac{1}{2}\"")
        sys.exit(1)
    
    latex_expr = sys.argv[1]
    
    print(f"Input LaTeX: {latex_expr}")
    
    # Convert LaTeX to math
    math_result = LatexToMath(latex_expr)
    if math_result:
        print(f"Math format: {math_result}")
    else:
        print("Conversion failed")
        sys.exit(1)

if __name__ == "__main__":
    main()