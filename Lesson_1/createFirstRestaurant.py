# To run this script first run initiateSession.py

#create instance of Restaurant class
myFirstRestaurant = Restaurant(name= "Pizza Palace")

#put Restaurant object to a staging zone
session.add(myFirstRestaurant)
#store Restaurant object into db
session.commit()

#ask session to go to a db, find the table that corresponds
#to the Restaurant class and find all the entries in table
#and return them in list
session.query(Restaurant).all()

#add menue items for "Pizza Palace" restaurant
#and specify foreign key relationship to the object name
#of first restaurant
cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
session.add(cheesepizza)
session.commit()

#to check if object exist - consider print to see on screen
session.query(MenuItem).all()
print "First restaunrant and first menu created successfully!"
