# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import datetime

# Start the browser and login with standard_user   
print(' browser starting....')
options = ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
print (' Browser started successfully. Navigating to the demo page to login.')
url = 'https://www.saucedemo.com/'
driver.get(url)
user ='standard_user'
passwords ='secret_sauce'
username = driver.find_element(By.ID, 'user-name')
username.send_keys(user)
print(f'Username: {user}')
password = driver.find_element(By.ID, 'password')
password.send_keys(passwords)
print('Password')

login = driver.find_element(By.ID,'login-button')
print( 'Username and password provided')
login.click()

product_page = driver.find_element(By.CLASS_NAME, 'title')
assert product_page.text == "Products", "Error, login failed!"
print('Login to URL with user name standard_user successful!')


print(f'Looking for items to add to cart')

products = []
product_list = driver.find_elements(By.CLASS_NAME, 'inventory_item')

for product in product_list:
    product_name = product.find_element(By.CLASS_NAME, 'inventory_item_name').text
    products.append(product_name)
    add_product_button = product.find_element(By.CLASS_NAME, 'btn_inventory')
    add_product_button.click()
    print(f' {product_name} added to the cart')

cart_badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
final_count = int(cart_badge.text)

assert final_count == len(products), 'The cart count does not match the number of products added'


print(f' All products added to the cart')

print(f' Navigating to cart page ...')
cart = driver.find_element(By.CLASS_NAME,'shopping_cart_link')
cart.click()

print(f' removing product from cart....')
product_cart = driver.find_elements(By.CLASS_NAME,'cart_item')

initial_cart_count = len(product_cart)


print(f'There are {initial_cart_count} products left in the cart')

for product in product_cart:
    product_name = product.find_element(By.CLASS_NAME,'inventory_item_name').text
    remove_btn = product.find_element(By.CLASS_NAME,'cart_button')
    remove_btn.click()

    print(f' {product_name} removed from the cart')

cart_without_products = driver.find_elements(By.CLASS_NAME,'cart_item')

final_cart_count = len(cart_without_products)

assert final_cart_count == 0,'ERROR: Not all products were removed from the cart'
print(f'All products removed from the cart successfully')

