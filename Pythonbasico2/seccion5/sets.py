set1 = {2,3,5,7}
set2 = set([2,3,5,7])

nombres = {"Elena", "Juana", "Pablo","Elena"}
#print(nombres)

#Los set son inmutables, no pueden ser modificados.
#for nombre in nombres:
    #print(nombre)

    #print("Pedro" in nombres)

    #clase 2
nombres.add("Pedro")
print(nombres)

nombres.remove("Elena")
print(nombres)

nombres.pop()
print(nombres)