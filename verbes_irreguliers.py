#Programme réalisé par BOUKLIKHA Mohamed-Amine => PC : 22
from tkinter import*
from random import*


#Creation de la fenetre
fenetre=Tk()
fenetre.title('BOUKLIKHA Mohamed-Amine')
fenetre.config(width=800, height=500, bg='skyblue')

#Canevas avec un drapeau du Royaume-Unis pour la déco
Canevas=Canvas(fenetre, width=800, height=500, bg='skyblue')
Drapeau=PhotoImage(file='drapeau_anglais.PNG')
Dr=Canevas.create_image(700,60,image=Drapeau)
Canevas.place(x=0, y=0)

#Label pour indiquer ce qu'il faut entrer dans les entry ...
Titre = Label(fenetre, text='LES VERBES IRRÉGULIERS EN ANGLAIS',bg='skyblue', fg='blue', font=('arial', 15, 'bold'))
Titre.place(x=200, y=50)

Infinitif = Label(fenetre, text='Infinitif : ',bg='skyblue',fg='black', font=('arial', 12, 'bold'))
Infinitif.place(x=50, y=150)

Preterit = Label(fenetre, text='Preterit : ',bg='skyblue',fg='black', font=('arial', 12, 'bold'))
Preterit.place(x=50, y=200)

Past_Perfect = Label(fenetre, text='Past Perfect : ',bg='skyblue',fg='black', font=('arial', 12, 'bold'))
Past_Perfect.place(x=50, y=250)

Traduction = Label(fenetre, text='Traduction : ',bg='skyblue',fg='black', font=('arial', 12, 'bold'))
Traduction.place(x=50, y=320)



#Entree pour rentrer les verbes
EntreeI = Entry(fenetre)                                                  #Entree pour les verbes à l'infinitif
EntreeI.place(x=150, y=150)

EntreePr = Entry(fenetre)                                                 #Entree pour les verbes au preterit
EntreePr.place(x=150, y=200)

EntreePp = Entry(fenetre)                                                 #Entree pour les verbes au past perfect
EntreePp.place(x=150, y=250)

#Lecture du fichier csv et passage au dictionnaire
file = open ('verbes.csv', 'r', encoding='utf-8')
Donnees = file.read()
file.close()
verbes = []
ligne = Donnees.split("\n")                             #Redécoupe chaque ligne pour obtenir les éléments des colonnes

for i in range(1, len(ligne)):
    d_ligne = ligne[i].split(";")
    verbes.append({'infinitif': d_ligne[0], 'preterit': d_ligne[1], 'past perfect': d_ligne[2], 'traduction': d_ligne[3]})

#Label contenant la traduction du mot choisi au hasard
francais = Label(fenetre, bg='grey', font=('arial', 10, 'bold'))

def jouer():
    global choix
    francais.event_delete
    choix = choice(verbes)
    verbesfr = choix['traduction']
    francais.config(text=verbesfr, bg='grey', font=('arial', 10, 'bold'))
    francais.place(x=150, y=320)
    Consigne = Label(fenetre,text=' • Un mot est choisi au hasard en francais tu devras trover sa traduction en anglais .',bg='skyblue', fg='black', font=('arial', 8, 'bold'))
    Consigne.place(x=250, y=350)

    Consigne2 = Label(fenetre, text=" • Et ensuite répondre dans les différentes cases afin de t'améliorer dans les verbes irréguliers .", bg='skyblue', fg='black',font=('arial', 8, 'bold'))
    Consigne2.place(x=250, y=400)

    Consigne3 = Label(fenetre, text='  Good luck !  ', bg='skyblue', fg='black', font=('arial', 8, 'bold'))
    Consigne3.place(x=480, y=450)
Jouer = Button(fenetre, text=' Jouer  ! ', command=jouer)
Jouer.place(x=50, y=100)


#Label pour indiquer si c'est vrai ou faux
#Vérification de l'Infinitif
BonneReponseInfinitif = Label(fenetre, bg='skyblue')
ReponseInfinitif = Label(fenetre, bg='skyblue')

#Preterit
BonneReponsePreterit = Label(fenetre, bg='skyblue')
ReponsePreterit = Label(fenetre, bg='skyblue')

#PastPerfect
BonneReponsePastPerfect = Label(fenetre, bg='skyblue')
ReponsePastPerfect = Label(fenetre, bg='skyblue')

#Compteur pour compter le nombre de point
CompteurPoint = Label(fenetre, bg='skyblue')

def Valider():
    global BonneReponseInfinitif, BonneReponsePreterit, BonneReponsePastPerfect, CompteurPoint, ReponseInfinitif, \
    ReponsePreterit, ReponsePastPerfect

    Inf = EntreeI.get()                                      # Récupère la valeur de l'Entry de l'infinitif
    Pret = EntreePr.get()                                    # Récupère la valeur de l'Entry de preterit
    PastP = EntreePp.get()                                   # Récupère la valeur de l'Entry de Past Perfect
    VerbesInfinitif = choix['infinitif']
    VerbesPreterit = choix['preterit']
    VerbesPastPerfect = choix['past perfect']

    if  Inf == VerbesInfinitif:
        BonneReponseInfinitif.config(text='BONNE RÉPONSE ! ', fg='green')
        BonneReponseInfinitif.place(x=350, y=150)
        CompteurPoint += 1

    else:
        BonneReponseInfinitif.config(text='FAUX', fg='red')
        BonneReponseInfinitif.place(x=350, y=150)

        ReponseInfinitif.config(text= '➔' + '    ' + "C'était " + VerbesInfinitif + " et non " + Inf, font=('arial', 8, 'bold'))
        ReponseInfinitif.place(x=400, y=150)


    if  Pret == VerbesPreterit:
        BonneReponsePreterit.config(text='BONNE RÉPONSE ! ', fg='green')
        BonneReponsePreterit.place(x=350, y=200)
        CompteurPoint += 1

    else:
        BonneReponsePreterit.config(text='FAUX', fg='red')
        BonneReponsePreterit.place(x=350, y=200)

        ReponsePreterit.config(text= '➔' + '    ' + "C'était " + VerbesPreterit + " et non " + Pret, font=('arial', 8, 'bold'))
        ReponsePreterit.place(x=400, y=200)


    if  PastP == VerbesPastPerfect:
        BonneReponsePastPerfect.config(text='BONNE RÉPONSE ! ', fg='green')
        BonneReponsePastPerfect.place(x=350, y=250)
        CompteurPoint += 1

    else:
        BonneReponsePastPerfect.config(text='FAUX', fg='red')
        BonneReponsePastPerfect.place(x=350, y=250)

        ReponsePastPerfect.config(text= '➔' + '    ' + "C'était " + VerbesPastPerfect + " et non " + PastP, font=('arial', 8, 'bold'))
        ReponsePastPerfect.place(x=400, y=250)

Valider = Button(fenetre,text=' Valider ', command=Valider)
Valider.place(x=50,y=370)


fenetre.mainloop()

