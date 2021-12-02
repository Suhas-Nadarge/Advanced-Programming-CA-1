class Employee:
    allEmpDetails=[]
    allHoursDetails=[]
    currentEmpDetails = {}
    currentHoursDetails ={}
    empPropertiesList = ['StaffID','LastName','FirstName','RegHours','HourlyRate','OTMultiple','TaxCredit','StandardBand']
    hourPropertiesList= ['StaffID','Date','HoursWorked']

    with open ('Employees.txt', 'w') as f:
        f.write('12345 Green Joe 37 16 1.5 70 700 ,12346 Suhas Reddy 35 16 1.5 70 700')
        # <StaffID> <LastName> <FirstName> <RegHours> <HourlyRate> <OTMultiple> <TaxCredit> <StandardBand>
    with open('Hours.txt','w') as f:
        f.write('12345 31/10/2021 42 ,12346 31/10/2021 40')
        # <StaffID> <Date> <HoursWorked>

    @classmethod
    def constuctEmpHoursObject(cls):
        # Lets construct dictionary object for Employee with key-value pair by reading Employees.txt file
        myEmpfile = open("Employees.txt", "rt")
        contents = myEmpfile.read()        
        myEmpfile.close()
        # Copied from  https://stackoverflow.com/questions/14658623/how-to-merge-2-list-as-a-key-value-pair-in-python
        #  and modified by me for mapping keys to the values from Employees.txt and Hours.txt
        for i in contents.split(','):
            cls.allEmpDetails.append(dict(zip(cls.empPropertiesList,i.split(' '))))
            # print(cls.allEmpDetails)

        # Lets construct dictionary object for Working Hours from Hours.txt same as we did for Employee
        myHourfile = open("Hours.txt", "rt")
        contents = myHourfile.read()         
        myHourfile.close()
        for k in contents.split(','):
            cls.allHoursDetails.append(dict(zip(cls.hourPropertiesList,k.split(' '))))
            # print(cls.allHoursDetails)
            

    def __init__(self,staff_ID):
        for j in self.allEmpDetails:
            if staff_ID == j['StaffID']:
                self.currentEmpDetails = j
                print('current emp-> ',self.currentEmpDetails)
            else:
                print('Please enter correct Staff-Number')
        for p in self.allHoursDetails:
            if staff_ID == p['StaffID']:
             self.currentHoursDetails = p
             print('current Hour-> ',self.currentHoursDetails)   

    def compute_payment(self,date,hours_worked):
        test_dict = {'hours': hours_worked,'date': date,'name':self.first_name}
        return test_dict     

# Method to read text files and construct object for Employee and Hours details
setData = Employee.constuctEmpHoursObject()

# Create object for specifoc employee by passing Staff_ID
suhasObj = Employee('12346')

# suhasObj.compute_payment('31/10/2021', '40')



