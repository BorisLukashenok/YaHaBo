import numpy as np

n = list(map(float, input().split()))
print(np.exp(np.log(n).mean()))
