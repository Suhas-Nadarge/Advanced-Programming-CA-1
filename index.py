class Employee:
    empDetails={}
    workDetails={}

    with open ('Employees.txt', 'w') as f:
        f.write('12345 Green Joe 37 16 1.5 70 700,12346 Suhas Reddy 35 16 1.5 70 700')
        # <StaffID> <LastName> <FirstName> <RegHours> <HourlyRate> <OTMultiple> <TaxCredit> <StandardBand>

    with open('Hours.txt','w') as f:
        f.write('12345 31/10/2021 42,12346 31/10/2021 40')
        # <StaffID> <Date> <HoursWorked>

    def __init__(self,empDetails={},workDetails={}):
        self.contructEmpObj()
        self.contructWorkObj()
        
# Lets construct dictionary object for Employee with key-value pair by reading Employees.txt file
    def constructEmpObj():
        myEmpfile = open("Employees.txt", "rt")
        contents = myEmpfile.read()        
        myEmpfile.close()
        for i in contents.split(','):
            print(i) 

# Lets construct dictionary object for Working Hours with key-value pair by reading Hours.txt file
    def constructWorkObj():
        myEmpfile = open("Hours.txt", "rt")
        contents = myEmpfile.read()        
        myEmpfile.close()
        for i in contents.split(','):
            print(i)         

# Create instance of class
obj = Employee()



