 Dizi içersinde eleman sayısı bulma

liste_1 = [0,5,25,100,5,5,0,100]
def my_h(liste_1):
    my_d = {}
    for i in liste_1:
        if i in my_d:
            my_d[i]=my_d[i] + 1
        else:
            my_d[i] = 1
    return my_d
print(my_h(liste_1))

# dizi içersinde eleman sayısı bulma (2)

liste_1 = [0,5,25,100,5,5,0,100]
def my_h(liste_1):
    my_d = {}
    for i  in liste_1:
        if i not in my_d:
           my_d[i] = 1
        else:
            my_d[i] +=1
    return my_d
print(my_h(liste_1))

# Fibonacci hesaplama

known={0:0,1:1}
def fibo_rec(n):
    if n in known:
        return known[n]
    else:
        result = fibo_rec(n-1) + fibo_rec(n-2)
        known[n]=result
        return result
x=fibo_rec(10)
print(x)



# Gönderilen key'in listede varlığının kontrolü
def lookup(d,v):
    for key in range(0,len(liste_1)):
        if d[key]==v:
            return 1
    else:
        return 0

liste_1= [0,5,25,100,5,5,0,100]
print(lookup(liste_1,5100))
