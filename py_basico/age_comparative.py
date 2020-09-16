age_1 = int(input('Cuantos años tienes?: '))
age_2 = int(input('Cual es la edad de tu amigo?: '))

if age_1 > age_2:
    diff = age_1 - age_2
    difw = str(diff)
    print('Eres mayor que tu amigo por ' + difw + ' años')
elif age_1 < age_2:
    diff = age_2 - age_1
    difw = str(diff)
    print('Tu amigo es mayor por ' + difw + ' años')
else:
    print('Los dos tienen la misma edad')

