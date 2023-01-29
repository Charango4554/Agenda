#classe Contact
class Contact:
    def __init__(self, nom, prenom, numero):
        self.nom = nom
        self.prenom = prenom
        self.numero = numero
        
    def __str__(self):
        return f"{self.prenom} {self.nom}: {self.numero}"
    
#classe Agenda qui va gérer la liste des contacts
class Agenda:
    def __init__(self):
        self.contacts = []
        
    def ajouter_contact(self, contact):
        self.contacts.append(contact)
        
    def lister_contacts(self):
        for contact in self.contacts:
            print(contact)
            
    def supprimer_contact(self, nom):
        contacts_a_supprimer = []
        for i, contact in enumerate(self.contacts):
            if contact.nom == nom:
                contacts_a_supprimer.append(i)
                
        for i in reversed(contacts_a_supprimer):
            del self.contacts[i]

                
    def rechercher_contact(self, nom):
        for contact in self.contacts:
            if contact.nom == nom:
                return contact
        return None

#Appelle agenda
agenda = Agenda()

#Programme d'utilisation
quitter = False
while not quitter:
    print("\nGestion des contacts")
    print("1. Ajouter un contact")
    print("2. Lister les contacts")
    print("3. Supprimer un contact")
    print("4. Rechercher un contact")
    print("5. Quitter")
    
    choix = int(input("Choisissez une option : "))
    
    if choix == 1:
        nom = input("Entrez le nom : ")
        prenom = input("Entrez le prénom : ")
        numero = input("Entrez le numéro de téléphone : ")
        agenda.ajouter_contact(Contact(nom, prenom, numero))
        print("Contact ajouté avec succès")
        
    elif choix == 2:
        print("Liste des contacts :")
        agenda.lister_contacts()
        
    elif choix == 3:
        nom = input("Entrez le nom du contact à supprimer : ")
        agenda.supprimer_contact(nom)
        print("Contact supprimé avec succès")
        
    elif choix == 4:
        nom = input("Entrez le nom du contact à rechercher : ")
        contact = agenda.rechercher_contact(nom)
        if contact:
            print(f"Contact trouvé : {contact}")
        else:
            print("Contact non trouvé")
        
    elif choix == 5:
        quitter = True
        print("Au revoir")
        
    else:
        print("Choix non valide")
