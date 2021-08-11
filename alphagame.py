import random

ALP = ["A","B","C","D","E","F","G"]     #리스트로 알파벳 정의
r = random.choice(ALP)

alp = ""
for i in ALP:
    if i != r:
        alp = alp + i
        
print(alp)
        
