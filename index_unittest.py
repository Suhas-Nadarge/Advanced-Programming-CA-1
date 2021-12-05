import unittest
from index import Employee

class testTest(unittest.TestCase):
  def testNetLessEqualGross(self):
    self.assertLessEqual(jg['Net Pay'],jg['Gross Pay'],'Net pay cannot exceed gross pay')

  def testNegativeOverTimePay(self):
    self.assertGreaterEqual(jg['Over Time Pay'],0,'Overtime pay cannot be negative')

  def testNegativeOvertimeHours(self):
    self.assertGreaterEqual(jg['Overtime Hours Worked'],0,'Overtime hours cannot be negative')

  def testNegativeHigherTax(self):
    self.assertGreaterEqual(jg['Higher Tax'],0,'Higher Tax cannot be negative')

  def testNegativeNetPay(self):
    self.assertGreaterEqual(jg['Net Pay'],0,'Net Pay cannot be negative')

    
  

# b = testTest()
# b.testPass()  
if __name__ == '__main__':
     jg = Employee('12345')
     jg = jg.computePayment('30/10/2021', 42)
     print(jg)
     unittest.main()