import pandas as pd


shots = pd.read_csv("data171_4fcbd1f963.csv")
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x1, x2 = min(x1, x2), max(x1, x2)
y1, y2 = min(y1, y2), max(y1, y2)
print(shots.loc[(shots['x'] >= x1) & (shots['x'] <= x2)
      & (shots['y'] >= y1) & (shots['y'] <= y2)])
