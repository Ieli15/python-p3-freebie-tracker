from models import session, Company, Dev, Freebie

genovese = Company(name="Genovese")
gigante = Company(name="Gigante")

elias = Dev(name="Elias")  
maureen = Dev(name="Maureen")

session.add_all([genovese, gigante, elias, maureen])
session.commit()

f1 = Freebie(item_name="T-shirt", value=10, dev=elias, company=genovese)  
f2 = Freebie(item_name="Laptop", value=1000, dev=maureen, company=gigante)

session.add_all([f1, f2])
session.commit()
