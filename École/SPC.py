form=input("Mettez 1 pour la masse volumique, 2 pour la concentration massique, 3 pour la loi des mailles, 4 pour la loi des noeuds, 5 pour la loi d'ohm et 6 pour connaitre la masse d'un atome ")
if int(form)==1:
    print("Vous avez choisis la masse volumique. Sa formule est m/V=mv où m est la masse de la substance et V son volume. Voulez-vous calculer m, V ou mv ? ")
    rep=input("")
    if rep=="mv":
      m=input("m= ")
      V=input("V= ")
      u1=input("Unité de m : ")
      u2=input("Unité de V : ")
      m=float(m)
      V=float(V)
      mv=m/V
      mv=str(mv)
      print("La masse volumique de cette substance est "+mv+u1+"/"+u2)
    if rep=="m":
        V=input("V= ")
        mv=input("mv= ")
        V=float(V)
        mv=float(mv)
        m=mv*V
        m=str(m)
        print("La masse de cette substance est "+m)
if int(form)==2:
    print("Vous avez choisis la concetration massique. Sa formule est m/V=C où m est la masse du soluté et V le volume de la solution.")
    m=input("m= ")
    m=float(m)
    V=input("V= ")
    V=float(V)
    u1=input("Unité de m : ")
    u2=input("Unité de V : ")
    mv=m/V
    mv=str(mv)
    print("La concentration massique de cette substance est de "+mv+u1+"/"+u2)
if int(form)==3:
    print("Vous avez choisis la loi des mailles. Cette loi dis que la somme de toutes les tensions d'une maille doit etre nulle ou U1+U2+U3-Ug=0 ou encore Ug=U1+U2+U3")
    rep=input("Voulez-vous calculer U1, U2, U3 ou Ug ? ")
    if rep=="U1":
      U2=int(input("U2= "))
      U3=int(input("U3= "))
      Ug=int(input("Ug= "))
      U1=Ug-U2-U3
      unite=input("Unité des valeurs = ")
      print("U1 est égal à "+str(U1)+unite)
    if rep=="U2":
      U1=int(input("U1= "))
      U3=int(input("U3= "))
      Ug=int(input("Ug= "))
      U2=Ug-U1-U3
      unite=input("Unité des valeurs = ")
      print("U2 est égal à "+str(U2)+unite)
    if rep=="U3":
      U1=int(input("U1= "))
      U2=int(input("U2= "))
      Ug=int(input("Ug= "))
      U3=Ug-U2-U1
      unite=input("Unité des valeurs = ")
      print("U3 est égal à "+str(U3)+unite)
    if rep=="Ug":
      U1=int(input("U1= "))
      U2=int(input("U2= "))
      U3=int(input("U3= "))
      Ug=U1+U2+U3
      unite=input("Unité des valeurs = ")
      print("Ug est égal à "+str(Ug)+unite)
if int(form)==4:
    print("Vous avez choisi la loi des noeuds. Cette loi dis que la somme des intensitées rentrant et sortant d'un noeud est nulle. Soit I1 et I2 intensités entrantes et I3 et I4 intensitées sortantes, I1+I2-I3-I4=0 ou I1+I2=I3+I4.")
    rep=input("Voulez-vous calculer I1, I2, I3 ou I4 ? ")
    if rep=="I1":
      I2=int(input("I2= "))
      I3=int(input("I3= "))
      I4=int(input("I4= "))
      I7=I3+I4-I2
      I1=str(I1)
      unite=input("Unité des valeurs = ")
      print("I1 est égal à "+str(I1)+unite)
    if rep=="I2":
      I1=int(input("I1= "))
      I3=int(input("I3= "))
      I4=int(input("I4= "))
      I2=I3+I4-I1
      I2=str(I2)
      unite=input("Unité des valeurs = ")
      print("I2 est égal à "+str(I2)+unite)
    if rep=="I3":
      I1=int(input("I1= "))
      I2=int(input("I2= "))
      I4=int(input("I4= "))
      I3=I1+I2-I4
      I3=str(I3)
      unite=input("Unité des valeurs = ")
      print("I3 est égal à "+str(I3)+unite)
    if rep=="I4":
      I1=int(input("I1= "))
      I2=int(input("I2= "))
      I3=int(input("I3= "))
      I4=I1+I2-I3
      I4=str(I4)
      unite=input("Unité des valeurs = ")
      print("I4 est égal à "+str(I4)+unite)
if int(form)==5:
    print("Vous avez choisi la loi d'Ohm. Cette loi dis que la tension aux bornes de d'une résistance (U) est égale au produit de la valeur de cette résistance (R) par l'intensité aux bornes de cette même résistance (I) ou U=R*I.")
    rep=input("Voulez-vous calculer U, R ou I ? ")
    if rep=="U":
      I=int(input("I= "))
      R=int(input("R= "))
      U=R*I
      print("U est égal à "+str(U)+"V")
    if rep=="R":
      I=int(input("I= "))
      U=int(input("U= "))
      R=U/I
      print("R est égal à "+str(R)+" Ohm")
    if rep=="I":
      R=int(input("R= "))
      U=int(input("U= "))
      I=U*R
      print("I est égal à "+str(I)+"A")
if int(form)==6:
    print("Vous avez choisi de calculer la masse d'un atome. Pour la calculer, il faut multiplier le nombre de nucléons (A) par le poids d'un nucléon (1.67*10**-27) soit A * 1.67*10**-27")
    A=int(input("Quel est le nombre de masse de l'atome dont vous voulez connaitre la masse ? "))
    ma=A*(1.67*10**-27)
    print("La masse de l'atome est "+str(ma))
