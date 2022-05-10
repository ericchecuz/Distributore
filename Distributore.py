from model.Bibita import Bibita
from model.Tessera import Tessera
from model.Colonna import Colonna

class Distributore:
    def  __init__(self):
        self.lista_tessere = []
        self.lista_bibite = []
        self.lista_colonne = []


    def aggiungiBevanda(self, codice, nome, prezzo):
        bevanda = Bibita(codice, nome , prezzo)
        self.lista_bibite.append(bevanda)
        print("BIBITA AGGIUNTA", nome, " CODICE ", codice, "PREZZO", prezzo)


    def getPrice(self, codiceBibita):
        for bibita in self.lista_bibite:
            if bibita.codice == codiceBibita:
                return float(bibita.prezzo)
        else:
            return("BIBITA INESISTENTE")

    def getNome(self, codiceBibita):
        for bibita in self.lista_bibite:
            if bibita.codice == codiceBibita:
                return str(bibita.codice)
        else :
            return ("BIBITA INESISTENTE")



    def caricaTessera(self, codiceTessera, credito):
            tessera = Tessera(codiceTessera,credito)
            self.lista_tessere.append(tessera)
            print("AGGIUNTA LA TESSERA NR^" ,tessera.codice, "CREDITO RESIDUO" , tessera.credito)


    def cancellaTessera(self, codiceTessera):
        for tessera in self.lista_tessere:
            if tessera.codice == codiceTessera:
                self.lista_tessere.remove(tessera)


    def leggiCredito(self, codiceTessera ):
        for tessera in self.lista_tessere:
            if tessera.codice == codiceTessera:

                return float(tessera.credito)

    def aggiornaColonna(self,colonna, bibita, lattine):
        col = Colonna(colonna, bibita, lattine)
        self.lista_colonne.append(col)
        print("AGGIUNTA COLONNA NR^", col.numero, "BIBITA", col.bibita , "NUMERO LATTINE", col.lattine)

    def lattineDisponibili(self, codiceBibita):
        for lattine in self.lista_colonne:
                if codiceBibita == self.getNome(codiceBibita):
                    print("CODICE -->", codiceBibita , "LATTINE DISPONIBILI-->", lattine.lattine)
                break

    def erogaBibita(self, codiceBibita, codiceTessera):
        credito = self.leggiCredito((codiceTessera))
        prezzo = self.getPrice(codiceBibita)
        prezzo = float(prezzo)
        credito = float(credito)

        nome = self.getNome(codiceBibita)
        for lattine in self.lista_colonne:
            if codiceBibita == nome :
                if lattine.lattine >0:
                    if(credito>prezzo):
                        credito = credito - prezzo
                        lattine.lattine=lattine.lattine-1
                        print("COSTO BEVANDA SELEZIONATA-->", prezzo, "NR TESSERA", codiceTessera, "CREDITO RESIDUO", credito)
                    break
                else:
                    raise Exception ("LATTINE ESAURITE")
            else:
                raise Exception("BIBITA NON VALIDA")