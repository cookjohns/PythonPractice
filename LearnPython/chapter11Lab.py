import sqlite3

class LogMessage:
    def __init__(self, dbNameIn):
        self.dbName = dbNameIn
        self.db = sqlite3.connect(self.dbName)                  #create database
    def read(self):
        table = self.db.execute('select * from messages')       #grab all info from db
        for each in table:
            print(each)                                         #print all info from table
    def write(self, messageIn):
        self.db.execute('drop table if exists messages')        #drop table if it exists
        self.db.execute('create table messages (message text)') #create table in db to store messages
        self.db.execute('insert into messages (message) values (?)', [messageIn]) #uses brackets to input string as a tuple rather than input sequence
        self.db.commit()
        
messageDB = LogMessage('log.db')
messageDB.write('This is a test message.')
messageDB.read()