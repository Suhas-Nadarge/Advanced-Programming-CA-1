import copy
import json
class Employee:
    allEmpDetails=[]
    allHoursDetails=[]
    currentEmpDetails = {}
    currentHoursDetails ={}
    name,date= '',''
    regularHoursWorked,overtimeHoursWorked,regularRate,overtimeRate,regularPay,overtimePay,grossPay = 0,0,0,0,0,0,0
    standardRatePay,higherRatePay,standardTax,higherTax,totalTax,taxCredit,netDeduction,netPay = 0,0,0,0,0,0,0,0
    
    empPropertiesList = ['StaffID','FirstName','LastName','RegHours','HourlyRate','OTMultiple','TaxCredit','StandardBand']
    hourPropertiesList= ['StaffID','Date','HoursWorked']
    resultOutput = dict()

    with open ('Employees.txt', 'w') as f:
        f.write('12345 Green Joe 37 16 1.75 70 700 ,12346 Suhas Reddy 35 16 1.5 70 900 ,12347 John Nill 40 18 1.5 90 1100')
        # ***After each property space is mandatory***
        # <StaffID> <LastName> <FirstName> <RegHours> <HourlyRate> <OTMultiple> <TaxCredit> <StandardBand>
    with open('Hours.txt','w') as f:
        f.write('12345 30/10/2021 42 ,12346 31/10/2021 40 ,12347 31/10/2021 63')
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

        # Lets construct dictionary object for Working Hours from Hours.txt same as we did for Employee
        myHourfile = open(hourTextFile, "rt")
        contents = myHourfile.read()         
        myHourfile.close()
        for k in contents.split(','):
            cls.allHoursDetails.append(dict(zip(cls.hourPropertiesList,k.split(' '))))
            


# This method is useful only while calculating individuals pay
    def __init__(self,staff_ID):
        for j in self.allEmpDetails:
            if staff_ID == j['StaffID']:
                self.currentEmpDetails = j

        # if user enters wrong staff_ID, he will get warning message as below
        if not self.currentEmpDetails:
            print('Please enter correct Staff-Number')

        for p in self.allHoursDetails:
            if staff_ID == p['StaffID']:
             self.currentHoursDetails = p
          

    def computePayment(self,date,hours_worked):
        # Referred from https://techvidvan.com/tutorials/ternary-operator-in-python modified by me(for conditional statements)
          self.name = self.currentEmpDetails['FirstName']+' '+self.currentEmpDetails['LastName']
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

        # Taxes calculation
          self.higherTax = round(0.4*self.higherRatePay, 2)
          self.standardTax = 0.2*float(self.currentEmpDetails['StandardBand'])
          self.totalTax = self.higherTax+self.standardTax

        # Deduction calculation
          self.taxCredit = float(self.currentEmpDetails['TaxCredit'])
          self.netDeduction = self.totalTax-self.taxCredit
          self.netDeduction = round(self.netDeduction,2)
          self.netPay = self.grossPay-self.netDeduction

          return self.displayData()


    # This method will display calculated data
    def displayData(self):
        for item in vars(self):
            # return dictionary object in key:value pair
            # Exclude the current objects which we created from txt files for calculation purpose, as we don't need it in output
            if item not in ['currentEmpDetails','currentHoursDetails']:
             self.resultOutput[item] = vars(self)[item]

        # To rename the keys from dictionary object for displaying purpose
        # Taken Reference from https://thewebdev.info/2021/10/29/how-to-rename-a-dictionary-key-with-python/ and modified by me
        # print('Before: ',self.resultOutput)
        self.resultOutput['Name'] = self.resultOutput.pop('name')
        self.resultOutput['Date'] = self.resultOutput.pop('date')
        self.resultOutput['Regular Hours Worked'] = self.resultOutput.pop('regularHoursWorked')
        self.resultOutput['Overtime Hours Worked'] = self.resultOutput.pop('overtimeHoursWorked')
        self.resultOutput['Regular Rate'] = self.resultOutput.pop('regularRate')
        self.resultOutput['Over Time Rate'] = self.resultOutput.pop('overtimeRate')
        self.resultOutput['Regular Pay'] = self.resultOutput.pop('regularPay')
        self.resultOutput['Over Time Pay'] = self.resultOutput.pop('overtimePay')
        self.resultOutput['Gross Pay'] = self.resultOutput.pop('grossPay')
        self.resultOutput['Standard Rate Pay'] = self.resultOutput.pop('standardRatePay')
        self.resultOutput['Higher Rate Pay'] = self.resultOutput.pop('higherRatePay')
        self.resultOutput['Standard Tax'] = self.resultOutput.pop('standardTax')
        self.resultOutput['Higher Tax'] = self.resultOutput.pop('higherTax')
        self.resultOutput['Total Tax'] = self.resultOutput.pop('totalTax')
        self.resultOutput['Tax Credit'] = self.resultOutput.pop('taxCredit')
        self.resultOutput['Net Deductions'] = self.resultOutput.pop('netDeduction')
        self.resultOutput['Net Pay'] = self.resultOutput.pop('netPay')

        # final expected output
        # print('After: ',self.resultOutput)
        return self.resultOutput



    # This method will work same as ComputePay() but here will iterate each record and calculate pay for all by reusing the ComputePay()
    def computeAllPayment():
        allObj =[]
        for element in Employee.allHoursDetails:
            # Taken Reference from https://stackoverflow.com/questions/7125467/find-object-in-list-that-has-attribute-equal-to-some-value-that-meets-any-condi
            # Mapping StaffID from both file to send them  to computePayment() as parameter
            Employee.currentEmpDetails = next(x for x in Employee.allEmpDetails if x['StaffID']== element['StaffID'])
            # We will create instances dynamically for each record
            obj = Employee(Employee.currentEmpDetails['StaffID'])
            # Deep copy is used because we are playing with object which is dynamically created 
            allObj.append(copy.deepcopy(obj.computePayment(element['Date'], float(element['HoursWorked']))))

        return allObj     

# Step-1:Method to read text files and construct object for Employee and Hours details----->Common for all(Individuals and Seperate Employee)
setData = Employee.constuctEmpHoursObject("Employees.txt","Hours.txt")



# Step-2:Create object for specific employee by passing respective Staff_ID
jg = Employee('12345')

# Step-3:Call compute payment method by passing date and hours worked()
print('Individual Employee Compute Pay: ',jg.computePayment('30/10/2021', 42))
print()
# print('Individual Employee Compute Pay: ',jg.computePayment('31/10/2021', 63) )



# Calculate for all employees
print('Compute All Details: ',Employee.computeAllPayment())








