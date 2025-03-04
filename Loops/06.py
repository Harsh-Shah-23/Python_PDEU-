# Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.
for h in range(24):
    if h == 0:
        print("12 Midnight")
    elif h < 12:
        print(h, "AM")
    elif h == 12:
        print("12 Noon")
    else:
        print(h - 12, "PM")
