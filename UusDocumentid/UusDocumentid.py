print("Tere! Olen sinu uus sõber - Python!")
nimi=input("nimi => ")
print("oi kui ilus nimi!")
a=input("Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
if a=="1":

    while True:
        try:
         pikkus=int(input("Pikkus: "))
         if pikkus>0 and pikkus<273: break
        except:
            print("Error,")
    mass=-1
    while mass<0 or mass>400:
        try:
            mass=int(input("Mass: "))
       
        except:
            print("Error")
    try:
        index=mass/(0.01*pikkus)**2
        if index<16:
            print("Tervisele ohtlik alakaal")
        elif index>=16 and index<19:
            print("Alakaal")
        elif index>=19 and index<25:
            print("Normaalkaal")
        elif index>=25 and index<30:
            print("Ülekaal")
        elif index>=30 and index<35:
            print("Rasvumine")
        elif index>=35 and index<40:
            print("Tugev rasvumine")
        elif index>=40:
            print("Tervisele ohtlik rasvumine")
    except:
        print("Error")

else:
    print("Kahju! See on väga kasulik info!")
    g