import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Baca data dari akun.txt dan code.txt
with open('akun.txt', 'r') as akun_file:
    akun_lines = [line.strip().split('|') for line in akun_file.readlines()]

with open('code.txt', 'r') as code_file:
    code_text = code_file.read().strip()

# Inisialisasi WebDriver (misal, menggunakan Chrome)
driver = webdriver.Chrome()

try:
    # Loop melalui setiap akun di akun.txt
    for url, username in akun_lines:
        print(f"Proses URL: {url} | USERNAME: {username}")  # Tambahkan print di sini
        
        # Buka URL login
        driver.get(url)
        time.sleep(10)  # Jeda 15 detik
        
        # Step #3: Select frame by index
        driver.switch_to.frame(0)
        time.sleep(3)

        # Step #4: Click username field
        driver.find_element(By.NAME, "username").click()
        time.sleep(3)
        
        # Step #5: Type username
        driver.find_element(By.NAME, "username").send_keys(username)
        time.sleep(3)
        
        # Step #6: Click password field
        driver.find_element(By.NAME, "password").click()
        time.sleep(3)
        
        # Step #7: Type password
        driver.find_element(By.NAME, "password").send_keys("AyLevy123@")
        time.sleep(3)
        
        # Step #8: Click submit button
        driver.find_element(By.CSS_SELECTOR, ".ButtonStyles-button").click()
        time.sleep(10)
        
        # Buka halaman automation jobs
        driver.get(f"{url}/p/main/automation/jobs")
        time.sleep(10)  # Jeda 5 detik

        # Klik tombol "Create script"
        create_script_button = driver.find_element(By.XPATH, "//span[@class='XTextStyles-ellipsis' and text()='Create script']")
        create_script_button.click()
        time.sleep(5)  # Jeda 5 detik

        # Klik editor dan paste kode
        editor = driver.find_element(By.XPATH, "//div[@class='cm-line' and text()='}']")
        editor.click()
        editor.send_keys(Keys.CONTROL + "a")
        editor.send_keys(code_text)

        time.sleep(5)  # Jeda 5 detik

        # Klik tombol "Commit"
        commit_button = driver.find_element(By.XPATH, "//button[@type='button' and contains(@class, 'ksc-205') and contains(@class, 'XButtonStyles-Kind-primary')]//span[text()='Commit']")
        commit_button.click()
        time.sleep(3)  # Jeda 3 detik

        # Konfirmasi komit
        confirm_commit_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'ksc-205') and contains(@class, 'XButtonStyles-Kind-primary')]//span[text()='Commit']")
        confirm_commit_button.click()

        time.sleep(5)  # Jeda 5 detik sebelum menutup tab

    print("Selesai")

finally:
    driver.quit()  # Tutup browser setelah selesai
