from models import session, Company, Dev, Freebie

google = Company(name="Google")
apple = Company(name="Apple")

alice = Dev(name="Alice")  
bob = Dev(name="Bob")

session.add_all([google, apple, alice, bob])
session.commit()

f1 = Freebie(item_name="T-shirt", value=10, dev=alice, company=google)  
f2 = Freebie(item_name="Laptop", value=1000, dev=bob, company=apple)

session.add_all([f1, f2])
session.commit()
