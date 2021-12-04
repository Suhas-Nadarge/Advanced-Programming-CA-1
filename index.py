class Employee:
    allEmpDetails=[]
    allHoursDetails=[]
    currentEmpDetails = {}
    currentHoursDetails ={}
    name,date= '',''
    regularHoursWorked,overtimeHoursWorked,regularRate,overtimeRate,regularPay,overtimePay,grossPay = 0,0,0,0,0,0,0
    standardRatePay,higherRatePay,standardTax,higherTax,totalTax,taxCredit,netDeduction,netPay = 0,0,0,0,0,0,0,0
    
    empPropertiesList = ['StaffID','LastName','FirstName','RegHours','HourlyRate','OTMultiple','TaxCredit','StandardBand']
    hourPropertiesList= ['StaffID','Date','HoursWorked']
    resultOutput = dict()

    with open ('Employees.txt', 'w') as f:
        f.write('12345 Green Joe 37 16 3 70 700 ,12346 Suhas Reddy 35 16 1.5 70 700')
        # <StaffID> <LastName> <FirstName> <RegHours> <HourlyRate> <OTMultiple> <TaxCredit> <StandardBand>
    with open('Hours.txt','w') as f:
        f.write('12345 31/10/2021 42 ,12346 31/10/2021 40 ,12345 30/10/2021 63')
        # <StaffID> <Date> <HoursWorked>



    @classmethod
    def constuctEmpHoursObject(cls,empTextFile,hourTextFile):
        # Lets construct dictionary object for Employee with key-value pair by reading Employees.txt file
        myEmpfile = open(empTextFile, "rt")
        contents = myEmpfile.read()        
        myEmpfile.close()
        # Copied from  https://stackoverflow.com/questions/14658623/how-to-merge-2-list-as-a-key-value-pair-in-python
        #  and modified by me for mapping keys to the values from Employees.txt and Hours.txt
        for i in contents.split(','):
            cls.allEmpDetails.append(dict(zip(cls.empPropertiesList,i.split(' '))))
            # print(cls.allEmpDetails)

        # Lets construct dictionary object for Working Hours from Hours.txt same as we did for Employee
        myHourfile = open(hourTextFile, "rt")
        contents = myHourfile.read()         
        myHourfile.close()
        for k in contents.split(','):
            cls.allHoursDetails.append(dict(zip(cls.hourPropertiesList,k.split(' '))))
            # print(cls.allHoursDetails)
            

    def __init__(self,staff_ID):
        for j in self.allEmpDetails:
            if staff_ID == j['StaffID']:
                self.currentEmpDetails = j
                # print('current emp object-> ',self.currentEmpDetails)

        # if user enters wrong staff_ID, he will get warning message as below
        if not self.currentEmpDetails:
            print('Please enter correct Staff-Number')

        for p in self.allHoursDetails:
            if staff_ID == p['StaffID']:
             self.currentHoursDetails = p
            #  print('current Hour object-> ',self.currentHoursDetails) 
          


    def computePayment(self,date,hours_worked):
        #   print(self.currentEmpDetails)
        # Taken from https://techvidvan.com/tutorials/ternary-operator-in-python modified by me(for conditional statements)
          self.name = self.currentEmpDetails['FirstName']+''+self.currentEmpDetails['LastName']
          self.date = date
          self.regularHoursWorked = float(self.currentEmpDetails['RegHours'] if float(hours_worked) > float(self.currentEmpDetails['RegHours']) else hours_worked) 
          self.regularRate = self.currentEmpDetails['HourlyRate']
          self.regularPay = float(self.regularRate)*self.regularHoursWorked
          
          self.overtimeRate = float(self.regularRate)*float(self.currentEmpDetails['OTMultiple'])
          
          if float(hours_worked) > float(self.currentEmpDetails['RegHours']):
              self.overtimeHoursWorked = float(hours_worked) - float(self.currentEmpDetails['RegHours'])
          else:
              self.overtimeHoursWorked = 0
          self.overtimePay = self.overtimeHoursWorked*self.overtimeRate
          self.grossPay = self.regularPay + self.overtimePay
          self.standardRatePay = float(self.currentEmpDetails['StandardBand'])
          if self.grossPay > float(self.currentEmpDetails['StandardBand']):
              self.higherRatePay = self.grossPay - float(self.currentEmpDetails['StandardBand'])
          else:
              self.higherRatePay = 0

        # Taxes calculation starts
          self.higherTax = round(0.4*self.higherRatePay, 2)
          self.standardTax = 0.2*float(self.currentEmpDetails['StandardBand'])
          self.totalTax = self.higherTax+self.standardTax
        # Taxes calculation ends

        # Deduction calculation starts
          self.netDeduction = self.totalTax-int(self.currentEmpDetails['TaxCredit'])
          self.netDeduction = round(self.netDeduction,2)
          self.netPay = self.grossPay-self.netDeduction
        # Deduction calculation ends  
        
          self.displayData()

    # This method will display calculated data
    def displayData(self):
        # deleting properties which we created from txt file for iterating purpose
        # delattr(self, 'currentEmpDetails')
        # delattr(self, 'currentHoursDetails')

        for item in vars(self):
            # return dictionary object in key:value pair
            # Exclude the current objects which we created from txt files for calculation purpose, as we don't need it in output
            if item not in ['currentEmpDetails','currentHoursDetails']:
             self.resultOutput[item] = vars(self)[item]


        print(self.resultOutput)


    def computeAllPayment():
        print()
 
# Step-1:Method to read text files and construct object for Employee and Hours details
setData = Employee.constuctEmpHoursObject("Employees.txt","Hours.txt")

# Step-2:Create object for specific employee by passing Staff_ID
suhasObj = Employee('12345')

# Step-3:Call compute payment method by passing date and hours worked
suhasObj.computePayment('31/10/2021', 42)
suhasObj.computePayment('30/10/2021', 63)

# suhasObj.computeAllPayment()








