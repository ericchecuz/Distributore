from model.Colonna import Colonna
from model.Distributore import Distributore

distributore = Distributore()
colonna = Colonna("posizione", "nome", "lattinedisponibili")


distributore.aggiungiBevanda("A", "Acqua", 0.20 )
distributore.aggiungiBevanda("B", "Coca" , 0.30 )
distributore.aggiungiBevanda("C", "Birra", 1.00 )

distributore.caricaTessera(12, 5.5)
distributore.caricaTessera(21,10.0)
distributore.caricaTessera(99,0.75)

distributore.leggiCredito(12)
distributore.leggiCredito(21)
distributore.leggiCredito(99)

distributore.aggiornaColonna(1, "acqua", 40)
distributore.aggiornaColonna(2, "coca", 20 )
distributore.aggiornaColonna(3, "birra", 50 )
distributore.aggiornaColonna(4, "acqua frizz", 50 )

distributore.lattineDisponibili("A")

distributore.erogaBibita('A', 12)
distributore.erogaBibita('A', 21)
distributore.erogaBibita('C', 21)

