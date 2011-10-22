#!/usr/bin/env python

from sys import argv
import __pypy_path__
from sanya.parser import parse_string
from sanya.llir import hir_compile

def main():
    with open(argv[1]) as f:
        content = f.read()
    list_of_expr = parse_string(content)
    toplevel, walker = hir_compile.compile_list_of_expr(list_of_expr)
    hir_compile.WalkerPrinter(walker).pprint()

if __name__ == '__main__':
    main()