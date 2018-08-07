# Veggie Burger price before change in specific restaurant Urban Burger with id 10
UrbanVeggieBurger = session.query(MenuItem).filter_by(id = 10).one()
print 'Veggie Burger price in restaurant id 10'
print UrbanVeggieBurger.price

#reset price of the Urban Veggie Burger to $2.99
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()
print "price is changed to:"
print UrbanVeggieBurger.price