"""import keyword
print(keyword.kwlist)"""
#print("Hello Yaman")
#name = input ("enter your name")
#print(name)


# Data Type

"""1. Number 
2. String
3. Boolens"""



"""a,b,c = 1,2,3

print(a)
print(b)
print(c)"""


"""x = 5 # int
pi = 4.76 #float
name = "yaman"# string"""



"""firstVal = int(input("enter the first val"))  
secondVal = int(input("enter the second val"))

print (firstVal + secondVal)"""


                   #Table


"""user_input =int(input("enter your number"))

print(f"{user_input}*1={user_input*1}")
print(f"{user_input}*2={user_input*2}")
print(f"{user_input}*3={user_input*3}")
print(f"{user_input}*4={user_input*4}")
print(f"{user_input}*5={user_input*5}")
print(f"{user_input}*6={user_input*6}")
print(f"{user_input}*7={user_input*7}")
print(f"{user_input}*8={user_input*8}")
print(f"{user_input}*9={user_input*9}")
print(f"{user_input}*10={user_input*10}")
"""







  #Test Case


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Chrome open
driver = webdriver.Chrome()

# 2. Google open
driver.get("https://www.google.com")

# 3. Wait for page load
time.sleep(2)

# 4. Search box find karo
search = driver.find_element(By.NAME, "q")

# 5. Type karo
search.send_keys("Pakistan")

time.sleep(10)

# 6. Enter press karo
search.send_keys(Keys.RETURN)

# 7. Wait result dekhne ke liye
time.sleep(5)

# 8. Browser close
driver.quit()




"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

driver.find_element(By.NAME, "q").send_keys("Pakistan", Keys.RETURN)
time.sleep(5)
driver.quit()"""




"""a = "yaman"
b = 23
print(type(a))
print(len(a)) 
print(a[4])
print(type(b))"""

"""first_inut = int(input("input"))

print(f"{first_inut}*1= {first_inut*1}")
print(f"{first_inut}*2= {first_inut*2}")
print(f"{first_inut}*4= {first_inut*4}")
print(f"{first_inut}*5= {first_inut*5}")
print(f"{first_inut}*6= {first_inut*6}")"""




"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Google Maps open
driver.get("https://maps.google.com")

# Wait
time.sleep(2)

# Search box
search = driver.find_element(By.NAME, "q")

# City search
search.send_keys("Lahore Pakistan")

# Enter
search.send_keys(Keys.RETURN)

# Wait for map loading
time.sleep(5)

driver.quit()"""




"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Browser open
driver = webdriver.Chrome()

# Browser maximize
driver.maximize_window()

# Google open
driver.get("https://www.google.com")

# Wait for loading
time.sleep(2)

# Search box find
search = driver.find_element(By.NAME, "q")

# Search text type
search.send_keys("Pakistan")

# Press Enter
search.send_keys(Keys.RETURN)

# Wait for results
time.sleep(3)

# Page title print
print("Page Title is:")
print(driver.title)

# Verify title
if "Pakistan" in driver.title:
    print("TEST CASE PASSED")
else:
    print("TEST CASE FAILED")

# Wait before close
time.sleep(5)

# Close browser
driver.quit()"""