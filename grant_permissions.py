from selenium import webdriver
from selenium.webdriver.common.keys import Keys



from const import url,usr,pwd,driver


inp_user_name = 'adil'
inp_provisioner_id = '455324'
passwd = '12345'
rep_passwd = '12345'
email = 'adil@gmail.com'



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





def grant_permission():


	click_manage = driver.find_element_by_link_text('Manage Provisioners')
	click_manage.click()

	print "MANAGE LINK ...."

	click_manage_permissions = driver.find_element_by_xpath('/html/body/center/table[2]/tbody/tr[2]/td/form/div/a[3]')
	click_manage_permissions.click()

	print "MANAGE PERMISSIONS........"

	provisoner_id = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[1]/table/tbody/tr[2]/td[2]/input")
	provisoner_id.send_keys(inp_provisioner_id)

	print "ID PROVIDED"

	search_prov_id = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[1]/table/tbody/tr[4]/td[2]/input")
	search_prov_id.click()

	print "SEARCH DONE....."

	## provide permissions....


	elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[2]/table/tbody/tr[3]/td[1]/input")
	elem.click()

	elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[2]/table/tbody/tr[3]/td[5]/input")
	elem.click()

	elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[2]/table/tbody/tr[3]/td[6]/input")
	elem.click()

	elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[2]/table/tbody/tr[3]/td[12]/input")
	elem.click()

	elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[2]/table/tbody/tr[3]/td[16]/input")
	elem.click()

	print "PERMISSIONS SELECTED........."

	elem = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr[2]/td/form/div[3]/div[4]/input[1]")
	elem.click()

	print "SEARCH DONE.........."



def close():

	driver.close()

########## Function Calls #############

open_link()
login()
grant_permission()
close()