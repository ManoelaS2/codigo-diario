import math

A, B, C = map(int, input().split())

M = (A+B+abs(A-B))/2

if M > C:
    print(f"{M:.0f} eh o maior")
else:
    print(f"{C} eh o maior")