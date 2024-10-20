# Bemenet beolvasása
n = int(input())
arr = list(map(int, input().split()))

# Tömb rendezése
arr.sort()

# Egyedi elemek számlálása rendezett tömbben
unique_count = 1  # Az első elemet biztosan beleszámoljuk

for i in range(1, n):
    if arr[i] != arr[i - 1]:
        unique_count += 1

# A különböző értékek számának kinyomtatása
print(unique_count)
