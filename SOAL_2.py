print ("alat cek palinrome")
asdf = str(input("kata: "))
print ("")
def funpalingdrome():
    if asdf == asdf[::-1]:
        print ("yes")
        print ("jika dibalik ",asdf[::-1])
    else:
        print ("no")
        print ("jika dibalik ",asdf[::-1])
funpalingdrome()