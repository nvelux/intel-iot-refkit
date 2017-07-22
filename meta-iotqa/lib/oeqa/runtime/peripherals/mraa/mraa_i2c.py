from oeqa.oetest import oeRuntimeTest

class MraaI2cTest(oeRuntimeTest):
     def test_mraa_i2c_version(self):
        (status, output)= self.target.run("mraa-i2c version")
	self.assertEqual(status, 0, msg="Error messages: %s" % output)
     def test_mraa_i2c_list(self):
	(status, output)= self.target.run("mraa-i2c list")
	self.assertEqual(status, 0, msg="Error messages: %s" % output)
     def test_mraa_i2c_detectbus(self):
	(status, output)= self.target.run("mraa-i2c detect bus")
	self.assertEqual(status, 0, msg="Error messages: %s" % output)

     def test_i2c_value():
	(status, output) = self.target.run("mraa-i2c set 1 0x02 0x03 0x04 > /tmp/log.txt")
	(status, output) = self.target.run("cat /tmp/log.txt|grep 'value = 04'")
        self.assertEqual(status, 0, msg="Error messages: %s" % output)

