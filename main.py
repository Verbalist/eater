_author__ = 'verbalist'

def get_day_calories(height, weight, age, is_man, active=1.2):
    if is_man:
        return 88.36 + 13.4 * weight + 4.8 * height - 5.7 * age
    else:
        return 447.6 + 9.2 * weight + 3.1 * height - 4.3 * age

print(get_day_calories(170, 50, 33, False, 1.3))