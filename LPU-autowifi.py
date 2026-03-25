import subprocess
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

USERNAME = "12509995"
PASSWORD = ""

URL = "https://internet.lpu.in/24online/webpages/client.jsp"


# 🔍 Get current connected WiFi
def get_connected_wifi():
    try:
        result = subprocess.check_output("netsh wlan show interfaces", shell=True).decode(errors="ignore")
        for line in result.split("\n"):
            if "SSID" in line and "BSSID" not in line:
                return line.split(":")[1].strip()
    except:
        return None


# 🔍 Find valid LPU WiFi (exclude jioNet)
def find_lpu_wifi():
    result = subprocess.check_output("netsh wlan show networks", shell=True).decode(errors="ignore")

    for line in result.split("\n"):
        if "SSID" in line:
            ssid = line.split(":")[1].strip()

            if "LPU" in ssid.upper() and "JIONET@LPU" not in ssid.upper():
                print(f"📡 Found valid WiFi: {ssid}")
                return ssid

    return None


# 🔌 Connect WiFi
def connect_wifi(ssid):
    print(f"🔌 Connecting to {ssid}...")
    subprocess.call(f'netsh wlan connect name="{ssid}"', shell=True)
    time.sleep(5)


# 🌐 Wait for internet
def wait_for_internet(timeout=20):
    print("🌐 Waiting for internet...")

    for _ in range(timeout):
        try:
            requests.get("http://www.google.com", timeout=3)
            print("🟢 Internet ready")
            return True
        except:
            time.sleep(1)

    print("❌ Internet not ready")
    return False


# 🌐 Check if login required
def is_login_required():
    try:
        r = requests.get(URL, timeout=5)
        text = r.text.lower()

        if "username" in text and "password" in text:
            return True
        return False
    except:
        return True


# 🌐 Login (auto close browser)
def login():
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")

    driver = webdriver.Edge(options=options)

    driver.get(URL)
    time.sleep(3)

    try:
        print("🔑 Filling credentials...")

        driver.find_element(By.NAME, "username").send_keys(USERNAME)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)

        # checkbox
        checkbox = driver.find_element(By.ID, "agreepolicy")
        driver.execute_script("arguments[0].click();", checkbox)
        time.sleep(1)

        driver.execute_script("policycheck();")
        time.sleep(1)

        # login
        print("🚀 Logging in...")
        driver.execute_script("appendUserName();")

        time.sleep(5)

        if "successfully logged in" in driver.page_source.lower():
            print("🟢 LOGIN SUCCESS → closing browser")
            driver.quit()
            return True
        else:
            print("❌ LOGIN FAILED → closing browser")
            driver.quit()
            return False

    except Exception as e:
        print("❌ Error:", e)
        driver.quit()
        return False


# 🔁 MAIN LOOP
print("🚀 FINAL AUTO WIFI LOGIN SYSTEM STARTED\n")

while True:
    current = get_connected_wifi()

    if current and "LPU" in current.upper() and "JIONET@LPU" not in current.upper():
        print(f"🟢 Connected to {current}")

        if is_login_required():
            print("🔴 Login required → starting login...")
            login()
        else:
            print("🟢 Already logged in")

    else:
        ssid = find_lpu_wifi()

        if ssid:
            connect_wifi(ssid)

            if wait_for_internet():
                login()
        else:
            print("❌ No valid LPU WiFi found")

    time.sleep(15)