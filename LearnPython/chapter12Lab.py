from logMessage import LogMessageFile
from logMessage import LogMessageDB

log = LogMessageFile('ch12LogFile.txt')
log.write('This is a write to a file-based log.')
log.read()

log2 = LogMessageDB('ch12LogDB.db')
log2.write('This is a write to a database log.')
log2.read()