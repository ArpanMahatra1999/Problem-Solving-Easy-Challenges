b, w, bc, wc, z = 3,3,1,9,2
cost = 0
if bc > wc + z:
    cost = (b + w) * wc + b * z
elif wc > bc + z:
    cost = (b + w) * bc + w * z
else:
    cost = b * bc + w * wc
print(cost)
