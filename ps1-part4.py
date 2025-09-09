score = 0

# receive numbers
arrests = int(input("Prior arrests: "))
if arrests >= 5:
    score += 1

if arrests >= 2:
    score += 1

ordinance = input("Prior arrests for local ordinance (Y/N): ")
if ordinance == 'Y':
    score += 1

release_age = int(input("Age at release: "))
if release_age >= 18 and release_age <= 24:
    score += 1
elif release_age >= 40:
    score -= 1

# print score
print ("The recidivism risk score is", score)
