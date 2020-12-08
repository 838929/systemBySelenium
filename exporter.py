import HandleExporterFiles
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# copy parts and copanies to exporter files before upload
HandleExporterFiles.main()

# setting : depend on locations for chrome & chromedriver on PC.
options = Options()
options.binary_location = r"C:\Program Files (x86)\Google\Chrome Beta\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options = options, executable_path=r"C:\Users\ahmed.mosaad\Desktop\Rs\selenium_1\chromedriver.exe")

# Variables .
Username = "ahmed.mosaad@z2data.com"
Password = "Catchmeifyoucan1&"
url = "https://pn.z2data.com:7071/pages/impExp/exporter"
button_Parts_xpath = '//*[@id="navbarSupportedContent"]/div[1]/div[1]/button' 
search_box_xpath = '/html/body/app-root/nb-layout/div/div/div/div/div/nb-layout-column/zapp-pages/body/app-zdataapp/app-importer-exporter/div/div[1]/div/form/div[1]/ng-autocomplete/div[1]/div[1]/input'
Select_File_xpath = '//*[@id="fileUpload"]'
download_template_button_xpath = '/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/zapp-pages/body/app-zdataapp/app-importer-exporter/div/div[1]/div/form/div[2]/button[1]'
export_template_xpath = '/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/zapp-pages/body/app-zdataapp/app-importer-exporter/div/div[1]/div/form/div[2]/button[2]'
LoadingCircle_xpath = "/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/zapp-pages/body/app-zdataapp/app-importer-exporter/div/div[1]/div/form/div[2]/span"


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

def choose_file(export_name):
	# set file according to exporter name  .
	if export_name == 'Replacement Masks Smart Filter':
		file = 'Mask.xlsx'
	elif export_name == 'Part Obsolescence Code':
		file = 'OBS.xlsx'
	elif export_name == 'Replacement NotMatch Parts':
		file = 'NotMatch.xlsx'
	# set file according to exporter name /delete .
	elif export_name == 'PCN Document By ZPart and ZMan':
		file = 'Pcn.xlsx' 
	elif export_name == 'Company Part Validation' :
		file = 'PartCompanyValidation.xlsx'
	elif export_name == 'LC Master Part & Man Exact' :
		file = 'LCMasterInput.xlsx'
	elif export_name == 'Lifecycle By Processing Date' :
		file = 'LifecycleEXByProcessingDate.xlsx'
	else :
		print('exporter name not added yet .')
	return file

def export_(export_name, search_box_xpath=search_box_xpath ):
	driver.refresh()
	driver.refresh()
	time.sleep(3)
	

	wait.until(ec.presence_of_element_located((By.XPATH, search_box_xpath)))
	driver.find_element_by_xpath(search_box_xpath).send_keys(export_name)
	wait.until(ec.element_to_be_clickable((By.LINK_TEXT, export_name)))
	driver.find_element_by_partial_link_text(export_name).click()
	time.sleep(3)
	
	# activate necessary elements related to upload file before upload file .
	# wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/zapp-pages/body/app-zdataapp/app-importer-exporter/div/div[1]/div/form/div[2]/app-custom-upload/span")))
	# driver.find_element_by_xpath("/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/zapp-pages/body/app-zdataapp/app-importer-exporter/div/div[1]/div/form/div[2]/app-custom-upload/span").click()
	driver.find_element_by_xpath("/html/body/app-root/nb-layout/div[1]/div/div/div/div/nb-layout-column/zapp-pages/body/app-zdataapp/app-importer-exporter/div/div[1]/div/form/div[2]/app-custom-upload/span/i").click()
	
	file = choose_file(export_name)

	# upload file .
	driver.find_element_by_xpath(Select_File_xpath).send_keys(r"C:\Users\ahmed.mosaad\Desktop\Rs\system\exporter_files\\" + file)
	time.sleep(5)

	# click  import template to get exported data .
	driver.find_element_by_xpath(export_template_xpath).click()
	time.sleep(7)
	# make sure file imported by disapperaing of LoadingCircle 
	print(file + " Done exported")





## export options .
# export_('Replacement Masks Smart Filter')
# export_('Part Obsolescence Code')
# export_('Replacement NotMatch Parts')

# export_('PCN Document By ZPart and ZMan')
# export_('Company Part Validation')
# export_('LC Master Part & Man Exact')
# export_('Lifecycle By Processing Date')










































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
	# 		driver.find_element_by_xpath(export_template_xpath).click()
	# 		break

	# 	else:
	# 		driver.refresh()
	# 		driver.find_element_by_xpath(search_box_xpath).send_keys(export_name)
	# 		driver.find_element_by_partial_link_text(export_name).click()
	# 
####################################################################################
	# driver.execute_script("arguments[0].click();", upload_button)