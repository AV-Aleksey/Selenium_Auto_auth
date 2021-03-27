from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome('./chromedriver')
driver.get("https://passport.yandex.ru/auth?origin=uslugi&retpath=https%3A%2F%2Fuslugi.yandex.ru%2Fcab%2Forders%3Fcompletely_moderated%3D1%26rubric%3D%252Fremont-i-stroitel_stvo%252Fbetonnye-raboty%26rubric%3D%252Fremont-i-stroitel_stvo%252Fburenie%26rubric%3D%252Fremont-i-stroitel_stvo%252Fdorojnoe-stroitel_stvo%26rubric%3D%252Fremont-i-stroitel_stvo%252Fdrugoe%26rubric%3D%252Fremont-i-stroitel_stvo%252Fdveri-i-zamki%26rubric%3D%252Fremont-i-stroitel_stvo%252Felektromontajnye-raboty%26rubric%3D%252Fremont-i-stroitel_stvo%252Ffasadnye-raboty%26rubric%3D%252Fremont-i-stroitel_stvo%252Ffundament%26rubric%3D%252Fremont-i-stroitel_stvo%252Fkladka-pecej-i-kaminov%26rubric%3D%252Fremont-i-stroitel_stvo%252Fkladocnye-raboty%26rubric%3D%252Fremont-i-stroitel_stvo%252Fkrovel_nye-raboty%26rubric%3D%252Fremont-i-stroitel_stvo%252Fmaster-na-cas%26rubric%3D%252Fremont-i-stroitel_stvo%252Fmebel_%26rubric%3D%252Fremont-i-stroitel_stvo%252Foboi-i-malarnye-raboty%26rubric%3D%252Fremont-i-stroitel_stvo%252Fohrannye-sistemy-i-kontrol_-dostupa%26rubric%3D%252Fremont-i-stroitel_stvo%252Fokna-i-balkony%26rubric%3D%252Fremont-i-stroitel_stvo%252Fozelenenie%26rubric%3D%252Fremont-i-stroitel_stvo%252Fplitocnye-raboty%26rubric%3D%252Fremont-i-stroitel_stvo%252Fpoly-i-napol_nye-pokrytia%26rubric%3D%252Fremont-i-stroitel_stvo%252Fpotolki%26rubric%3D%252Fremont-i-stroitel_stvo%252Fremont-kvartir-i-domov%26rubric%3D%252Fremont-i-stroitel_stvo%252Fremont-ofisa%26rubric%3D%252Fremont-i-stroitel_stvo%252Frol_stavni-i-sekzionnye-vorota%26rubric%3D%252Fremont-i-stroitel_stvo%252Fsantehniceskie-raboty-i-otoplenie%26rubric%3D%252Fremont-i-stroitel_stvo%252Fsnos-i-demontaj%26rubric%3D%252Fremont-i-stroitel_stvo%252Fstekol_nye-uslugi%26rubric%3D%252Fremont-i-stroitel_stvo%252Fstroitel_stvo-ban_%252C-saun-i-bassejnov%26rubric%3D%252Fremont-i-stroitel_stvo%252Fstroitel_stvo-domov-i-kottedjej%26rubric%3D%252Fremont-i-stroitel_stvo%252Fstroitel_stvo-garajej%26rubric%3D%252Fremont-i-stroitel_stvo%252Fsvarocnye-raboty%26rubric%3D%252Fremont-i-stroitel_stvo%252Fumnyj-dom%26rubric%3D%252Fremont-i-stroitel_stvo%252Fvodosnabjenie-i-kanalizazia%26rubric%3D%252Fremont-i-stroitel_stvo%252Fzabory-i-ograjdenia%26rubric%3D%252Fremont-i-stroitelstvo%252Fotdelka-derevyannyih-domov-ban-saun%26rubric%3D%252Fremont-i-stroitel_stvo%252Fventilazia%26type%3Dnew&backpath=https%3A%2F%2Fuslugi.yandex.ru")

login = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'passp-field-login')))
login.send_keys('сюда логин')

btnLogin = driver.find_element_by_class_name('Button2_type_submit').click()


password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'passp-field-passwd')))
password_field.send_keys('сюда пасс')

driver.find_element_by_class_name('Button2_type_submit').click()

driver.get_log()
