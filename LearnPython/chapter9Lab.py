class PayrollCalc:
    def __init__(self, nameIn, hourlyIn, hoursWorkedIn):
        self.name = nameIn
        self.hourly = hourlyIn
        self.hoursWorked = hoursWorkedIn
        self.overtime = False
        self.overtimeHours = 0
    def overtimeCalc(self):
        if self.hoursWorked > 40:
            otHours = self.hoursWorked % 40
            self.overtimeHours = otHours
            otHours /= 2
            self.hoursWorked += otHours
            self.overtime = True
    def toString(self):
        print(self.name)
        self.overtimeCalc()
        if not(self.overtime):
            print('Hours worked:', self.hoursWorked)
            print('Total pay:', self.hoursWorked * self.hourly)
        else:
            print('Regular hours worked: 40')
            print('Regular pay:', self.hourly * 40)
            print('Overtime hours worked:', self.overtimeHours)
            print('Overtime pay:', (self.overtimeHours * self.hourly) * 1.5)
            print('Total pay:', self.hoursWorked * self.hourly)
            
john = PayrollCalc('John', 10, 50)
john.toString()
jane = PayrollCalc('Jane', 8, 37)
jane.toString()