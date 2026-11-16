from collections import Counter

reports = [
    (28.7041, 77.1025),
    (28.7049, 77.1031),
    (28.7102, 77.0950),
    (28.7044, 77.1029),
    (28.6512, 77.2301),
    (28.7047, 77.1022),
]

def cell(lat, lon):
    return round(lat, 2), round(lon, 2)

hotspots = Counter(cell(lat, lon) for lat, lon in reports)

print("Most dangerous stretches this month:")
for rank, ((lat, lon), n) in enumerate(hotspots.most_common(3), start=1):
    word = "animal" if n == 1 else "animals"
    print(f"{rank}. near {lat:.2f}, {lon:.2f}: {n} {word} hit")
