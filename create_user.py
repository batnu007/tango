from selenium import webdriver
from selenium.webdriver.common.keys import Keys



from const import url,usr,pwd,driver


def open_link():

	driver.get(url)

	print "LINK OPEN SUCCESS..."



def login():

	user = driver.find_element_by_name("username")
	passwd = driver.find_element_by_name("password")
	user.send_keys(usr)
	passwd.send_keys(pwd)
	passwd.send_keys(Keys.RETURN)

	print "LOGIN SUSCCESFUL...."


def create_user():

	click_manage = driver.find_element_by_link_text('Manage Provisioners')
	click_manage.click()

	print "MANAGE PROVISION...."

	click_provisioner = driver.find_element_by_link_text('Create New Provisioner')
	click_provisioner.click()

	print "CREATING NEW USER..."

	elem = driver.find_element_by_name("fb_saveprovisioner_FBManageProvisionersprov_name")
	elem.send_keys(inp_user_name)


	elem = driver.find_element_by_name("fb_saveprovisioner_FBManageProvisionersprov_id")
	elem.send_keys(inp_provisioner_id)

	elem = driver.find_element_by_name("fb_saveprovisioner_FBManageProvisionerspassword1")
	elem.send_keys(passwd)

	elem = driver.find_element_by_name("fb_saveprovisioner_FBManageProvisionerspassword2")
	elem.send_keys(rep_passwd)


	elem = driver.find_element_by_name("fb_saveprovisioner_FBManageProvisionersemail")
	elem.send_keys(email)

	print "USER DATA ENTERED.."


	elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[3]/input[1]").click()
	# handle the alert
	alert = driver.switch_to_alert()
	alert.accept()

	print "USER CREATED.."


def close():

	driver.close()



########## Function Calls #############

open_link()
login()
create_user()
close()