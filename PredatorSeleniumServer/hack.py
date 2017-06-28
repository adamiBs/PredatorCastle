import selenium
import re
import time
from selenium import webdriver
d = webdriver.Chrome()

usr_name = 'aviron@tutanota.com'
usr_pass = 'Aviron669!@#'

def mainn():
  login(usr_name,usr_pass)

def login(username,usr_password):
  d.get("https://www.facebook.com")
  elm_email = d.find_element_by_id("email")
  elm_pass = d.find_element_by_id("pass")
  elm_login = d.find_element_by_id("loginbutton")
  
  elm_email.send_keys(username)
  elm_pass.send_keys(usr_password)
  elm_login.click()

#~~~~~~~~~~~~~ User Methods
def getFriends(usr_id):
    d.get("https://www.facebook.com/search/" + usr_id + "/friends")
    scrollDown()
    strr = d.page_source
    lst_ids = [strr[m.start()+15:m.start()+30] for m in list(re.finditer("profile.php",strr))]
    lst_ids = [idd[0:re.search("[0-9]+",idd).end()] for idd in lst_ids]
    return lst_ids

def getMutualFriendsCount(usr_id1, usr_id2):
    d.get("https://www.facebook.com/browse/mutual_friends/?uid=" + usr_id1 + "&node=" + usr_id2)
    scrollDown()
    pageSrc = d.page_source
    lst_ids = [pageSrc[m.start()+15:m.start()+30] for m in list(re.finditer("profile.php",pageSrc))]
    return len(lst_ids)

def getMutualFriendsList(usr_id1, usr_id2):
    d.get("https://www.facebook.com/browse/mutual_friends/?uid=" + usr_id1 + "&node=" + usr_id2)
    scrollDown()
    pageSrc = d.page_source
    lst_ids = [pageSrc[m.start()+15:m.start()+30] for m in list(re.finditer("profile.php",pageSrc))]
    lst_ids = [idd[0:re.search("[0-9]+",idd).end()] for idd in lst_ids]
    return lst_ids

#~~~~~~~~~~~~~ Groups Methods
def getGroupMembers(groupName):
    d.get("https://www.facebook.com/groups/" + groupName + '/members')
    
#~~~~~~~~~~~~~ Common Methods
def scrollDown():
    var_cont = True
    last_height = 0
    while var_cont:
        d.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(4)
        height = d.execute_script("return document.body.scrollHeight")
        var_cont = ( height != last_height )
        last_height = height

def ConvertDataToFile(data):
    return 1
    
    


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Ideas  
def extractUserIdsFromUrl(url):
    return 1
def getFriendsListForUser(usr_id):
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
