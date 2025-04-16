ha = int(input('Digite a hora: '))
ma = int(input('Digite os minutos: '))
sa = int(input('Digite os segundos: '))    
h = 0
while h <= 23:
    m = 0
    while m <= 59:
        s = 0
        while s <= 59:
            print(f'{h}:{m}:{s}')
            if h == ha and m == ma and s == sa:
                print('ALARME!')
                break
            s+=1
        if h == ha and m == ma:
            break   
        m+=1
    if h == ha:
        break    
    h+=1  
