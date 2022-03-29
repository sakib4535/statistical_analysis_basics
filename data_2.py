area_list = [
            ["Zigatola", "Dhanmondi", "spam"],
            ["Hazaribag", "Tenari", "RayerBazar"],
            ["Tali Office", "SonatanGar", "Beribadh", "spam", "Puran Dhaka"],
            ["Dhanmondi", "Lalmatia", "Mohammadpur", "Mitali Road", "Hasan Road"]
]

for area in area_list:
    for index in range(len(area) - 1, - 1, - 1):
        if area[index] == "spam":
            del area[index]
            print(area)

for area in area_list:
    for item in area:
        if item != "Lalmatia":
            print(item)
    else:
        print("{0} has a score of {1} spam".format(area, area.count("spam")))