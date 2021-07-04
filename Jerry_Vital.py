from tkinter import *
import sqlite3 as sq
dictMois = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]

#######################
# Fonction moteur du logiciel
# Entree: VIDE
# Sortie: VIDE
# ######################
def enginer():
    genre = setGenre()
    annee = setDateNaissance(eDateNaissance)

    fenetreResultats = createurFenetre()
    lbGenre = Label(fenetreResultats, text="Genre: " + genre, fg="#240747", bg="#F9F8F4", font="Verdana")
    lbGenre.place(x=0, y=0)
    try:
        lbDate = Label(fenetreResultats, text="Date de naissance: " + str(dictMois[int(eMois.get()) - 1]) + "," + annee,fg="#240747", bg="#F9F8F4", font="Verdana")
        lbDate.place(x=0, y=30)
        lbErreur.config(text="")
    except:
        getErreur()

    connection = sq.connect("Base.data.db")
    cursor = connection.cursor()
    departement = (str(eDepartement.get()))
    ville = (str(eVille.get()))

    try:
        setRegion(fenetreResultats, cursor, departement, ville)

        setDepartement(fenetreResultats, cursor, departement, ville)

        setVille(fenetreResultats, cursor, departement, ville)
    
        setInformationsVille(fenetreResultats, cursor, departement, ville)

        lbErreur.config(text="")
    except :
        getErreur()
    finally:
        connection.close()
    
    if eNe.get()!="":
        lbNumeroNe = Label(fenetreResultats, text="Numéro de Né: "+ eNe.get() , fg="#240747", bg="#F9F8F4",font="Verdana")
        lbNumeroNe.place(x=0, y=170)
        lbErreur.config(text="")
    else:
        getErreur()

#######################
# Fonction permettant de recuperer les informations de la ville
# Entree: fenetre, curseur BD, string, string
# Sortie: VIDE
# ######################
def setInformationsVille(fenetreResultats, cursor, departement, ville):
    cursor.execute('SELECT * FROM "data" WHERE "Code_dep" LIKE '+departement+ ' AND "Code_commune" LIKE '+ville+'')
    req4 = cursor.fetchone()[3]
    L_statut = Label(fenetreResultats, text=""+req4, fg="#240747", bg="#F9F8F4",font="Verdana")
    L_statut.place(x=45, y=140)

#######################
# Fonction permettant de recuperer le nom de la ville
# Entree:fenetre, curseur BD, string, string
# Sortie: VIDE
# ######################
def setVille(fen_resultat, cursor, departement, ville):
    cursor.execute('SELECT * FROM "data" WHERE "Code_dep" LIKE ' + departement + ' AND "Code_commune" LIKE ' + ville + '')
    req3 = cursor.fetchone()[0]
    lbVille = Label(fen_resultat, text="Ville: " + req3, fg="#240747", bg="#F9F8F4",font="Verdana")
    lbVille.place(x=0, y=120)

#######################
# Fonction permettant de recuperer le nom du departement
# Entree:fenetre, curseur BD, string, string
# Sortie: VIDE
# ######################
def setDepartement(fen_resultat, cursor, departement, ville):
    cursor.execute('SELECT * FROM "data" WHERE "Code_dep" LIKE '+ departement + ' AND "Code_commune" LIKE '+ville+'')
    req2 = cursor.fetchone()[1]
    lbdepartement = Label(fen_resultat, text="Département: " + req2, fg="#240747", bg="#F9F8F4",font="Verdana")
    lbdepartement.place(x=0, y=90)

#######################
# Fonction permettant de recuperer le nom de la region
# Entree:fenetre, curseur BD, string, string
# Sortie: VIDE
# ######################
def setRegion(fen_resultat, cursor, departement, ville):
    cursor.execute('SELECT * FROM "data" WHERE "Code_dep" LIKE ' + departement + ' AND "Code_commune" LIKE ' + ville + '')
    req1 = cursor.fetchone()[2]
    lbRegion = Label(fen_resultat, text="Région: " + req1, fg="#240747", bg="#F9F8F4",font="Verdana")
    lbRegion.place(x=0, y=60)

#######################
# Fonction permettant de créer la fenetre de resultat
# Entree: VIDE
# Sortie: fenetre
# ######################
def createurFenetre():
    fenetreResultat = Toplevel()
    fenetreResultat.title("Jerry Vital - Résultat")
    fenetreResultat.geometry("300x350+700+325")
    fenetreResultat.resizable(False, False)
    fenetreResultat.configure(bg="#F9F8F4")
    fenetreResultat.iconbitmap('logo_app.ico')
    return fenetreResultat

#######################
# Fonction permettant de recuperer l'année de naissance
# Entree: string
# Sortie: string
# ######################
def setDateNaissance(dateNaissance):
    try:
        if anneeSuperieurAnneeActuelle() or anneeInferieurAnneeActuelleRetraite():
            annee = setAnnee("19", dateNaissance)
        elif anneeInferieurAnneeActuellePasRetraite():
            annee = setAnnee("20", dateNaissance)
        lbErreur.config(text="")
        return annee
    except:
        getErreur()

#######################
# Fonction permettant de recuperer le genre
# Entree: VIDE
# Sortie: String
# ######################
def setGenre():
    if estUnHomme():
        return "Homme"
    if estUneFemme():
        return "Femme"
    getErreur()
    return ""

#######################
# Fonction qui recrée l'année de naissance
# Entree:int, int
# Sortie: String
# ######################
def setAnnee(an, dateNaissance):
    return str(an)+str(dateNaissance.get())

def anneeInferieurAnneeActuelleRetraite():
    try:
        lbErreur.config(text="")
        return int(eDateNaissance.get()) < 21 and retraite.get() == 1
    except:
        getErreur()

def getErreur():
    lbErreur.config(text="Une erreur est survenue. Veuillez saisir tous les champs correctement")

def anneeInferieurAnneeActuellePasRetraite():
    try:
        lbErreur.config(text="")
        return int(eDateNaissance.get()) < 21 and retraite.get() == 0
    except:
        getErreur()

def anneeSuperieurAnneeActuelle():
    try:
        lbErreur.config(text="")
        return int(eDateNaissance.get()) > 21
    except:
        getErreur()

def estUnHomme():
    return eSexe.get() == "1"

def estUneFemme():
    return eSexe.get() == "2"

def toucheEntreePresse(touche):
    return touche == 'Return'

#######################
# Fonction permettant de créer la fenetre principale de l'application
# Entree: VIDE
# Sortie: VIDE
# ######################
def CreateurFenetreSaisi():
    fenetreSaisi = Tk()
    fenetreSaisi.title("Jerry Vital - Saisi de numéro")
    fenetreSaisi.geometry("800x600+500+175")
    fenetreSaisi.resizable(False,False)
    fenetreSaisi.configure(bg="#F9F8F4")
    fenetreSaisi.iconbitmap('logo_app.ico')
    return fenetreSaisi

if __name__ == '__main__':
    fenetreSaisi = CreateurFenetreSaisi()

    # Affichage du logo
    ecran = Canvas(fenetreSaisi, bg="#F9F8F4", width=593, height=186, highlightthickness=0)
    ecran.place(x=100, y=50)
    Logo = PhotoImage(file="Logo.PNG")
    ecran.create_image(0, 0, anchor=NW, image=Logo)

    lbDemande = Label(fenetreSaisi, text="Saisissez votre numéro de sécurité social", fg="#240747", bg="#F9F8F4", font="Verdana")
    lbDemande.place(x=255, y=275)

    lbInfo = Label(fenetreSaisi, text="Ce logiciel traduit votre numéro de sécurité social en informations claires, \n dans aucun cas les informations seront enregistrées et revendues à une tiers \n personne morale ou physique.", fg="#240747", bg="#F9F8F4",font="Verdana", anchor=CENTER)
    lbInfo.place(x=75, y=450)

    lbErreur = Label(fenetreSaisi, text="", fg="red", bg="#F9F8F4",font="Verdana", anchor=CENTER)
    lbErreur.place(x=125, y=250)
    # Champ de saisi
    retraite = int()

    eSexe = Entry(fenetreSaisi, width=1, bg="#F9F8F4", bd=5, relief=GROOVE, font="Verdana", fg="#240747")
    eSexe.place(x=295, y=300)

    eDateNaissance = Entry(fenetreSaisi, width=2, bg="#F9F8F4", bd=5, relief=GROOVE, font="Verdana", fg="#240747")
    eDateNaissance.place(x=320, y=300)

    eMois = Entry(fenetreSaisi, width=2, bg="#F9F8F4", bd=5, relief=GROOVE, font="Verdana", fg="#240747")
    eMois.place(x=355, y=300)

    eDepartement = Entry(fenetreSaisi, width=2, bg="#F9F8F4", bd=5, relief=GROOVE, font="Verdana", fg="#240747")
    eDepartement.place(x=390, y=300)

    eVille = Entry(fenetreSaisi, width=3, bg="#F9F8F4", bd=5, relief=GROOVE, font="Verdana", fg="#240747")
    eVille.place(x=425, y=300)

    eNe = Entry(fenetreSaisi, width=3, bg="#F9F8F4", bd=5, relief=GROOVE, font="Verdana", fg="#240747")
    eNe.place(x=470, y=300)

    Entry(fenetreSaisi, width=2, bg="#F9F8F4", bd=5, relief=GROOVE, font="Verdana", fg="#240747").place(x=515, y=300)

    retraite = IntVar()
    cbRetraite = Checkbutton(fenetreSaisi, text="Je suis à la retraite", bg="#F9F8F4",fg="#240747",activebackground="#F9F8F4", activeforeground="#240747", variable=retraite)
    cbRetraite.place(x=355, y=345)

    Button(fenetreSaisi, text="Valider",font="verdana",fg="#240747", command=enginer).place(x=375, y=400)

    fenetreSaisi.mainloop()