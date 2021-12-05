# Advanced-Programming-CA-1-2021
Create and test a function to compute net pay from payment, work, and tax credit information of Employees.

Details of Variables and function used
 
 Global Variables:
    1.allEmpDetails=[]
    Here we are storing all employees.txt data in dictionary format.
    
    2.allHoursDetails=[] 
    Here we are storing all hours.txt data in dictionary format.
    
    3.currentEmpDetails,currentHoursDetails = {}
    This object we are using while calculating computePay for individuals

    4.empPropertiesList
    This list contains all proerties(keys) related to employee.txt which we are using while constructing dictionary object
    
    5.hourPropertiesList
    Same as of empPropertiesList, but here keys are related to hours.txt.
    


 Functions:
     @classmethod
    1.def constuctEmpHoursObject(cls,empTextFile,hourTextFile):
      This is classmethod which we are calling before object creation, to construct the dictionary objects from txt files.
      As we need to construct objects first whatevr we have recieved without waiting for init method.
    
    2.def __init__(self,staff_ID):
      We are using this method while creating object by passing staff_ID which is necessary while calculating pay for individuals,
      for computeAll we don't need to use this method
      If we pass wrong or invalid staffID, user will get error message in console.
      
    3.def computePayment(self,date,hours_worked):
      This method takes two paramaeter(date, hours worked).Here based on data and hours we are calculating the pay for current employee object.
      This method is reusable which we are using by calling it recursively while calculating computeAllPay().
      
    4.def computeAllPayment():
      This functions will calculate computePay of all Employees available in our txt files, this will return array of object based on number of records.
      Here we are re-using computePayment(self,date,hours_worked) method.
    
    5.def displayData(self):
      Whatever object we are returning, in this method we will be changing property names as per sample output required. After object is modified,
      we will return the result object to function. 
      
 
 Test cases:
    We have added test cases for below scenario:
      1.Net pay cannot exceed gross pay
      2.Overtime pay cannot be negative
      3.Overtime hours cannot be negative
      4.Higher Tax cannot be negative
      5.Net Pay cannot be negative
      
  
      
