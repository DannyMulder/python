#opdracht1.1

for i in range(5):
    print("*****")

print()

for i in range(1, 6):
    print("*" * i)

print()

for i in range(5, 0, -1):
    print("*" * i)

print()

for i in range(5):
    for j in range(1, 6):
        print(j, end="")
    print()

print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print()


for i in range(1, 6):
    print("." * (5 - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()

#opdracht1.2


i = 0
while i < 5:
    print("*****")
    i += 1

print()

i = 1
while i <= 5:
    print("*" * i)
    i += 1

print()

i = 5
while i >= 1:
    print("*" * i)
    i -= 1

print()

i = 0
while i < 5:
    j = 1
    while j <= 5:
        print(j, end="")
        j += 1
    print()
    i += 1

print()

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1

print()

i = 1
while i <= 5:
    print("." * (5 - i), end="")
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1

#opdracht2

grootte = int(input("Hoe groot moet het vierkant zijn? "))
rand = input("Welk symbool heeft de rand? ")
inhoud = input("Welk symbool heeft de inhoud? ")

print()

for rij in range(grootte):
    regel = ""
    for kolom in range(grootte):
        if rij == 0 or rij == grootte - 1:
            regel += rand
        elif kolom == 0 or kolom == grootte - 1:
            regel += rand
        else:
            regel += inhoud
    print(regel)
