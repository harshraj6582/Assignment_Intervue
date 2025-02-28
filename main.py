from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (e.g., Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")  # Ignores SSL errors
options.add_argument("--disable-blink-features=AutomationControlled")  # Prevents detection as bot
options.add_argument("--disable-dev-shm-usage")  # Reduces memory issues
options.add_argument("--no-sandbox")  # Bypasses sandbox restrictions
options.add_argument("--ignore-ssl-errors")
options.add_argument("--allow-insecure-localhost")

driver = webdriver.Chrome(options=options)

try:
    # Open the website
    driver.get("https://www.intervue.io/")

    # Wait for the navbar element to be visible and scroll it into view
    navbar_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.iv-homepage-navbar-7.header-links[data-text="Why Intervue?"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", navbar_element)

    # Hover over navbar elements
    actions = ActionChains(driver)
    nav_elements = [
        ('a.iv-homepage-navbar-7.header-links[data-text="Products"]', 5),
        ('a#solutions', 5),
        ('a#pricing', 5),
        ('a#resources', 5),
        ('a#contact-us', 2)
    ]

    for selector, wait_time in nav_elements:
        element = driver.find_element(By.CSS_SELECTOR, selector)
        actions.move_to_element(element).perform()
        time.sleep(wait_time)

    # Click the "Login" button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "loginBtn"))
    )
    login_button.click()

    # Switch to the new tab
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])

    # Wait for the second "Login" button and click it
    second_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.AccessAccount-ColoredButton'))
    )
    second_login_button.click()

    # Input the email address
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_email"))
    )
    email_input.send_keys("211430@juitsolan.in")

    # Input the password
    password_input = driver.find_element(By.ID, "login_password")
    password_input.send_keys("Ayushraj6582@")

    # Click the login button after entering credentials
    login_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ant-btn.btn.LoginDarkButton-sc-1ertvag-0.isOnQC.ant-btn-primary.ant-btn-lg.ant-btn-block"))
    )
    login_submit_button.click()

    # Add a wait time after login to ensure the page is fully loaded
    time.sleep(5)

    # Find and click the search placeholder span
    search_span = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "span.search_placeholder"))
    )
    search_span.click()
    print("Found and clicked the search placeholder span")

    # Wait for the search input field with the specific placeholder and class
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input.SearchBox__StyledInput-ctnsh0-4.lhwsuL[placeholder="Type what you want to search for"]'))
    )
    
    # Enter "hello" in the search field
    search_input.send_keys("hello")
    print("Entered 'hello' in the search field")
    
    # Wait a moment for suggestions to appear
    time.sleep(5)
    
    # Find and click the search result div
    search_result_div = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.SearchThrough__PlaceholderText-sc-8f4vh4-0'))
    )
    search_result_div.click()
    print("Clicked on search result to view results")

    # Wait for search results to load
    time.sleep(5)

    # Ensure the search completes before proceeding
    print("Search completed successfully")
    print("Current page title after search:", driver.title)

    try:
        # Click on the profile dropdown
        profile_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ant-dropdown-link.ProfileHeader__StyedDropdownHoverLink-sc-1gwp6c1-3'))
        )
        profile_dropdown.click()
        print("Clicked on user profile dropdown")

        # Wait for dropdown menu to appear
        time.sleep(2)

        # Create action chains for hovering over menu items
        actions = ActionChains(driver)

        # Hover over each menu item for 2 seconds
        menu_items = [
            'a[href="/profile/billing"]',
            'a[href="/profile/settings/team"]',
            'a[href="/profile/settings/integrations"]',
            'a[href="/profile/settings/user"]'
        ]

        for item_selector in menu_items:
            try:
                menu_item = WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, item_selector))
                )
                actions.move_to_element(menu_item).perform()
                print(f"Hovering over {item_selector}")
                time.sleep(2)
            except:
                print(f"Could not hover over {item_selector}")

        # Finally, click on the logout button
        logout_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/logout"][style*="color: rgb(244, 67, 54)"]'))
        )
        logout_link.click()
        print("Clicked on Logout")

        # Wait for logout to complete
        time.sleep(5)

        print("Logout completed successfully")
        print("Current page title after logout:", driver.title)

    except Exception as e:
        print("An error occurred in the profile dropdown section:", str(e))

except Exception as e:
    print("An error occurred:", str(e))
