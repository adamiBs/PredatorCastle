import selenium
import re
import time
from selenium import webdriver
d = webdriver.Chrome()

usr_name = 'aviron@tutanota.com'
usr_pass = 'Aviron669!@#'

def mainn():
  login(usr_name,usr_pass)

def login(username,usr_pass):
  d.get("https://www.facebook.com")
  elm_email = d.find_element_by_id("email")
  elm_pass = d.find_element_by_id("pass")
  elm_login = d.find_element_by_id("loginbutton")
  
  elm_email.send_keys(usr_name)
  elm_pass.send_keys(usr_pass)
  elm_login.click()

#~~~~~~~~~~~~~ Working Methods
def getFriends(usr_id):
    d.get("https://www.facebook.com/search/" + usr_id +"/friends")
    var_cont = True
    last_height = 0
    while var_cont:
        d.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(4)
        height = d.execute_script("return document.body.scrollHeight")
        var_cont = ( height != last_height )
        last_height = height
    strr = d.page_source
    lst_ids = [strr[m.start()+15:m.start()+30] for m in list(re.finditer("profile.php",strr))]
    lst_ids = [idd[0:re.search("[0-9]+",idd).end()] for idd in lst_ids]
    return lst_ids

def getUserLikes(usr_id):
    


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Ideas  
def extractUserIdsFromUrl(url):
    return 1
def getFriendsListForUser(usr_id):
    return 1
def getFriends(usr_id):
    return 1
def getMutualFriends(usr_id):
    return 1
def extractIdsFromHtml(html):
    return 1
def extractGroupsFromHtml(html):
    return 1

#~~~~~~~~~~~~~~~~ User JSON export handler
#groups
#friends
#profile picture
#picture related sites
#mutual friends with fictive users
#date of create account
#dates of friends added
#friends in group


mainn()
