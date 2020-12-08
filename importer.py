from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# setting : depend on locations for chrome & chromedriver on PC.
options = Options()
options.binary_location = r"C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r"C:\Users\ahmed.mosaad\Desktop\Rs\selenium_1\chromedriver.exe")

# Variables .
Username = "ahmed.mosaad@z2data.com"
Password = "Catchmeifyoucan1&"
url = "https://pn.z2data.com:7071/pages/impExp/importer/"
button_Parts_xpath = '//*[@id="navbarSupportedContent"]/div[1]/div[1]/button' 
search_box_xpath = '/html/body/app-root/nb-layout/div/div/div/div/div/nb-layout-column/zapp-pages/body/app-zdataapp/app-importer-exporter/div/div[1]/div/form/div[1]/ng-autocomplete/div[1]/div[1]/input'
Select_File_xpath = '//*[@id="fileUpload"]'
download_template_button_xpath = '/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/zapp-pages/body/app-zdataapp/app-importer-exporter/div/div[1]/div/form/div[2]/button[1]'
import_template_xpath = '/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/zapp-pages/body/app-zdataapp/app-importer-exporter/div/div[1]/div/form/div[2]/button[2]'



#  open url, maximize window and wait 5sec .
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

# login by name and password , click sign in and wait . 
driver.find_element_by_id("Username").send_keys(Username)
driver.find_element_by_id("Password").send_keys(Password)
driver.find_element_by_name("button").click()
driver.implicitly_wait(5)


# activate mouse indicator on page before refreshing by selecting "Parts" button and make refresh.
driver.refresh()
wait = WebDriverWait(driver, 10000) # set wait variable to use in elements that need time to  be clickable or appear . 
wait.until(ec.element_to_be_clickable((By.XPATH, button_Parts_xpath)))
driver.find_element(By.XPATH, button_Parts_xpath).click()

def choose_file(importer_name):
	# set file according to exporter name /insert .
	if importer_name == 'Replacment Mask Parts':
		file = 'Mask.xlsx'
	elif importer_name == 'Part Obsolescence Code':
		file = 'obs.xlsx'
	elif importer_name == 'Replacement NotMatch Insert':
		file = 'NotMatch.xlsx'
	# set file according to exporter name /delete .
	elif importer_name == 'Replacment Mask Delete By Part & Replacment Part':
		file = 'DeleteMask.xlsx' 
	elif importer_name == 'Delete Part ObsolescenceCode' :
		file = 'Deleteobs.xlsx'
	elif importer_name == 'Replacement NotMatch Delete' :
		file = 'DeleteNotMatch.xlsx'
	else :
		print('importer not supported yet .')
	return file

def import_(importer_name, search_box_xpath=search_box_xpath ):
	driver.refresh()
	time.sleep(3)
	driver.refresh()
	

	wait.until(ec.presence_of_element_located((By.XPATH, search_box_xpath)))
	driver.find_element_by_xpath(search_box_xpath).send_keys(importer_name)
	driver.find_element_by_partial_link_text(importer_name).click()
	time.sleep(3)
	
	# activate necessary elements related to upload file before upload file .
	driver.find_element_by_xpath("/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/zapp-pages/body/app-zdataapp/app-importer-exporter/div/div[1]/div/form/div[2]/app-custom-upload/span").click()
	driver.find_element_by_xpath("/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/zapp-pages/body/app-zdataapp/app-importer-exporter/div/div[1]/div/form/div[2]/app-custom-upload/span/i").click()
	
	file = choose_file(importer_name)

	# upload file .
	driver.find_element_by_xpath(Select_File_xpath).send_keys(r"C:\Users\ahmed.mosaad\Desktop\Rs\system\importer_files\\" + file)
	time.sleep(5)

	# click import .
	driver.find_element_by_xpath(import_template_xpath).click()
	time.sleep(5)
	print(file + " Done imported")

## insert options .
# import_('Replacment Mask Parts')
# import_('Part Obsolescence Code')
# import_('Replacement NotMatch Insert')

## delete options .
# import_('Replacment Mask Delete By Part & Replacment Part')
# import_('Delete Part ObsolescenceCode')
# import_('Replacement NotMatch Delete')











































# trials

#selenium.common.exceptions.JavascriptException: Message: javascript error: Cannot set property 'value' of undefined
	# driver.execute_script("""
 #     	cardNumberInput = document.getElementsByClassName('ng-tns-c11-1')
 #     	cardNumberInput[4].value = "fileUpload"
 #                      """)



 # upload_btn = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.XPATH, Select_File_xpath_1))).send_keys("C://Users/Mos2d/Desktop/selenium/PartObsolescenceCodeInput.xlsx")

################################################################################################
	# while True:
	# 	if driver.find_element_by_xpath(Select_File_xpath_1):
	# 		driver.find_element_by_xpath(Select_File_xpath_1).send_keys("C://Users/Mos2d/Desktop/selenium/PartObsolescenceCodeInput.xlsx")
	# 		time.sleep(5)
	# 		driver.find_element_by_xpath(import_template_xpath).click()
	# 		break

	# 	else:
	# 		driver.refresh()
	# 		driver.find_element_by_xpath(search_box_xpath).send_keys(importer_name)
	# 		driver.find_element_by_partial_link_text(importer_name).click()
	# 
####################################################################################
	# driver.execute_script("arguments[0].click();", upload_button)