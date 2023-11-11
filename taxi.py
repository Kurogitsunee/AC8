import taxi_funcs as tf

while True:
    try:
        n = int(input('Введите количество работников: '))
        break

    except ValueError:
        print('Пожалуйста, введите число.')

# create dicts and lists for data
person = {}
taxi = {}
sort = {}
person_n = []
total_sum = int()

# distance for each employee
i = 0
while i < n:
    try:
        distance_i = int(input(f'Укажите расстояние для {i + 1} работника: '))
        person[i + 1] = distance_i
        i += 1
    except ValueError:
        print('Пожалуйста, введите число.')

# price for each taxi
i = 0
while i < n:
    try:
        cost_i = int(input(f'Укажите цену для {i + 1} такси: '))
        taxi[i + 1] = cost_i
        i += 1
    except ValueError:
        print('Пожалуйста, введите число.')

# make the least distance equal to the greatest price by index
taxi_sorted = sorted(taxi.values(), reverse=True)
person_sorted = sorted(person.values())

# find taxi for each employee
for i in range(n):
    q1 = person_sorted[i]
    s1 = taxi_sorted[i]

    q = tf.my_keys(person, q1)
    s = tf.my_keys(taxi, s1)

    sort[s] = q

    del person[q]
    del taxi[s]

# taxi's numbers in order of employees
sort1 = sorted(sort.values())

for i in range(n):
    s2 = sort1[i]
    s3 = tf.my_keys(sort, s2)

    person_n.append(s3)

# find cost
for i in range(n):
    sum = taxi_sorted[i] * person_sorted[i]
    total_sum += sum

# print results
print(f"Такси для работников (начиная с первого работника): ", end='')
print(*person_n)
print(total_sum)
tf.cash(total_sum)