class Employee:
    empDetails={}
    workDetails={}
    empPropertiesList = ['StaffID','LastName','FirstName','RegHours','HourlyRate','OTMultiple','TaxCredit','StandardBand']
    hourPropertiesList= ['StaffID','Date','HoursWorked']

    with open ('Employees.txt', 'w') as f:
        f.write('12345 Green Joe 37 16 1.5 70 700,12346 Suhas Reddy 35 16 1.5 70 700')
        # <StaffID> <LastName> <FirstName> <RegHours> <HourlyRate> <OTMultiple> <TaxCredit> <StandardBand>
    with open('Hours.txt','w') as f:
        f.write('12345 31/10/2021 42,12346 31/10/2021 40')
        # <StaffID> <Date> <HoursWorked>

    def __init__(self,empDetails={},workDetails={}):
        self.constructWorkObj()
        self.constructEmpObj()  

# Lets construct dictionary object for Employee with key-value pair by reading Employees.txt file
    def constructEmpObj(self):
        myEmpfile = open("Employees.txt", "rt")
        contents = myEmpfile.read()        
        myEmpfile.close()
        # Copied from  https://stackoverflow.com/questions/14658623/how-to-merge-2-list-as-a-key-value-pair-in-python and modified by me for merging
        print(dict(zip(self.empPropertiesList,contents.split(' '))))
        self.empDetails = dict(zip(self.empPropertiesList,contents.split(' ')))

        
# Lets construct dictionary object for Working Hours with key-value pair by reading Hours.txt file
    def constructWorkObj(self):
        myHourfile = open("Hours.txt", "rt")
        contents = myHourfile.read()        
        myHourfile.close()
        # Copied from  https://stackoverflow.com/questions/14658623/how-to-merge-2-list-as-a-key-value-pair-in-python and modified by me for merging
        print(dict(zip(self.hourPropertiesList,contents.split(' '))))
        self.empDetails = dict(zip(self.empPropertiesList,contents.split(' ')))       


obj = Employee()



