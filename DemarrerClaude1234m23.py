#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:51:03 2021

@author: toor
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 22:18:00 2021

@author: Paradoxe
"""
import os
import glob
from tkinter import *
import psycopg2
from tkinter import messagebox
import random
import time
from datetime import date, datetime
import matplotlib.pyplot as plt
import matplotlib
import random as rd
rouge="000"
rouge2="000"
vert="000"
vert2="000"
bleu="000"
bleu2="000"

print(rouge, vert, bleu)

    
DATABASE = "paradoxe2"   #nom de la base de donnée
USER = "paradoxe"          #propriétaire de la bd
PASSWORD = "paradoxe"         # mot de passe d'accès
HOST = "localhost"        #adresse ip du serveur, ici on est en local
    

        #Établissement de la connexion . Création du curseur"
try:
    con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
       
except Exception as err:
    print('La connexion a la base de donnée a échoué : \n'\
              'Erreur détecté :\n%s' % err)
    echec =1
else:
    cursor = con.cursor()  #création du curseur
    echec =0
            
if echec:
    sys.exit()

prixtt=0
parametre =1
produitlist = []
quantitelist = []
prixlist = []
numero_produit=[]
listeNumBonCmd=[]
remplirListboxAffiche=[]
num_caissier=27


if os.path.isdir('color'):
    #pass
    print("heureux")
else:
    os.mkdir("color")

f1=open("color/primitive.txt","r")
couleur=f1.read()
couleur=couleur.split("\n")

rouge=couleur[0]
vert=couleur[1]
bleu=couleur[2]
rouge2=couleur[3]
vert2=couleur[4]
bleu2=couleur[5]

nomInsert=""
prenomInsert=""
telInsert=""
adrINsert=""

class Eleonor(Tk):#Accueil

    
    
    
    def __init__(self):
        
        
        Tk.__init__(self)
        
        
        
        self.title("                                                                                                                                Eleonor")
        self.geometry("910x534+180+80")
        self.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        
        self.resizable(False, False)
        
        canfAcc=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleoc.png")
        canfAcc.create_image(0,0,anchor=NW,image=self.img)
        canfAcc.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        canfAcc.place(x=-1.5,y=-1.7)
        
        """self.imgClient = PhotoImage(file="images/demarrer1.png")
        boutonClient = Button(canfAcc, image=self.imgClient, cursor="hand2",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground = "black",border=0,
                              command=self.menu)
        boutonClient.place(x=385, y=190)
        client_label = Label(canfAcc, text= "Commencer une nouvelle session ", font=("arial", 10,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        client_label.place(x=357, y=340)"""
        canfAcc.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        #client_label.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        #boutonClient.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        
        menubar = Menu(self)
        
        cesarmenu = Menu(menubar, tearoff=0)
        cesarmenu.add_command(label="Ouvrir", command=self.menu)
        cesarmenu.add_command(label="Quitter", command=self.destroy)
        cesarmenu.add_separator()
        menubar.add_cascade(label="Menu", menu=cesarmenu)
        self.config(menu=menubar)
        
        
        """vigmenu = Menu(menubar, tearoff=0)
        vigmenu.add_command(label="Commencer", command=self.client)
        vigmenu.add_command(label="Exit", command=self.client)
        vigmenu.add_separator()
        menubar.add_cascade(label="ViginèreCipher", menu=vigmenu)
        
        
        dansmenu = Menu(menubar, tearoff=0)
        dansmenu.add_command(label="Commencer", command=self.client)
        dansmenu.add_command(label="Exit", command=self.client)
        dansmenu.add_separator()
        menubar.add_cascade(label="Dancing-men Cipher", menu=dansmenu)"""
        
        
    def menu(self):
        global nomInsert
        global prenomInsert
        global telInsert
        global adrINsert
        nomInsert=""
        prenomInsert=""
        telInsert=""
        adrINsert=""
        
        self.title("                                                                                     Eleonor")
        self.geometry("910x534+180+80")
        self.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        self.resizable(False, False)
        
        canfAcc=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleoc.png")
        canfAcc.create_image(0,0,anchor=NW,image=self.img)
        canfAcc.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        canfAcc.place(x=-1.5,y=-1.7)
        
        labelNavigation = Label(canfAcc, text= "^ Cliquer sur un des onglets du menu pour démarrer ^ ", font=("arial", 10,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        labelNavigation.place(x=5, y=5)
        
        
        """self.imgClient = PhotoImage(file="images/client.png")
        boutonClient = Button(canfAcc, image=self.imgClient, cursor="hand2",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground = "black",border=0,
                              command=self.client)
        boutonClient.place(x=85, y=190)
        client_label = Label(canfAcc, text= "Client ", font=("arial", 10,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        client_label.place(x=127, y=350)
        
        self.imgstat = PhotoImage(file="images/caissier.png")
        boutonCaissier = Button(canfAcc, image=self.imgstat, cursor="hand2",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground = "black",border=0,
                            command=self.caissiers)
        boutonCaissier.place(x=240, y=190)
        caissier_label = Label(canfAcc, text= "Caissier ", font=("arial", 10,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        caissier_label.place(x=280, y=350)
        
        
        self.imgrespo = PhotoImage(file="images/responsable.png")
        boutonRespo = Button(canfAcc, image=self.imgrespo, cursor="hand2",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground = "black",border=0,
                             command=self.responsables)
        boutonRespo.place(x=400, y=190)
        respo_label = Label(canfAcc, text= "Responsables ", font=("arial", 10,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        respo_label.place(x=425, y=350)
        
        
        self.imgParam = PhotoImage(file="images/parametres.png")
        boutonParam = Button(canfAcc, image=self.imgParam, cursor="hand2",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground = "black",border=0,
                             command=self.parametres)
        boutonParam.place(x=560, y=190)
        param_label = Label(canfAcc, text= "Paramètres ", font=("arial", 10,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        param_label.place(x=590, y=350)
        
        
        
        self.imgoperateur = PhotoImage(file="images/operateur.png")
        boutonOperateur = Button(canfAcc, image=self.imgoperateur, cursor="hand2",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground = "black",border=0)
        boutonOperateur.place(x=720, y=190)
        operateur_label = Label(canfAcc, text= "Operateur ", font=("arial", 10,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        operateur_label.place(x=760, y=350)"""
        
        menubar = Menu(self)
        
        clientmenu = Menu(menubar, tearoff=0)
        clientmenu.add_command(label="Explorer", command=self.client)
        #clientmenu.add_command(label="Exit", command=self.destroy)
        clientmenu.add_separator()
        menubar.add_cascade(label="Client", menu=clientmenu)
        
        
        caissiermenu = Menu(menubar, tearoff=0)
        caissiermenu.add_command(label="Explorer", command=self.caissiers)
        #caissiermenu.add_command(label="Exit", command=self.client)
        caissiermenu.add_separator()
        menubar.add_cascade(label="Caissier", menu=caissiermenu)
        
        
        """responsablesmenu = Menu(menubar, tearoff=0)
        responsablesmenu.add_command(label="Explorer", command=self.responsables)
        #responsablesmenu.add_command(label="Exit", command=self.client)
        responsablesmenu.add_separator()
        menubar.add_cascade(label="Responsables", menu=responsablesmenu)"""
        
        
        parametremenu = Menu(menubar, tearoff=0)
        parametremenu.add_command(label="Ouvrir", command=self.parametres)
        #parametremenu.add_command(label="Exit", command=self.client)
        parametremenu.add_separator()
        menubar.add_cascade(label="Paramètres", menu=parametremenu)
        
        parametremenu = Menu(menubar, tearoff=0)
        parametremenu.add_command(label="Cette option est indisponible pour le moment")
        #parametremenu.add_command(label="Exit", command=self.client)
        parametremenu.add_separator()
        menubar.add_cascade(label="Opérateur", menu=parametremenu)
        self.config(menu=menubar)
        
        canfAcc.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        """boutonClient.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        client_label.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        boutonCaissier.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        caissier_label.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        boutonRespo.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        respo_label.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        boutonParam.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        param_label.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        boutonOperateur.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        operateur_label.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")"""
        labelNavigation.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        
        
        
        
#======================ARBORESCENCE DU CLIENT =====================================


    def client(self):
        global rouge
        global vert 
        global bleu
        global entryNomCl
        global entryPrenomCl
        global entryTelCl
        global entryadrCl
        
        
        
        
        self.title("                                                                                                                                Eleonor")
        self.geometry("910x534+180+80")
        self.resizable(False,False)
        
        
        caninCl=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        caninCl.create_image(0,0,anchor=NW,image=self.img)
        caninCl.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        
        caninCl.place(x=-2,y=-1.7)
        
        self.photoprecedent = PhotoImage(file="images/icprec1.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="black",cursor="hand2",
                        command=self.menu)
        btprec.place(x=10,y=10)
        
        infoCl = Label(caninCl, font=('harrington', 35, 'bold'),bd=0, text="Informations générales", fg="aqua", bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        infoCl.place(x=210,y=52)
        
        
        nomCl = Label(self, font=('harrington', 20, 'bold'), text="Noms:", padx=1,fg="gold", bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        nomCl.place(x=165,y=160)
        entryNomCl = Entry(caninCl, font=('harrington', 20, 'bold'), width=20)
        entryNomCl.insert(END,nomInsert )
        entryNomCl.place(x=320, y=162)
        
        prenomCl = Label(caninCl, font=('harrington', 20, 'bold'), text="Prenoms:", padx=1,fg="gold", bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        prenomCl.place(x=165, y=210)
        entryPrenomCl = Entry(caninCl, font=('harrington', 20, 'bold'), width=20)
        entryPrenomCl.insert(END, prenomInsert)
        entryPrenomCl.place(x=320, y=212)
                
        telCl = Label(caninCl, font=('harrington', 20, 'bold'), text="Téléphone:", padx=1,fg="gold", bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        telCl.place(x=165, y=260)
        entryTelCl = Entry(caninCl, font=('harrington', 20, 'bold'), width=20)
        entryTelCl.insert(END, telInsert)
        entryTelCl.place(x=320, y=262)
                
        adrCl = Label(caninCl, font=('harrington', 20, 'bold'), text="Addresse:", padx=1,fg="gold", bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        adrCl.place(x=165, y=310)
        entryadrCl = Entry(caninCl, font=('harrington', 20, 'bold'), width=20)
        entryadrCl.insert(END, adrINsert)
        entryadrCl.place(x=320, y=312)
        
        self.imchSui=PhotoImage(file="images/btsuivCl.png")
        boutonSui= Button(self, image=self.imchSui, bd=-2,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"", activebackground="black",command=self.ajouter)
        boutonSui.place(x=360, y=350)
        """boutonSui= Button(self, image=self.imchSui, bd=-2,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"", activebackground="black",command=self.migrationVersProduitUpdate)
        boutonSui.place(x=360, y=350)"""
        
        caninCl.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        btprec.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        infoCl.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        nomCl.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        prenomCl.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        telCl.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        adrCl.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        boutonSui.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        
        
        menubar = Menu(self)
        
        cesarmenu = Menu(menubar, tearoff=0)
        cesarmenu.add_command(label="Ouvrir", command=self.menu)
        cesarmenu.add_command(label="Quitter", command=self.destroy)
        cesarmenu.add_separator()
        menubar.add_cascade(label="Menu", menu=cesarmenu)
        self.config(menu=menubar)
        
        """menubar = Menu(self)
        
        cesarmenu = Menu(menubar, tearoff=0)
        cesarmenu.add_command(label="Commencer", command=self.client)
        cesarmenu.add_command(label="Exit", command=self.destroy)
        cesarmenu.add_separator()
        menubar.add_cascade(label="prduits", menu=cesarmenu)
        
        
        vigmenu = Menu(menubar, tearoff=0)
        vigmenu.add_command(label="Commencer", command=self.client)
        vigmenu.add_command(label="Exit", command=self.client)
        vigmenu.add_separator()
        menubar.add_cascade(label="bon de commande", menu=vigmenu)
        
        
        dansmenu = Menu(menubar, tearoff=0)
        #dansmenu.add_command(label="Commencer", command=self.client)
        dansmenu.add_command(label="Exit", command=self.client)
        dansmenu.add_separator()
        menubar.add_cascade(label="sortie", menu=dansmenu)
        self.config(menu=menubar)"""
    def ajouter(self):
        
        global nomInsert
        global prenomInsert
        global telInsert
        global adrINsert
        global numclient
        
        nomInsert= entryNomCl.get()
        prenomInsert = entryPrenomCl.get()
        telInsert = entryTelCl.get()
        adrINsert = entryadrCl.get()        
        
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("SELECT num_client FROM Clients")
        rows = cursor.fetchall()
        numclient= random.randint(0,10000)
        for row in rows:
            print (row[0])
            while row[0] == numclient:
                numclient= random.randint(0,10000)

        print(nomInsert)
        print(telInsert)
        print(numclient)
        
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("select nom_client, tel_client from clients")
                       
        client = cursor.fetchall()
       
        if nomInsert =='' or telInsert=='':
            messagebox.showerror("Gestion des clients", "Tous les champs ne sont pas renseignée.")
        else:
            for row in client:
                if row[0]==nomInsert and row[1]==telInsert:
                    self.clientAppelProduits()
                
            con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
            cursor = con.cursor()
            cursor.execute("INSERT INTO Clients (num_client, nom_client, tel_client) VALUES ('" + str(numclient) + "', '" + str(nomInsert) + "', '" + str(telInsert) +"')")
            con.commit()
            con.close() 
            self.clientAppelProduits()
        
    def client2(self):
            
        Eleonor.client(self)
        """self.photoSuivant = PhotoImage(file="images/icsuiv1.png")
        boutonSuivant = Button(self,image=self.photoSuivant, bd=-5, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="black",cursor="hand2",
                        command=self.migrationVersProduitUpdate)
        boutonSuivant.place(x=810,y=500)"""
        
        self.imchSui=PhotoImage(file="images/btsuivCl.png")
        boutonSui= Button(self, image=self.imchSui, bd=-2,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"", activebackground="black",command=self.migrationVersProduitUpdate)
        boutonSui.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonSui.place(x=540, y=350)
        
        menubar = Menu(self)
        
        cesarmenu = Menu(menubar, tearoff=0)
        cesarmenu.add_command(label="Retour au menu", command=self.menu)
        cesarmenu.add_separator()
        menubar.add_cascade(label="Menu", menu=cesarmenu)
        
        cesarclient = Menu(menubar, tearoff=0)
        cesarclient.add_command(label="Retour à la page des produit", command=self.migrationVersProduitUpdate)
        cesarclient.add_separator()
        menubar.add_cascade(label="Produits", menu=cesarclient)
        
        
        self.config(menu=menubar)
        
        
        
        
    def clientAppelProduits(self):
        
        global nomInsert
        global prenomInsert
        global telInsert
        global adrINsert
        
        nomInsert= entryNomCl.get()
        prenomInsert = entryPrenomCl.get()
        telInsert = entryTelCl.get()
        adrINsert = entryadrCl.get()
        #global btprec
        print("okay",nomInsert)
        Eleonor.produits(self)
        self.photoprecedent = PhotoImage(file="images/icprec1.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="black",cursor="hand2",
                        command=self.client2)
        btprec.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        btprec.place(x=920,y=10)
        print(nomInsert)
        
        menubar = Menu(self)
        
        cesarmenu = Menu(menubar, tearoff=0)
        cesarmenu.add_command(label="Retour au menu", command=self.menu)
        cesarmenu.add_separator()
        menubar.add_cascade(label="Menu", menu=cesarmenu)
        
        cesarclient = Menu(menubar, tearoff=0)
        cesarclient.add_command(label="Retour aux informations client", command=self.client2)
        cesarclient.add_separator()
        menubar.add_cascade(label="Client", menu=cesarclient)
        
        
        self.config(menu=menubar)
        
    def produitCaissier(self):
        
        global rouge
        global vert 
        global bleu
        
        
       
        
        
        Tk.destroy(self)
        Tk.__init__(self)
        self.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        self.geometry("1000x670+100+10")
        self.resizable(False,False)
        can=Canvas(self, width=900,heigh=620)
        can.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        can.place(x=0,y=20)
        #can.grid()
        
        
        
        canvas = Canvas(can,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",width=540,height=640)#c'est ici que tu peux modifier la taille du tableau de produit
        
        scroll_y = Scrollbar(can, orient="vertical", command=canvas.yview)
        entête = ["Numero","Nom","Prix"]
        indice=0
        
        
        frame = Frame(canvas,width=540,height=540,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        # labels presents dans le frame scrollable
        tab=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER,PASSWORD))
        cursor=tab.cursor()
        cursor.execute("SELECT * FROM produits")
        rows=cursor.fetchall()
        tab.close()
        #print(rows)
        for i in entête:
            indice+=1   
            libelle = Label(self,text=i,bd=0.5,bg="gold",relief=RIDGE,width=26)
            libelle.grid(row=0,column=indice,sticky=NSEW)
        
        

        def fond(e):
            global imgp
           
            #a=int(num_produit.get())
            #self.canphoto=Canvas(obj, width=200,height=200)
            imgp=PhotoImage(file="images/prod"+str(e)+".png")
            self.canphoto.itemconfigure("img_fond",image=imgp)
            global parametre
            parametre = e
            print(parametre)
        
            
        listeNumero=[]
        for groupe in rows:
            listeNumero+=[groupe[0]]
                
            #print(listeNumero)
                
        listeNom=[]
        for groupe in rows:
            listeNom+=[groupe[1]]
            #print(listeNom)
            
        listePrix=[]
        for groupe in rows:
            listePrix+=[groupe[2]]
                #print(listePrix)
                    
        numero=dict()
        i=0
        while(i<len(listeNumero)): 
                
            numero[i] = Button(frame,text=listeNumero[i],bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold",cursor="hand2",bd=0.5,width=25)
            numero[i].config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
            numero[i].grid(row=i+1,column=1,sticky=NSEW)
                    
            i+=1
                    
        
                 
                #for indice in range(len(listeNom)):
                   # for element in listeNom
         
        
        nom=dict()  
        i=0
        while(i<len(listeNom)):
            nom[i] = Button(frame,text=listeNom[i],bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold", cursor="hand2",bd=0.5,width=25)
            nom[i].config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
            nom[i].grid(row=i+1,column=2,sticky=NSEW)
            i+=1
                        
        itemList=[]        
        for item in listeNumero:
            numero[listeNumero.index(item)].config(command = lambda z=item: fond(z)) 
            itemList.append(item)
            nom[listeNumero.index(item)].config(command = lambda z=item: fond(z))                
                
                #print(numero[listeNumero.index(item)])    
        i=0
        while(i<len(listePrix)):
            prix = Label(frame,text=str(listePrix[i])+" FCFA",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold", relief=RAISED,bd=0.5,width=25)
            prix.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
            prix.grid(row=i+1,column=3,sticky=NSEW)
            i+=1
    
       # insersion du frame dans le canvas
        canvas.create_window(100, 100, anchor='nw', window=frame)
        # on s'assure que tous sera affiché avant de définir la scrollregion
        canvas.update_idletasks()
        
        canvas.configure(scrollregion=canvas.bbox('all')#c'est cette commande qui s'assure de la presence, 
                         ,yscrollcommand=scroll_y.set)
                         
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')
        
        self.canphoto=Canvas(self, width=200,height=200)
               
        self.imgp= PhotoImage(file="images/nature.png") 
        self.canphoto.create_image(2,2, anchor=NW, image=self.imgp, tags="img_fond")
        self.canphoto.place(x=660,y=270)
        

        
    def produits(self):
        
        global rouge
        global vert 
        global bleu
        
        
       
        
        
        Tk.destroy(self)
        Tk.__init__(self)
        self.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        self.geometry("1000x670+100+10")
        self.resizable(False,False)
        can=Canvas(self, width=900,heigh=620)
        can.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        can.place(x=0,y=20)
        #can.grid()
        
        
        
        canvas = Canvas(can,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",width=540,height=640)#c'est ici que tu peux modifier la taille du tableau de produit
        
        scroll_y = Scrollbar(can, orient="vertical", command=canvas.yview)
        entête = ["Numero","Nom","Prix"]
        indice=0
        
        
        frame = Frame(canvas,width=540,height=540,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        # labels presents dans le frame scrollable
        tab=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER,PASSWORD))
        cursor=tab.cursor()
        cursor.execute("SELECT * FROM produits")
        rows=cursor.fetchall()
        tab.close()
        #print(rows)
        for i in entête:
            indice+=1   
            libelle = Label(self,text=i,bd=0.5,bg="gold",relief=RIDGE,width=26)
            libelle.grid(row=0,column=indice,sticky=NSEW)
        
        

        def fond(e):
            global imgp
           
            #a=int(num_produit.get())
            #self.canphoto=Canvas(obj, width=200,height=200)
            imgp=PhotoImage(file="images/prod"+str(e)+".png")
            self.canphoto.itemconfigure("img_fond",image=imgp)
            global parametre
            parametre = e
            print(parametre)
        
            
        listeNumero=[]
        for groupe in rows:
            listeNumero+=[groupe[0]]
                
            #print(listeNumero)
                
        listeNom=[]
        for groupe in rows:
            listeNom+=[groupe[1]]
            #print(listeNom)
            
        listePrix=[]
        for groupe in rows:
            listePrix+=[groupe[2]]
                #print(listePrix)
                    
        numero=dict()
        i=0
        while(i<len(listeNumero)): 
                
            numero[i] = Button(frame,text=listeNumero[i],bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold",cursor="hand2",bd=0.5,width=25)
            numero[i].config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
            numero[i].grid(row=i+1,column=1,sticky=NSEW)
                    
            i+=1
                    
        
                 
                #for indice in range(len(listeNom)):
                   # for element in listeNom
         
        
        nom=dict()  
        i=0
        while(i<len(listeNom)):
            nom[i] = Button(frame,text=listeNom[i],bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold", cursor="hand2",bd=0.5,width=25)
            nom[i].config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
            nom[i].grid(row=i+1,column=2,sticky=NSEW)
            i+=1
                        
        itemList=[]        
        for item in listeNumero:
            numero[listeNumero.index(item)].config(command = lambda z=item: fond(z)) 
            itemList.append(item)
            nom[listeNumero.index(item)].config(command = lambda z=item: fond(z))                
                
                #print(numero[listeNumero.index(item)])    
        i=0
        while(i<len(listePrix)):
            prix = Label(frame,text=str(listePrix[i])+" FCFA",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold", relief=RAISED,bd=0.5,width=25)
            prix.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
            prix.grid(row=i+1,column=3,sticky=NSEW)
            i+=1
    
       # insersion du frame dans le canvas
        canvas.create_window(100, 100, anchor='nw', window=frame)
        # on s'assure que tous sera affiché avant de définir la scrollregion
        canvas.update_idletasks()
        
        canvas.configure(scrollregion=canvas.bbox('all')#c'est cette commande qui s'assure de la presence, 
                         ,yscrollcommand=scroll_y.set)
                         
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')
        
        self.canphoto=Canvas(self, width=200,height=200)
               
        self.imgp= PhotoImage(file="images/nature.png") 
        self.canphoto.create_image(2,2, anchor=NW, image=self.imgp, tags="img_fond")
        self.canphoto.place(x=660,y=20)
                
        labelquantite1 = Label(self, font=('arial', 12, 'bold'), text="Quantité: ", fg="gold", bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelquantite1.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelquantite1 .place(x=680,y=250)
        self.quantite = Entry(self, font=('arial', 14, 'bold'), width=3,bd=5)
        self.quantite.place(x=790,y=245)
            
        labelquantite2 = Label(self, font=('arial', 7, 'bold'), text="Indiquer \nla quantité achetée \navant de valider ", fg="green", bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelquantite2.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelquantite2 .place(x=710,y=280)
        
        self.photoValider = PhotoImage(file="images/validerprod.png")
        boutonValider = Button(self,image=self.photoValider, border = 0, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="black",cursor="hand2" ,command = self.valider)
        boutonValider.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonValider.place(x=700,y=320)
                
        self.photoconclure = PhotoImage(file="images/conclure.png")
        boutonconclure = Button(self,image=self.photoconclure, border = 0, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="black",cursor="hand2" ,command = self.bonCommande )
        boutonconclure.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonconclure.place(x=700,y=610)
        
        """self.photoprecedent = PhotoImage(file="images/icprec1.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="black",cursor="hand2",
                        command=self.client)
        btprec.place(x=920,y=10)"""
                    
        frameValide=Frame(self,width=240,height=240,bd=-3)
        frameValide.place(x=620,y=390)
                
        scrollbar=Scrollbar(frameValide)
        scrollbar.pack(side=RIGHT, fill=Y)
                
        self.photoachat = PhotoImage(file="images/listeachat1.png")
        label= Label(frameValide,image=self.photoachat)
        label.pack()
                
        self.listboxaffiche=Listbox(frameValide,width=40,height=11,yscrollcommand=scrollbar.set)
        self.listboxaffiche.pack(side=LEFT, fill = BOTH)
        scrollbar.config(command=self.listboxaffiche.yview)
        
        

    
        
            
    def valider(self):
        global prixtt
        global produitlist
        global quantitelist
        global prixlist
        global numero_produit
        global prix_nom_affiche
        global remplirListboxAffiche
        global numclient
        
            
        quant= int(self.quantite.get())
        
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("SELECT  nom_produit, prix_produit FROM Produits WHERE num_produit=%s" %(parametre))
        rows = cursor.fetchall()
        #print(rows)
        #con.close()
        nom_affiche=str(rows[0][0])
        prixprod = rows[0][1]
        cursor.execute("SELECT prix_produit FROM produits WHERE num_produit=%s" %(parametre))
        rowprix = cursor.fetchone()
        #print(rowprix[0])
            
        prixU=rowprix[0]
        prixT=prixU*quant
        prixtt+=prixT
                    
        
        prix_affiche=str(rows[0][1])
        prix_nom_affiche=str(quant)+" "+nom_affiche+" pour "+prix_affiche+" FCFA l'unité"
        
        remplirListboxAffiche+=[prix_nom_affiche]
        self.listboxaffiche.insert(END, prix_nom_affiche)
        prix = quant*int(prix_affiche)
        print (prix)
        print(prixT)
        print(prixtt)
        print("nous avons",remplirListboxAffiche)
        
        produitlist.append(nom_affiche)
        quantitelist.append(quant)
        prixlist.append(prixprod)
        numero_produit.append(parametre)
                    
        print(produitlist)
        print(quantitelist)
        print(prixlist)
        print(numero_produit)
        self.quantite.delete(0,END)              
                    
        """tupl=listboxaffiche.get('@1,0', END)
        #print (tupl, tupl[0])
        liste=list(tupl) 
        divis = liste[0].split(" ")
        #print(divis, divis[0], divis[1], divis[2]  )"""
        
    def bonCommande(self):
        
        global numclient
        global num_facture
        
                
        
        x=random.randint(1000,9999)
        num_facture = x
       
        
        self.title("                                                                                                                                Eleonor")
        self.geometry("1010x642+140+20")
                
                
        self.canfond=Canvas(self, width=1025,height=655)
        self.img=PhotoImage(file="images/imeleobfact.png")
        self.canfond.create_image(0,0,anchor=NW,image=self.img)
        self.canfond.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        self.canfond.place(x=-2,y=-1.7)
        
        self.photoprecedent = PhotoImage(file="images/icprec1.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="black",cursor="hand2",
                        command=self.migrationVersProduitUpdate)
        btprec.place(x=10,y=10)
        
        """self.photoprecedent = PhotoImage(file="images/icprec1.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="black",cursor="hand2",
                        command=self.clientAppelProduits)"""
        
        
        
        
                
                
                                                
                                                
                                                #==================================frames===============================
                                                            
        DataFrame = Frame(self, bd=-1, width=10, height=50, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        DataFrame.place(x=160,y=140)
                
        titre = Label(self.canfond, font=('arial', 30, 'bold'), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold", text="Bon de commande final")
        titre.place(x=210,y=40)
        scrolf = Scrollbar(DataFrame, orient=VERTICAL)
        self.txtarea = Text(DataFrame, yscrollcommand=scrolf.set)
        #DataFrame.config(scrollregion=DataFrame.bbox('all'),yscrollcommand=scrolf.set)
        scrolf.pack(side=RIGHT,fill=Y)
        scrolf.config(command=self.txtarea.yview())
        self.txtarea.pack(side=BOTTOM, fil=BOTH)
                                     
    
        self.txtarea.insert(END, "\t\t\t\t\t     "+time.strftime("%A %d %B %Y %H:%M:%S"))
        #self.txtarea.insert(END, "\n\n  \t\t\t\tBoutique Numero" + str(numBoutique))
        self.txtarea.insert(END, "\n\n================================================================================")            
        self.txtarea.insert(END, "\n\n  Bon de commande N° : "+str(num_facture))
        self.txtarea.insert(END, "\n  Numero du client : "+str(numclient))
        self.txtarea.insert(END, "\n  Nom  et prenom du client : "+str(nomInsert+" "+prenomInsert))
        self.txtarea.insert(END, "\n  Coordonnées : "+str(telInsert+" "+adrINsert))
        #self.txtarea.insert(END, "\n  Numero du caissiers : 000"+str(numcaissier))
        self.txtarea.insert(END, "\n\n================================================================================")
        self.txtarea.insert(END, "\n  Ref")
        self.txtarea.insert(END, "\t  Produits")
        self.txtarea.insert(END, "\t\t  Quantité")
        self.txtarea.insert(END, "\t\t Prix Unitaire ")
        self.txtarea.insert(END, "\n================================================================================")
        i = 0
        while(i<len(produitlist)):
           
            self.txtarea.insert(END, "\n  "+str(numero_produit[i]))
            self.txtarea.insert(END, "\t  "+produitlist[i])
            self.txtarea.insert(END, "\t\t    "+str(quantitelist[i]))
            self.txtarea.insert(END, "\t\t   "+str(prixlist[i])+"FCFA")
            i+=1
            
            
            
        self.txtarea.insert(END, "\n\n\n\tPrix total : "+str(prixtt)+" FCFA"  )
        
        
        """self.photoprecedent = PhotoImage(file="images/icprec1.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="black",cursor="hand2",
                        command=self.produits)"""
        #btprec.place(x=10,y=10)
         
        """self.butImprimer = Button(self, text="Imprimer",font=('arial', 30, 'bold'),bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold", command = self.imprimer)
        self.butImprimer.place(x=547, y=540)"""
        
        self.photoEnregistrer = PhotoImage(file="images/enregistrer.png")
        butImprimer = Button(self,image=self.photoEnregistrer, bd=-5, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",
                        activebackground="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",cursor="hand2",
                        command=self.imprimer)
        butImprimer.place(x=707, y=540)
        
        
        menubar = Menu(self)
        
        cesarmenu = Menu(menubar, tearoff=0)
        cesarmenu.add_command(label="Retour au menu", command=self.menu)
        cesarmenu.add_separator()
        menubar.add_cascade(label="Menu", menu=cesarmenu)
        
        cesarclient = Menu(menubar, tearoff=0)
        cesarclient.add_command(label="Retour aux informations client", command=self.client2)
        cesarclient.add_separator()
        menubar.add_cascade(label="Client", menu=cesarclient)
        
        cesarproduits = Menu(menubar, tearoff=0)
        cesarproduits.add_command(label="Retour a la page des produits", command=self.migrationVersProduitUpdate)
        cesarproduits.add_separator()
        menubar.add_cascade(label="Produits", menu=cesarproduits)
        
        
        self.config(menu=menubar)
        
    def imprimer(self):
        
        question = messagebox.askyesno("Enregistrement","Voulez vous enregistrer le bon de commande?")
        if question > 0:
            self.data = self.txtarea.get("1.0","end-1c")
            if os.path.isdir('factures'):
                #pass
                print("heureux")
            else:
                os.mkdir("factures")
                print("joyeux")
                
            print("sa continu?")
            a=f'{datetime.now():%d-%m-%Y %H:%M}'
            f1=open("Facture du "+str(a)+".txt", "w")
            f1.write(self.data) 
            f1.close
            tab=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER,PASSWORD))
            cursor=tab.cursor()
            cursor.execute("INSERT INTO Factures (num_facture, prix_total,date, num_client,num_caissier) VALUES ('"+str(num_facture)+"', '"+str(prixtt)+"', '"+str(datetime.now())+"', '"+str(numclient)+"', '"+str(num_caissier)+"')")
            #cursor.execute("INSERT INTO Factures (num_facture, prix_total,date, num_client,num_caissier) VALUES ('"+str(self.num_facture)+"', '"+str(self.prixtt)+"', '"+'13-03-2021'+"', '"+str(self.numclient)+"', '"+str(self.num_caissier)+"')")
            messagebox.showinfo("Statut de la vente", "Bon de commande enregistré")
            
            tab.commit()
            tab.close()

            j = 0
            while (j<len(produitlist)):
                con=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER,PASSWORD))
                cursor=con.cursor()
                cursor.execute("INSERT INTO Contenir (quantite, prix_unitaire, num_produit, num_facture) VALUES ('"+str(quantitelist[j])+"','"+str(prixlist[j])+"', '"+str(numero_produit[j])+"', '"+str(num_facture)+"')")
                j+=1
                con.commit()
                con.close()
            Tk.destroy(self)
            Tk.__init__(self)
            self.menu()
                
        else:
            return
                
                
    def migrationVersProduitUpdate(self):
            
           
            print("la listbox est:",remplirListboxAffiche)
            Eleonor.produits(self)
            for elt in remplirListboxAffiche:
                self.listboxaffiche.insert(END, elt)
                
                
            self.photoprecedent = PhotoImage(file="images/icprec1.png")
            boutonSuivant = Button(self,image=self.photoprecedent, bd=-5, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="black",cursor="hand2",
                        command=self.client2)
            boutonSuivant.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
            boutonSuivant.place(x=910,y=10)
            print(nomInsert)
            
            menubar = Menu(self)
        
            cesarmenu = Menu(menubar, tearoff=0)
            cesarmenu.add_command(label="Retour au menu", command=self.menu)
            cesarmenu.add_separator()
            menubar.add_cascade(label="Menu", menu=cesarmenu)
            
            cesarclient = Menu(menubar, tearoff=0)
            cesarclient.add_command(label="Retour aux informations client", command=self.client2)
            cesarclient.add_separator()
            menubar.add_cascade(label="Client", menu=cesarclient)
            
            
            self.config(menu=menubar)
                
            

        
    def caissiers(self):
        
        self.title("                                                 Eleonor")
        self.geometry("540x320+430+270")
        self.resizable(False, False)
        
        
        can=Canvas(self, width=600,heigh=400)
        self.img=PhotoImage(file="images/noirx.png")
        can.create_image(340,120,image=self.img)
        can.place(x=-5,y=-2)
        
        self.photoinscrit= PhotoImage(file = "images/icprec1.png")
        boutonprecConx = Button(self,image = self.photoinscrit, bd=-2,bg="black",activebackground = "black", cursor="hand2",
                                command=self.menu)
        boutonprecConx.place(x=10,y=10)
        
        
        nom_label = Label(self, text= "Login", font=("harrington", 20), bg="black", fg="gold")
        nom_label.place(x=20, y=80)
        
        self.password_label = Label(self, text= "Password ", font=("harrington", 20), bg="black", fg="gold")
        self.password_label.place(x=20, y=150)
            
        
        self.nom_entry = Entry(self,bg = "white", font=("harrington", 20))
        self.nom_entry.place(x=150, y=80)
        
        self.password_entry = Entry(self, bg = "white",font=("harrington", 20),show="¤")
        self.password_entry.place(x=150, y=150)
        
        self.photoconnect = PhotoImage(file = "images/icconex1.png")
        add_button = Button(self,image = self.photoconnect, cursor="hand2",bg="black",activebackground = "black",border=0,command=self.connexion)
        add_button.place(x=134, y=210)
        
        menubar = Menu(self)
        
        cesarmenu = Menu(menubar, tearoff=0)
        cesarmenu.add_command(label="Ouvrir", command=self.menu)
        cesarmenu.add_command(label="Quitter", command=self.destroy)
        cesarmenu.add_separator()
        menubar.add_cascade(label="Menu", menu=cesarmenu)
        self.config(menu=menubar)
        
    def connexion(self):
            
        nom = self.nom_entry.get()
        num=self.password_entry.get()
        if (nom == "" or num == ""):
             messagebox.showerror("error", "veuillez remplir tous les champs")
        else:
             con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
             cursor = con.cursor()
             cursor.execute("select * from caissiers where nom_caissier=%s and password=%s",
                                (self.nom_entry.get(), self.password_entry.get()))
             row = cursor.fetchone()
             if row == None:
                 messagebox.showerror("error", "Ivalid USERNAME & PASSWORD")
             else:
                    self.pageCaissiers()
        
    def pageCaissiers(self):
        self.title("                                                                                     Eleonor")
        self.geometry("910x534+180+80")
        self.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        self.resizable(False, False)
    
        
        canpCais=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleoc.png")
        canpCais.create_image(0,0,anchor=NW,image=self.img)
        canpCais.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        canpCais.place(x=-1.2,y=-1.7) 
        self.photoinscrit= PhotoImage(file="images/icprec1.png")
        self.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        boutonprecCaiss = Button(canpCais,image = self.photoinscrit, bd=-2,
                                 bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",
                                 activebackground = "#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"", cursor="hand2",
                                command=self.menu)
        boutonprecCaiss.place(x=10,y=70)
        
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("SELECT num_caissier,nom_caissier FROM caissiers;")
        rows = cursor.fetchall()
        print(rows)
        
        for elt in rows:
            numero=elt[0]
            nom=elt[1]
        print(numero)   
        print(nom)
        
        canAff=Canvas(canpCais, width=50,height=50)
        self.img2=PhotoImage(file="images/caissier2.png")
        canAff.create_image(0,0,anchor=NW,image=self.img2)
        #canAff.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        canAff.place(x=10,y=5)
        
        caissier_label = Label(canpCais, text=nom+""+str(numero) , font=("arial", 10,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        caissier_label.place(x=70, y=5)
        caissier_statut = Label(self, text="statut : " , font=("arial", 9,), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        caissier_statut.place(x=70, y=30)
        
        caissier_statut2 = Label(self, text="Connecté... " , font=("arial", 9,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="aqua")
        caissier_statut2.place(x=110, y=30)
        
        
        menubar = Menu(self)
        
        ventemenu = Menu(menubar, tearoff=0)
        ventemenu.add_command(label="Etats des ventes", command= self.caissierAppelEGV)
        
        ventemenu.add_command(label="Exit", command=self.menu)
        ventemenu.add_separator()
        menubar.add_cascade(label="Ventes", menu=ventemenu)
        
        produitmenu = Menu(menubar, tearoff=0)
        """produitmenu.add_command(label="Nouveau")"""
        produitmenu.add_command(label="Lister",command=self.caissierAppelProduits)
        produitmenu.add_command(label="Exit", command=self.destroy)
        produitmenu.add_separator()
        menubar.add_cascade(label="Produits", menu=produitmenu)
        
        
        factmenu = Menu(menubar, tearoff=0)
        
        factmenu.add_command(label="Lister",command=self.listerFacture)
        factmenu.add_command(label="Exit", command=self.destroy)
        factmenu.add_separator()
        menubar.add_cascade(label="Factures", menu=factmenu)
        
        statmenu = Menu(menubar, tearoff=0)
        statmenu.add_command(label="Consulter les statistiques de vente",command=self.caissierAppelEGV)
        statmenu.add_separator()
        menubar.add_cascade(label="Statistiques", menu=statmenu)
        
        self.config(menu=menubar)
        
        canpCais.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        caissier_label.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        caissier_statut.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        caissier_statut2.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        boutonprecCaiss.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        
        
        
    def caissierAppelProduits(self):
        #global btprec
        #print(btprec)
        Eleonor.produitCaissier(self)
        self.photoprecedent = PhotoImage(file="images/icprec1.png")
        btprec = Button(self,image=self.photoprecedent, bd=-5, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",
                        activebackground="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",cursor="hand2",
                        command=self.pageCaissiers)
        
        btprec.place(x=940,y=10)
        
        
        
        
    def caissierAppelEGV(self):#EGV:etat general des ventes
        Eleonor.etatsGeneralVentes(self)
        self.photoPrec= PhotoImage(file="images/icprec1.png")
        boutonRetour = Button(self,image = self.photoPrec, bd=-2,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground = "black", cursor="hand2",
                                command=self.pageCaissiers)
        boutonRetour.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        boutonRetour.place(x=10,y=10)
        
    
    def listerFacture(self):
        
        listeNum_bon=[]
        
        
        
        
        self.title("¤¤¤¤¤¤¤¤¤¤¤¤• PRODUITS ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
        self.geometry("940x534+180+80")
        self.resizable(False,False)
        canFact=Canvas(self, width=945,height=540)
        """self.img=PhotoImage(file="images/imeleob.png")
        canFact.create_image(0,0,anchor=NW,image=self.img)"""
        canFact.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        canFact.place(x=-2,y=-1.7)
        self.photoPrec= PhotoImage(file="images/icprec1.png")
        boutonAcc = Button(canFact,image = self.photoPrec, bd=-2,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground = "black", cursor="hand2",
                                command=self.pageCaissiers)
        boutonAcc.place(x=10,y=10)
        
        frameValide=Frame(self,width=240,height=240,bd=-3)
        frameValide.place(x=670,y=45)
                
        scrollbar=Scrollbar(frameValide)
        scrollbar.pack(side=RIGHT, fill=Y)
                
        self.photoachat = PhotoImage(file="images/listeachat1.png")
        label= Label(frameValide,image=self.photoachat)
        label.pack()
        
        self.photoPrec1= PhotoImage(file="images/validefact.png")
        boutonRetour1 = Button(self,image = self.photoPrec1, bd=-2,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"", cursor="hand2")
        boutonRetour1.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground ="#"+rouge+""+vert+""+bleu+"" )
        boutonRetour1.place(x=730,y=400)


        def recuperer(event):
            self.txtarea.delete("1.0","end")
            line = self.listboxaffiche.curselection()[0]
            global item
            item = self.listboxaffiche.get(line)
            global selected_item
            
            selected_item = StringVar()
            selected_item.set(item) 
            f1=open(item, "r")
            donne = f1.read()
            print(donne)
            self.txtarea.insert(END, donne)

        
                
        self.listboxaffiche=Listbox(frameValide,width=40,height=16,yscrollcommand=scrollbar.set)
        self.listboxaffiche.bind('<<ListboxSelect>>', recuperer)
        self.listboxaffiche.pack(side=LEFT, fill = BOTH)
        scrollbar.config(command=self.listboxaffiche.yview)
        
        
        self.txtarea = Text(self, yscrollcommand=scrollbar.set)
        #DataFrame.config(scrollregion=DataFrame.bbox('all'),yscrollcommand=scrolf.set)
        scrollbar.pack(side=RIGHT,fill=Y)
        scrollbar.config(command=self.txtarea.yview())
        #self.txtarea.pack(side=LEFT, fil=X)
        self.txtarea.place(x=5,y=45)
           
        print(listeNum_bon)
        
        for file in glob.glob("factures/*.txt"):
            self.listboxaffiche.insert(END, file)
        
        canFact.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        boutonAcc.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
            
        
    
        
        
        
        
        
        
#=======================ARBORESCENCE DES RESPONSABLES=============================

        
    def etatsGeneralVentes(self):
        global rouge
        global vert 
        global bleu
        
        #self.__init__()
        
        
        self.geometry("1030x600+180+80")
        canSG=Canvas(self, width=1030,height=600)
        canSG.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        canSG.place(x=-2,y=-1.7)
        
        titreSG=Label(canSG, text="          Etats général des ventes",font=("harrington",30,"bold"),fg="gold",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        titreSG.place(x=175, y=10)
        
        self.canphotoSG=Canvas(self, width=800,height=390)
        
        self.photoPrec= PhotoImage(file="images/icprec1.png")
        boutonRetRespo = Button(canSG,image = self.photoPrec, bd=-2,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground = "black", cursor="hand2",
                                command=self.pageCaissiers)
        boutonRetRespo.place(x=10,y=10)
        
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("SELECT sum(prix_total),date FROM factures group by(date)")
        rows = cursor.fetchall()
        print(rows)
        con.close()
        
        recette=[]
        for elt in rows:
            recette+=[elt[0]]
            
        print(recette)
        
        indice=[]
        jour=[]
        for elt in rows:
            indice=str(elt[1])
            #print(str(elt[1]))
            
            #print(jour)
            
            jour+=[indice]
            
        print(jour)    
        #print(jour)
            
        
            
        taillex=len(rows)
        plt.figure(figsize=(7,4))
        
        
        
        plt.bar(jour ,height=recette,facecolor="green")
        
        plt.show()#pour fficher dans autre chose que jupiter
        
        plt.savefig('graphe.png')
        plt.close()
        
        
        self.imgSG= PhotoImage(file="images/graphe.png") 
        self.canphotoSG.create_image(2,2, anchor=NW, image=self.imgSG)
        self.canphotoSG.place(x=160,y=60)
        
        self.photoVparProd = PhotoImage(file="images/boutonStatprod1.png")
        btVparProd = Button(self,image=self.photoVparProd, bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",bd=-2,activebackground="black",cursor="hand2",
                            command=self.venteParProduit)
        btVparProd.place(x=700,y=500)
        
        menubar = Menu(self)
        
        ventemenu = Menu(menubar, tearoff=0)
        ventemenu.add_command(label="Nouvelle",command=self.caissierAppelProduits)
        
        ventemenu.add_command(label="Exit", command=self.menu)
        ventemenu.add_separator()
        menubar.add_cascade(label="Ventes", menu=ventemenu)
        
        produitmenu = Menu(menubar, tearoff=0)
        """produitmenu.add_command(label="Nouveau")"""
        produitmenu.add_command(label="Lister",command=self.caissierAppelProduits)
        produitmenu.add_command(label="Exit", command=self.destroy)
        produitmenu.add_separator()
        menubar.add_cascade(label="Produits", menu=produitmenu)
        
        
        factmenu = Menu(menubar, tearoff=0)
        
        factmenu.add_command(label="Lister",command=self.listerFacture)
        factmenu.add_command(label="Exit", command=self.destroy)
        factmenu.add_separator()
        menubar.add_cascade(label="Factures", menu=factmenu)
        
        statmenu = Menu(menubar, tearoff=0)
        statmenu.add_command(label="Consulter les statistiques de vente",command=self.caissierAppelEGV)
        statmenu.add_separator()
        menubar.add_cascade(label="Statistiques", menu=statmenu)
        
        self.config(menu=menubar)
        
        canSG.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        titreSG.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        btVparProd.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonRetRespo.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        
        
        
    def venteParProduit(self):
        
        Tk.destroy(self)
        Tk.__init__(self)
        
        self.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        self.geometry("1300x695+25+0")
        can=Canvas(self, width=900,heigh=620)
        can.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        can.place(x=0,y=20)
        self.photoPrec= PhotoImage(file="images/icprec1.png")
        boutonRet = Button(self,image = self.photoPrec, bd=-2,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground = "black", cursor="hand2",
                                command=self.etatsGeneralVentes)
        boutonRet.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonRet.place(x=580,y=2)
        
         
        
        
        
        canvas = Canvas(can,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",width=540,height=640)#c'est ici que tu peux modifier la taille du tableau de produit
        
        scroll_y = Scrollbar(can, orient="vertical", command=canvas.yview)
        entête = ["Numero","Nom","Prix"]
        indice=0
        
        
        frame = Frame(canvas,width=540,height=540,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        # labels presents dans le frame scrollable
        tab=psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER,PASSWORD))
        cursor=tab.cursor()
        cursor.execute("SELECT * FROM produits")
        rows=cursor.fetchall()
        tab.close()
        #print(rows)
        for i in entête:
            indice+=1   
            libelle = Label(self,text=i,bd=0.5,bg="gold",relief=RIDGE,width=26)
            libelle.grid(row=0,column=indice,sticky=NSEW)
        
        

        def fond(e):
            global imgp
            
            con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
            cursor = con.cursor()
            cursor.execute("select (sum(contenir.quantite) * sum(contenir.prix_unitaire)) as prix, factures.date from contenir inner join factures on (contenir.num_facture = factures.num_facture) where contenir.num_produit=%s group by date" %(e))
            rows = cursor.fetchall()
            print(rows)
            con.close()
            
            recette=[]
            for elt in rows:
                recette+=[elt[0]]
                
            print(recette)
            
            indice=[]
            jour=[]
            for elt in rows:
                indice=str(elt[1])
                #print(str(elt[1]))
                
                #print(jour)
                
                jour+=[indice]
                
            print(jour)    
            #print(jour)
                
            
                
            taillex=len(rows)
            plt.figure(figsize=(7,4))
            
            
            
            plt.bar(jour ,height=recette,facecolor="green")
            
            plt.show()#pour fficher dans autre chose que jupiter
            
            plt.savefig("images/graphe"+str(e)+".png")
            plt.close()
           
            #a=int(num_produit.get())
            #self.canphoto=Canvas(obj, width=200,height=200)
            imgp=PhotoImage(file="images/graphe"+str(e)+".png")
            self.canphoto.itemconfigure("img_fond",image=imgp)
            global parametre
            parametre = e
            print(parametre)
            

        
            
        listeNumero=[]
        for groupe in rows:
            listeNumero+=[groupe[0]]
                
            #print(listeNumero)
                
        listeNom=[]
        for groupe in rows:
            listeNom+=[groupe[1]]
            #print(listeNom)
            
        listePrix=[]
        for groupe in rows:
            listePrix+=[groupe[2]]
                #print(listePrix)
                    
        numero=dict()
        i=0
        while(i<len(listeNumero)): 
                
            numero[i] = Button(frame,text=listeNumero[i],bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold",cursor="hand2",bd=0.5,width=25)
            numero[i].config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
            numero[i].grid(row=i+1,column=1,sticky=NSEW)
                    
            i+=1
                    
        
                 
                #for indice in range(len(listeNom)):
                   # for element in listeNom
         
        
        nom=dict()  
        i=0
        while(i<len(listeNom)):
            nom[i] = Button(frame,text=listeNom[i],bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold", cursor="hand2",bd=0.5,width=25)
            nom[i].config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
            nom[i].grid(row=i+1,column=2,sticky=NSEW)
            i+=1
                        
        itemList=[]        
        for item in listeNumero:
            numero[listeNumero.index(item)].config(command = lambda z=item: fond(z)) 
            itemList.append(item)
            nom[listeNumero.index(item)].config(command = lambda z=item: fond(z))                
                
                #print(numero[listeNumero.index(item)])    
        i=0
        while(i<len(listePrix)):
            prix = Label(frame,text=str(listePrix[i])+" FCFA",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold", relief=RAISED,bd=0.5,width=25)
            prix.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
            prix.grid(row=i+1,column=3,sticky=NSEW)
            i+=1
    
       # insersion du frame dans le canvas
        canvas.create_window(100, 100, anchor='nw', window=frame)
        # on s'assure que tous sera affiché avant de définir la scrollregion
        canvas.update_idletasks()
        
        canvas.configure(scrollregion=canvas.bbox('all')#c'est cette commande qui s'assure de la presence, 
                         ,yscrollcommand=scroll_y.set)
                         
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')
        
        label_statParProd=Label(self, text= "Statistique de vente par produits", font=("arial", 15,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        label_statParProd.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        label_statParProd.place(x=780, y=0)
        
        self.canphoto=Canvas(self, width=687,height=350)       
        self.imgp= PhotoImage(file="images/graphe.png") 
        self.canphoto.create_image(2,-30, anchor=NW, image=self.imgp, tags="img_fond")
        self.canphoto.place(x=590,y=35)
        
        con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cursor = con.cursor()
        cursor.execute("select (sum(contenir.quantite) * sum(contenir.prix_unitaire)) as prix, contenir.num_produit from contenir  group by num_produit order by prix desc")
        rows = cursor.fetchall()

        
        con.close()
        print(rows)
        self.xs=[]
        self.ys=[] 
        for row in rows:
            x = row[0]
            y = row[1]
            self.xs.append(x)
            self.ys.append(y)
        print(self.xs)
        print(self.ys)
        
        
        
        label_meilleurVente=Label(self, text= "Produits les mieux vendus", font=("arial", 15,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        label_meilleurVente.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        label_meilleurVente.place(x=780, y=420)
       
        self.meillvente=[]
        for i in (self.ys[0], self.ys[1], self.ys[2]):
            con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
            cursor = con.cursor()
            cursor.execute("select nom_produit from produits where num_produit=%s" %(i))
            rows = cursor.fetchone()
            self.meillvente.append(rows[0])
            con.close()
        print(self.meillvente)
        
        self.vente1=StringVar()
        self.vente2=StringVar()
        self.vente3=StringVar()
        
        self.vente1.set(self.meillvente[0])
        self.vente2.set(self.meillvente[1])
        self.vente3.set(self.meillvente[2])
        
        self.canphotoMeillrVente1=Canvas(self, width=200,height=200)       
        self.imgMV1= PhotoImage(file="images/prod"+str(self.ys[0])+".png") 
        self.canphotoMeillrVente1.create_image(2,2, anchor=NW, image=self.imgMV1, tags="img_fond")
        self.canphotoMeillrVente1.place(x=590,y=460)
        label_mllrVente1=Label(self, textvariable=self.vente1, font=("arial", 13,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        label_mllrVente1.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        label_mllrVente1.place(x=590, y=665)
        
        self.canphotoMeillrVente2=Canvas(self, width=200,height=200)       
        self.imgMV2= PhotoImage(file="images/prod"+str(self.ys[1])+".png") 
        self.canphotoMeillrVente2.create_image(2,2, anchor=NW, image=self.imgMV2, tags="img_fond")
        self.canphotoMeillrVente2.place(x=830,y=460)
        label_mllrVente2=Label(self, textvariable=self.vente2, font=("arial", 13,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        label_mllrVente2.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        label_mllrVente2.place(x=830, y=665)
        
        self.canphotoMeillrVente3=Canvas(self, width=200,height=200)       
        self.imgMV3= PhotoImage(file="images/prod"+str(self.ys[2])+".png") 
        self.canphotoMeillrVente3.create_image(2,2, anchor=NW, image=self.imgMV3, tags="img_fond")
        self.canphotoMeillrVente3.place(x=1070,y=460)
        label_mllrVente3=Label(self, textvariable=self.vente3, font=("arial", 13,"bold"), bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold")
        label_mllrVente3.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        label_mllrVente3.place(x=1070, y=665)
        
        menubar = Menu(self)
        
        ventemenu = Menu(menubar, tearoff=0)
        ventemenu.add_command(label="Nouvelle",command=self.caissierAppelProduits)
        
        ventemenu.add_command(label="Exit", command=self.menu)
        ventemenu.add_separator()
        menubar.add_cascade(label="Ventes", menu=ventemenu)
        
        produitmenu = Menu(menubar, tearoff=0)
        """produitmenu.add_command(label="Nouveau")"""
        produitmenu.add_command(label="Lister",command=self.caissierAppelProduits)
        produitmenu.add_command(label="Exit", command=self.destroy)
        produitmenu.add_separator()
        menubar.add_cascade(label="Produits", menu=produitmenu)
        
        
        factmenu = Menu(menubar, tearoff=0)
        
        factmenu.add_command(label="Lister",command=self.listerFacture)
        factmenu.add_command(label="Exit", command=self.destroy)
        factmenu.add_separator()
        menubar.add_cascade(label="Factures", menu=factmenu)
        
        statmenu = Menu(menubar, tearoff=0)
        statmenu.add_command(label="Consulter les statistiques de vente",command=self.caissierAppelEGV)
        statmenu.add_separator()
        menubar.add_cascade(label="Statistiques", menu=statmenu)
        
        self.config(menu=menubar)
        
        self.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        boutonRet.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        
        
#===========================ARBORESCENCE DE PARAMETRES=========================== Button

    def parametres(self):
        global rouge
        global vert 
        global bleu
        global rouge2
        global vert2 
        global bleu2
        
        global varRouge
        global varVert
        global varBleu
        global varRouge2
        global varVert2
        global varBleu2
        global canParam
        global titreParam
        global labelRouge
        global labelVert
        global labelBleu
        global labelRouge2
        global labelVert2
        global labelBleu2
        global boutonChangArr
        global boutonprec
        
        
        
        
        
        
        self.geometry("910x534+180+80")
        canParam=Canvas(self, width=915,height=540)
        self.img=PhotoImage(file="images/imeleob.png")
        canParam.create_image(0,0,anchor=NW,image=self.img)
        canParam.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        canParam.place(x=-2,y=-1.7)
        
        listenombre=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        listecouleurs=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        i=1
        while (rouge,vert,bleu,rouge2,vert2,bleu2 in listecouleurs) and i==1:
            i=listecouleurs.index(rouge)
            rougeS=listenombre[i]
            i=listecouleurs.index(vert)
            vertS=listenombre[i]
            i=listecouleurs.index(bleu)
            bleuS=listenombre[i]
            i=listecouleurs.index(rouge2)
            rougeS2=listenombre[i]
            i=listecouleurs.index(vert2)
            vertS2=listenombre[i]
            i=listecouleurs.index(bleu2)
            bleuS2=listenombre[i]
            print(rouge)
            print(vert)
            print(bleu)
            print(rouge2)
            print(vert2)
            print(bleu2)
            i=0
        
        self.photoPrec= PhotoImage(file="images/icprec1.png")
        boutonprec = Button(canParam,image = self.photoPrec, bd=-2,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground = "black", cursor="hand2",
                                command=self.menu)
        
        boutonprec.place(x=10,y=10)
        
        
        titreParam=Label(canParam, text="Choisissez la couleur d'arrière plan \nqui vous convient",
                    font=("harrington",20,"bold"),fg="gold",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        titreParam.place(x=175, y=10)
        
        
        
        varRouge = IntVar()
        varVert = IntVar()
        varBleu = IntVar()
        varRouge2 = IntVar()
        varVert2 = IntVar()
        varBleu2 = IntVar()
        
        echelleRouge = Scale(self, variable=varRouge,from_=0 , to=15,length=200, orient="vertical" )
        echelleRouge.set(rougeS)
        echelleRouge.place(x=210,y=100)
        
        
        labelRouge=Label(self,text="Rouge",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold" ,font=("bold"))
        labelRouge.place(x=210,y=310)
        
        echelleRouge2 = Scale(self, variable=varRouge2,from_=0 , to=15,length=200, orient="vertical" )
        echelleRouge2.set(rougeS2)
        echelleRouge2.place(x=270,y=100)
        
        
        labelRouge2=Label(self,text="Rouge",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold" ,font=("bold"))
        labelRouge2.place(x=280,y=310)
        
        
        echelleVert = Scale(self, variable=varVert,from_=0 , to=15,length=200, orient="vertical" )
        echelleVert.set(vertS)
        echelleVert.place(x=410,y=100)
        
        labelVert=Label(self,text="Vert",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold",font=("bold"))
        labelVert.place(x=420,y=310)
        
        echelleVert2 = Scale(self, variable=varVert2,from_=0 , to=15,length=200, orient="vertical" )
        echelleVert2.set(vertS2)
        echelleVert2.place(x=480,y=100)
        
        labelVert2=Label(self,text="Vert",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold",font=("bold"))
        labelVert2.place(x=490,y=310)
        
        
        
        echelleBleu = Scale(self, variable=varBleu,from_=0 , to=15, length=200, orient="vertical")
        echelleBleu.set(bleuS)
        echelleBleu.place(x=630,y=100)
        
        labelBleu=Label(self,text="Bleu",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold",font=("bold"))
        labelBleu.place(x=640,y=310)
        
        
        echelleBleu2 = Scale(self, variable=varBleu2,from_=0 , to=15, length=200, orient="vertical")
        echelleBleu2.set(bleuS2)
        echelleBleu2.place(x=690,y=100)
        
        labelBleu2=Label(self,text="Bleu",bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",fg="gold",font=("bold"))
        labelBleu2.place(x=700,y=310)
        
        
        
        
        self.imChangArr=PhotoImage(file="images/boutChang1.png")
        boutonChangArr= Button(self, image=self.imChangArr, bd=-2,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"", activebackground="black",
                           command=self.changeArrierePlan)
        boutonChangArr.place(x=400, y=390)
        
        canParam.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        titreParam.config(bd=-2,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        labelRouge.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelVert.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelBleu.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelRouge2.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelVert2.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelBleu2.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        boutonChangArr.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonprec.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        
    def changeArrierePlan(self):
        global rouge
        global vert
        global bleu
        
        rouge=(varRouge.get())
        vert=(varVert.get())
        bleu=(varBleu.get())
        rouge2=(varRouge2.get())
        vert2=(varVert2.get())
        bleu2=(varBleu2.get())
        print(rouge2)
        
        
        listenombre=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        listecouleurs=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        i=1
        while (rouge,vert,bleu,rouge2,vert2,bleu2 in listenombre) and i==1:
            i=listenombre.index(rouge)
            rouge=listecouleurs[i]
            i=listenombre.index(vert)
            vert=listecouleurs[i]
            i=listenombre.index(bleu)
            bleu=listecouleurs[i]
            i=listenombre.index(rouge2)
            rouge2=listecouleurs[i]
            i=listenombre.index(vert2)
            vert2=listecouleurs[i]
            i=listenombre.index(bleu2)
            bleu2=listecouleurs[i]
            
            i=0
        
        
        if os.path.isdir('color'):
           pass
        else:
            os.mkdir("color")
        f1=open("color/primitive.txt","w")
        f1.write(rouge)
        f1.write("\n")
        f1.write(vert)
        f1.write("\n")
        f1.write(bleu)
        f1.write("\n")
        f1.write(rouge2)
        f1.write("\n")
        f1.write(vert2)
        f1.write("\n")
        f1.write(bleu2)
        f1.write("\n")
        f1.close()
        
        canParam.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        titreParam.config(bd=-2,bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        labelRouge.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelVert.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelBleu.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelRouge2.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelVert2.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        labelBleu2.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"")
        boutonChangArr.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        boutonprec.config(bg="#"+rouge+""+rouge2+""+vert+""+vert2+""+bleu+""+bleu2+"",activebackground="#"+rouge+""+vert+""+bleu+"")
        

        
        
 
o = Eleonor()
o.mainloop()