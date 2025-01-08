from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "path"
username = "username"
password = "password"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

def click_remove_buttons():
    try:
        # Navigate to profile page
        driver.get("https://www.instagram.com/username")
        print("Navigating to profile...")

        # Wait for profile page to load by checking for profile picture
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt*='profile']"))
        )
        print("Profile page loaded successfully!")

        # Wait for the followers button to be clickable
        followers_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'followers')]"))
        )
        followers_button.click()
        print("Followers button clicked!")

        # Wait for the first remove button to be visible and clickable
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x16n37ib.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.xs83m0k.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > .x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x972fbf.xcfux6l.x1qhh985.xm0m39n.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x18d9i69.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x78zum5.x1f6kntn.xwhw2v2.x10w6t97.xl56j7k.x17ydfre.x1swvt13.x1pi30zi.x1n2onr6.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.x1gjpkn9.x5n08af.xsz8vos")
            )
        )

        # Click on the first remove button
        remove_button = driver.find_element(By.CSS_SELECTOR, ".x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x16n37ib.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.xs83m0k.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > .x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x972fbf.xcfux6l.x1qhh985.xm0m39n.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x18d9i69.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x78zum5.x1f6kntn.xwhw2v2.x10w6t97.xl56j7k.x17ydfre.x1swvt13.x1pi30zi.x1n2onr6.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.x1gjpkn9.x5n08af.xsz8vos")
        remove_button.click()
        print("First remove button clicked!")

        # Wait for the second remove button to be visible and clickable
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "button._a9--._ap36._a9-_")
            )
        )

        # Click on the second remove button
        remove_button_2 = driver.find_element(By.CSS_SELECTOR, "button._a9--._ap36._a9-_")
        remove_button_2.click()
        print("Second remove button clicked!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Start the process
try:
    # Log in to Instagram
    driver.get("https://www.instagram.com/accounts/login/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    # Wait for login to complete
    WebDriverWait(driver, 15).until(lambda d: "instagram.com" in d.current_url and "login" not in d.current_url)
    print("Login successful!")

    # Repeat the process of clicking the remove buttons 100 times
    for _ in range(100):
        click_remove_buttons()
        time.sleep(2)  # Wait 2 seconds between actions to avoid being flagged as a bot

finally:
    driver.quit()
