class LogMessage:
    def __init__(self, filenameIn):
        self.filename = filenameIn
    def read(self):
        input = open(self.filename, 'r')
        for line in input:
            print(line, end = '')
    def write(self, messageIn):
        output = open(self.filename, 'w')
        output.write(messageIn)

log = LogMessage('log.txt')
log.write('This is a test, man.')
log.read()