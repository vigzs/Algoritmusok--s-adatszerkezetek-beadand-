#https://www.spoj.com/problems/CODEM4/cstart=20

def Okos(tomb):
    if len(tomb) == 2:
        return [max(tomb), min(tomb)]
    else:
        tombHEAD = tomb[:-1]
        tombTAIL = tomb[1:]
        N = len(tomb)
        if tomb[0] + Okos(tombTAIL)[1] >= tomb[N-1] + Okos(tombHEAD)[1]:
            return [tomb[0] + Okos(tombTAIL)[1], Okos(tombTAIL)[0]]
        else:
            return [tomb[N-1] + Okos(tombHEAD)[1], Okos(tombHEAD)[0]]


def Okos2(tomb):
    if len(tomb) == 2:
        return [max(tomb), min(tomb)]
    else:
        tombHEAD = tomb[:-1]
        tombTAIL = tomb[1:]
        N = len(tomb)
        if tomb[0] + Buta(tombTAIL)[1] >= tomb[N-1] + Buta(tombHEAD)[1]:
            return [tomb[0] + Buta(tombTAIL)[1], Buta(tombTAIL)[0]]
        else:
            return [tomb[N-1] + Buta(tombHEAD)[1], Buta(tombHEAD)[0]]

def Buta(tomb):
    tombHEAD = tomb[:-1]
    tombTAIL = tomb[1:]
    N = len(tomb)
    if tomb[0] + Okos2(tombTAIL)[1] <= tomb[N-1] + Okos2(tombHEAD)[1]:
        return [tomb[0] + Okos2(tombTAIL)[1], Okos2(tombTAIL)[0]]
    else:
        return [tomb[N-1] + Okos2(tombHEAD)[1], Okos2(tombHEAD)[0]]



import sys

t = int(input().strip())
results = []

for i in range(t):
    size = int(input().strip())
    tomb=list(map(int, input().strip().split()))
    result = [Okos2(tomb)[0], Okos(tomb)[0]]
    results.append(result)
    

for res in results:
    print(" ".join(map(str, res)))