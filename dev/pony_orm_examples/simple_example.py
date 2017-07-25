from pony import orm

query = orm.select(p for p in Person).order_by(Person.name)[:2]

query.show()

with db_session:
    p = Person(name='Kate', age=33)
    Car(make='Audi', model='R8', owner=p)

@orm.db_session
def print_person_name(person_id):
    p = Person[person_id]
    print p.name


# p1 = Person(name='John', age=20)
# p2 = Person(name='Mary', age=22)
# p3 = Person(name='Bob', age=30)
# c1 = Car(make='Toyota', model='Prius', owner=p2)
# c2 = Car(make='Ford', model='Explorer', owner=p3)
# commit()

class MyEntity(db.Entity):
    attr1 = Required(str)

db.generate_mapping(create_tables=True)