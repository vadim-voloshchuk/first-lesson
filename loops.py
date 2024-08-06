# Loop - Цикл

# Первый вид циклов

sum = 20

while sum > 11:
    sum = sum - 1
    # if sum % 6 == 0:
    #     break
    if sum % 2 == 0:
        print("Чёт")
        
    print(str(sum) + " Я не остановлюсь")

# 0,1 ... 10
# 18,16,14,12,10

# 17 / 2 = 8.5
# 8 * 2 = 16
# 17  16 = 1

# 16 / 2 = 8.0
# 8 * 2 = 16
# 16  16 = 0

# Второй вид циклов

# for переменная in последовательность:
    # Тело цикла

# print("*" * 100)

# for i in range(1,150):
#     for j in range(1,150):
#         print(str(i) + " * " + str(j) + "=" + str(i*j))



# egor = "ЕГОР SFMSFMLMRO MSM Fm KMFOKDDK OMF OKMFMFLDMKM DLLMD KMFKN OKKMFI"
# for i in egor:
#     print(i)
    
print("*" * 100)

width = 53
height = 3

for i in range(height):
    for j in range(width):
        print("#", end='')
    print()

print("*" * 100)

height = 30

for i in range(height + 1):
    for j in range(i):
        print("#", end='')
    print()

print("*" * 100)

height = 30

for i in range(height + 1):
    for j in range(height - i - 1 ):
        print(" ", end='')
    for j in range(2 * i + 1 ):
        print("#", end='')
    print()
