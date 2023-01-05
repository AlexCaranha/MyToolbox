import Levenshtein

s1 = "kitten"
s2 = "sitting"

distance = Levenshtein.distance(s1, s2)
print(distance)  # Output: 3
