import math
x, y = map(float, input().split())
xx, yy = map(float, input().split())

D = math.sqrt((xx-x)**2 + (yy-y)**2)

print(f"{D:.4f}")
