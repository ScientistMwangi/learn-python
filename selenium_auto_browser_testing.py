from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

# find singing link
signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("scientistmwangi@gmail.com")
password_box = browser.find_element_by_id("password")
password_box.send_keys("Admin101#")
password_box.submit()

browser_source = browser.page_source
profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
print(link_label)
assert "ramsey" in link_label

browser.close()