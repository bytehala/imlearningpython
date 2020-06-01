import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
g = int(input())
b = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(f"#{hex(r)[2:]}{hex(g)[2:]}{hex(b)[2:]}".upper())
