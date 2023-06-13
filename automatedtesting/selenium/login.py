# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import datetime

#create log datetime
def log():
    time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return ("log" + time)

# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import datetime


def log():
    time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return ("LOG " + time)

def driver_func():
    
    print(f'{log()} Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    print (f'{log()} Browser started successfully. Navigating to the demo page to login.')
    return driver

# Start the browser and login with standard_user
def login (driver, user, password):
    url = 'https://www.saucedemo.com/'
    driver.get(url)

    username_input = driver.find_element(By.ID, 'user-name')
    username_input.send_keys(user)
    print(f'{log()} Username: {user} provided')

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    print(f'{log()} Password provided')

    login_btn = driver.find_element(By.ID,'login-button')
    print(f'{log()} Username and password submitted')
    login_btn.click()

    product_page_header = driver.find_element(By.CLASS_NAME, 'title')
    assert product_page_header.text == "Products", "Error, login failed!"
    print(f'{log()} Login successful')

def get_cart_count(driver, class_name):
    cart_badge = driver.find_element(By.CLASS_NAME, class_name)
    return int(cart_badge.text)

def add_products(driver):
    print(f'{log()} Starting to add products to the cart')

    products = []
    product_containers = driver.find_elements(By.CLASS_NAME, 'inventory_item')

    for product in product_containers:
        product_name = product.find_element(By.CLASS_NAME, 'inventory_item_name').text
        products.append(product_name)
        add_product_button = product.find_element(By.CLASS_NAME, 'btn_inventory')
        add_product_button.click()

        print(f'{log()} {product_name} added to the cart')
    
    final_cart_count = get_cart_count(driver,'shopping_cart_badge')

    assert final_cart_count == len(product_containers), 'ERROR: The cart count does not match the number of products added'

    print(f'{log()} Cart count matches with the number of products added')
    print(f'{log()} All products added to the cart')

def remove_products(driver):
    print(f'{log()} Navigating to cart page')
    cart = driver.find_element(By.CLASS_NAME,'shopping_cart_link')
    cart.click()

    print(f'{log()} Starting to remove products to the cart')
    cart_with_products = driver.find_elements(By.CLASS_NAME,'cart_item')

    initial_cart_count = len(cart_with_products)
    assert initial_cart_count == 6, 'ERROR: All products are not in the cart'

    print(f'{log()} There are {initial_cart_count} products left in the cart')

    for product in cart_with_products:
        product_name = product.find_element(By.CLASS_NAME,'inventory_item_name').text
        remove_btn = product.find_element(By.CLASS_NAME,'cart_button')
        remove_btn.click()

        print(f'{log()} {product_name} removed from the cart')

    cart_without_products = driver.find_elements(By.CLASS_NAME,'cart_item')

    final_cart_count = len(cart_without_products)

    assert final_cart_count == 0,'ERROR: Not all products were removed from the cart'
    print(f'{log()} All products removed from the cart successfully')

if __name__ == "__main__":
    driver_active = driver_func()
    login(driver_active, 'standard_user', 'secret_sauce')
    add_products(driver_active)
    remove_products(driver_active)
    



