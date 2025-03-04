# Print nCr and nPr.
n = int(input())
r = int(input())
f = 1
for i in range(1, n + 1):
    f *= i
nf = f
rf = 1
for i in range(1, r + 1):
    rf *= i
nrf = 1
for i in range(1, n - r + 1):
    nrf *= i
print("nCr:", nf // (rf * nrf))
print("nPr:", nf // nrf)
