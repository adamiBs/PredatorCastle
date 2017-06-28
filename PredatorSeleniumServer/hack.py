import selenium
from selenium import webdriver
d = webdriver.Chrome()

usr_name = 'aviron@tutanota.com'
usr_pass = 'Aviron669!@#'

mainn()

def function mainn():
    login(usr_name,usr_pass)

def function login(username,pass):
    d.get("https://www.facebook.com")
    elm_email = d.find_element_by_id("email")
    elm_pass = d.find_element_by_id("pass")
    elm_login = d.find_element_by_id("loginbutton")
    
    elm_email.send_keys(usr_name)
    elm_pass.send_keys(usr_pass)
    elm_login.click()


#~~~~~~~~~~~~~ Navigation
def function checkUserExists(usr_id):
    
def function extractUserIdsFromUrl(url):
def function getFriendsListForUser(usr_id):
def function getFriends(usr_id):
def function getMutualFriends(usr_id):
    
#~~~~~~~~~~~~~~~~ HTML
def function extractIdsFromHtml(html):
def function extractGroupsFromHtml(html):

#~~~~~~~~~~~~~~~~ User JSON export handler
