a = sorted(list(map(int, [input(), input(), input()])))
if a[2]**2 == a[1]**2 + a[0]**2:
    print("100%")
if a[2]**2 > a[1]**2 + a[0]**2:
    print("велика")
if a[2]**2 < a[1]**2 + a[0]**2:
    print("крайне мала")
