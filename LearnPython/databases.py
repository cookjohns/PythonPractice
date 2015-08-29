import sqlite3

db = sqlite3.connect('database.db') #creates database file
#db.execute('drop table if exists person') #deletes the 'person' table if it exists
#db.execute('create table person (firstName text, secondName text, age int)') #create table in database

# add person to database

#db.execute('insert into person (firstName, secondName, age) values ("John", "Cook", 26)')
#db.commit() #commit to database

# update record in database

#db.execute('update person set firstName = "Anna" where secondName = "Cook"') #udpates all instances of last name Cook to have first name Anna
#db.commit()

# delete record from database

table = db.execute('select * from person') #fills table with every record from db, may replace * with value
for each in table:
    print(each)                            #prints every record in db because it's now in table
    
nameTable = db.execute('select firstName from person') #prints every first name in db
for each in nameTable:
    print(each)

db.row_factory = sqlite3.Row #allows data to come back as dictionary
lastNameTable = db.execute('select secondName from person')
for each in lastNameTable:
    print(dict(each)) #prints data as dictionary (key : value), or in this case 'secondName : Cook'
    
# delete a record from database
#add a rec to delete first, commit, and check
#db.execute('insert into person (firstName, secondName, age) values ("This", "Guy", 20)')
#db.commit()
#now delete it
db.execute('delete from person where secondName = "Guy"')
db.execute('delete from person where age > 30')
db.commit()