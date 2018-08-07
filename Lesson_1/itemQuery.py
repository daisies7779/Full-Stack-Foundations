#query retrievs all MenuItem
items = session.query(MenuItem).all()
for item in items:
	print item.name
