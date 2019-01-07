import json
with open('lists.json', 'r') as f:
    lists_dict = json.load(f)

age = []
G1 = []
G2 = []
G3 = []
G4 = []
G5 = []
G6 = []
G7 = []
G8 = [] 
G9 = []
for lists in lists_dict:
    age = (lists['candidate']['age'])
    if age >= 10 and age <= 19:
        G1.append(age)
    elif age >= 20 and age <= 29:
        G2.append(age)
    elif age >= 30 and age <= 39:
        G3.append(age)
    elif age >= 40 and age <= 49:
        G4.append(age)
    elif age >= 50 and age <= 59:
        G5.append(age)
    elif age >= 60 and age <= 69:
        G6.append(age)
    elif age >= 70 and age <= 79 :
        G7.append(age)
    elif age >= 80 and age <= 89:
        G8.append(age)
    elif age >= 90 and age <= 99:
        G9.append(age)
    else:
        pass

total = len(G1) + len(G2) + len(G3) + len(G4) + len(G5) + len(G6) + len(G7) + len(G8) + len(G9)

def calc(a):
    return a*0.018
print('Between 10 and 19 is '+ str(calc(len(G1))) + ' %')
print('Between 20 and 29 is '+ str(calc(len(G2))) + ' %')
print('Between 30 and 39 is '+ str(calc(len(G3))) + ' %')
print('Between 40 and 49 is '+ str(calc(len(G4))) + ' %')
print('Between 50 and 59 is '+ str(calc(len(G5))) + ' %')
print('Between 60 and 69 is '+ str(calc(len(G6))) + ' %')
print('Between 70 and 79 is '+ str(calc(len(G7))) + ' %')
print('Between 80 and 89 is '+ str(calc(len(G8))) + ' %')
print('Between 90 and 99 is '+ str(calc(len(G9))) + ' %')