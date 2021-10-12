def make_division_by(n):
    def division(x):
        return x / n
    return division

division_by_3 = make_division_by(3)
division_by_2 =  make_division_by(2)

print(division_by_3(18))
print(division_by_2(40))