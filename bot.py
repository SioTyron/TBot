import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#--------------------------------------
#           TBot V1.0
#--------------------------------------
# Configuration du navigateur
options = Options()
options.headless = False  # Mode visible pour débogage
driver = webdriver.Chrome(options=options)

# Étape 1 : Accéder au site
print("[INFO] Accès au site web...")
driver.get("http://yourdomain.com/")

time.sleep(3)
# Étape 2 : Attendre le chargement du menu
print("[INFO] Accès à la page1...")
# Navigate to a specific URL
driver.get("http://localhost:8501/page1")

# Étape 3 : Détection du formulaire
print("[INFO] Attente du formulaire de contact...")
form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
)
print("[DEBUG] Formulaire détecté :", form.is_displayed())

# Étape 4 : Remplissage et soumission
print("[INFO] Remplissage du formulaire...")

# Étape 5 : Localiser les champs de saisie
name_field = driver.find_element(By.NAME, "name")
email_field = driver.find_element(By.NAME, "email")
message_field = driver.find_element(By.NAME, "message")

# Étape 6 : Remplir les champs
name_field.send_keys("Your Name")
email_field.send_keys("your.email@example.com")
message_field.send_keys("Your message here")

#Étape 7 : Envoyer le formulaire
submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Envoyer')]")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
time.sleep(1)
driver.execute_script("arguments[0].click();", submit_button)

#Contrôle de la soumission du formulaire
print("[INFO] Formulaire soumis.")

#Étape 8 : Fin du programme
print("[INFO] Successfull")
time.sleep(10)
driver.quit()


