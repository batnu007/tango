from selenium import webdriver
from selenium.webdriver.common.keys import Keys



from const import url,usr,pwd,driver

# inp_user_name = 'adil'
# inp_provisioner_id = '455324'
# passwd = '12345'
# rep_passwd = '12345'
# email = 'adil@gmail.com'



def open_link():

	try:
		driver.get(url)
		print "LINK OPEN SUCCESS..."
	except :
		print "LINK FAIL........"


def login():

	try:

		user = driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[1]/td[2]/input")
		passwd = driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[2]/td[2]/input")
		user.send_keys(usr)
		passwd.send_keys(pwd)
		passwd.send_keys(Keys.RETURN)

		print "LOGIN SUSCCESFUL...."

	except:
		print "LOGIN FAIL......."


def create_user():


	try:

		click_manage = driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[14]/a')
		click_manage.click()

		#print "MANAGE PROVISION...."

		click_provisioner = driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr[2]/td/form/div/a[1]')
		click_provisioner.click()

		#print "CREATING NEW USER..."

		elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[1]/table/tbody/tr[1]/td[2]/input")
		elem.send_keys(inp_user_name)


		elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[1]/table/tbody/tr[2]/td[2]/input")
		elem.send_keys(inp_provisioner_id)

		elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[1]/table/tbody/tr[3]/td[2]/input")
		elem.send_keys(passwd)

		elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[1]/table/tbody/tr[4]/td[2]/input")
		elem.send_keys(rep_passwd)


		elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[1]/table/tbody/tr[5]/td[2]/input")
		elem.send_keys(email)

		#print "USER DATA ENTERED.."


		elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[3]/input[1]").click()
		# handle the alert
		alert = driver.switch_to_alert()
		alert.accept()
		
		elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[1]/table/tbody/tr[1]/td")

		if elem:
			print "USER ALREADY CREATED............"
		else:
			print "USER CREATED.............."
		
	except:
		print "USER CREATION FAILED......"


def close():

	try:
		driver.close()
		print "LINK CLOSED SUCCESSFULLY........"
	except:
		"LINK NOT CLOSED SUCCESSFULLY......"



########## Function Calls #############

with open('data.csv') as inp_file:
	for each_line in inp_file:
		inp_user_name,inp_provisioner_id,passwd,rep_passwd,email = each_line.split(',')
		# print inp_user_name
		# print inp_provisioner_id
		# print passwd
		# print rep_passwd
		# print email
		try:
			open_link()
			login()
			create_user()
			close()
			print 
			print 
			#print inp_user_name + "CREATED!!!!!!" + "\n"			
		except:
			print inp_user_name + "not created" + "\n"
			pass




'''
'''