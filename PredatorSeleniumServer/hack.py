import selenium
import re
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import datetime
from datetime import datetime

usr_name = 'aviron@tutanota.com'
usr_pass = 'Aviron669!@#'


def login(username, usr_password):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    d = webdriver.Chrome(chrome_options=chrome_options)
    d.get("https://www.facebook.com")
    elm_email = d.find_element_by_id("email")
    elm_pass = d.find_element_by_id("pass")
    elm_login = d.find_element_by_id("loginbutton")

    elm_email.send_keys(username)
    elm_pass.send_keys(usr_password)
    elm_login.click()
    return d


# ~~~~~ User Methods
def getFriends(usr_id):
    d = login(usr_name, usr_pass)
    d.get("https://facebook.com/search/" + usr_id + "/friends")
    scrollDown(d)
    return extractIdsFromHtml(d.page_source, d)

def getFriendsStatistics(usr_id):
    suspectData = {
        "work": '',
        "city": '',
        "study": ''
    }
    data = {
        "gender":
            {
                "males": 0,
                "females": 0,
                "unknown": 0
            },
        "amount": 0,
        "common":
            {
                "work": 0,
                "city": 0,
                "study": 0
            }
    }
    lstFriends = getFriends(usr_id)

    suspectData['work'] = getUserWorkPlaceName(usr_id)
    suspectData['city'] = getUserHometown(usr_id)
    suspectData['study'] = getUserStudyPlace(usr_id)

    d = login(usr_name, usr_pass)
    d.get("https://m.facebook.com/" + usr_id)

    for currId in lstFriends:
        d.get("https://m.facebook.com/" + str(currId))
        if suspectData['work'] != '' and \
                        getUserWorkPlaceName(currId) == suspectData.work:
            data['common']['work'] = data['common']['work'] + 1
        if suspectData['city'] != '' and \
                        getUserHometown(currId) == suspectData.city:
            data['common']['city'] = data['common']['city'] + 1
        if suspectData['study'] != '' and \
                        getUserStudyPlace(currId) == suspectData.study:
            data['common']['study'] = data['common']['study'] + 1
        if getUserGender(usr_id) == 'Male':
            data['gender']['males'] = data['gender']['males'] + 1
        if getUserGender(usr_id) == 'Female':
            data['gender']['females'] = data['gender']['females'] + 1
        if getUserGender(usr_id) != 'Female' and \
                        getUserGender(usr_id) != 'Male':
            data['gender']['unknown'] = data['gender']['unknown'] + 1

    data['amount'] = len(lstFriends)
    d.close()
    return data

def waitForElementById(d,elm_id):
    while(len(d.find_elements_by_id("url_box")) == 0):
        (lambda:None)()

def getProfilePicSites(usr_id):
    #d = login(usr_name, usr_pass)
    d = webdriver.Chrome()
    pic_url = "https://graph.facebook.com/" + usr_id + "/picture?type=large&w%E2%80%8Cidth=720&height=720"
    d.get("https://www.tineye.com/")
    waitForElementById(d,"url_box")
    url_elm = d.find_element_by_id("url_box")
    url_elm.send_keys(pic_url)
    d.find_element_by_id("url_submit").click()
    waitForElementById(d,"col-md-12")
    l = d.find_element_by_class_name('col-md-12')
    txt = l.find_element_by_tag_name('h2').get_property("innerHTML")
    k = re.search("[0-9]+",txt)
    res = txt[k.start():k.end()]
    d.close()
    return res

def getUserPosts(usr_id):
    d = login(usr_name, usr_pass)
    d.get("https://m.facebook.com/" + usr_id)
    scrollDown(d)
    posts = d.find_elements_by_tag_name("article")
    posts_by_user = [post for post in posts if re.search("profile.php.*id=" + usr_id, post.get_attribute('innerHTML'))]
    d.close()
    return len(posts_by_user)


def getMutualFriendsCount(usr_id1, usr_id2):
    d = login(usr_name, usr_pass)
    d.get("https://www.facebook.com/browse/mutual_friends/?uid=" + usr_id1 + "&node=" + usr_id2)
    scrollDown(d)
    pageSrc = d.page_source
    lst_ids = [pageSrc[m.start() + 15:m.start() + 30] for m in list(re.finditer("profile.php", pageSrc))]
    d.close()
    return len(lst_ids)


def getUserGroups(usr_id):
    d = login(usr_name, usr_pass)
    d.get("https://facebook.com/" + usr_id + "/groups")
    groupContainers = d.find_elements_by_xpath("//div[contains(@class, 'fwb') and contains(@class, 'mbs')]//a")
    index = 0
    groups = []
    for container in groupContainers:
        groups.append(groupContainers[index].get_attribute("href")[
                      re.search('/groups/', groupContainers[index].get_attribute("href")).end():])
        index = index + 1
    d.close()
    return groups


def getMutualFriendsList(usr_id1, usr_id2):
    d = login(usr_name, usr_pass)
    d.get("https://www.facebook.com/browse/mutual_friends/?uid=" + usr_id1 + "&node=" + usr_id2)
    scrollDown(d)
    pageSrc = d.page_source
    lst_ids = [pageSrc[m.start() + 15:m.start() + 30] for m in list(re.finditer("profile.php", pageSrc))]
    lst_ids = [idd[0:re.search("[0-9]+", idd).end()] for idd in lst_ids]
    d.close()
    return lst_ids


# ~~~~~ User Details Methods
def getPersonalData(usr_id):
    data = {
        "work": getUserWorkPlaceName(usr_id),
        "city": getUserHometown(usr_id),
        "study": getUserStudyPlace(usr_id)
    }

    return data

def getUserWorkPlaceName(usr_id):
    d = openAboutPage(usr_id)
    workPlaceElement = d.find_elements_by_xpath(
        "//div[contains(@class, '_6a')]//span[contains(@class, '_50f8')  and contains(@class, '_50f4')]")
    workplace = d.execute_script("return arguments[0].innerText", workPlaceElement[0])
    d.close()
    return workplace if (workplace != "No workplaces to show") else ""

def getUserGender(usr_id):
    d = openAboutPage(usr_id)
    detailsTab = d.find_elements(By.PARTIAL_LINK_TEXT, "Contact and Basic Info")
    time.sleep(1)
    detailsTab[0].click()
    time.sleep(1)
    genderElem = d.find_elements_by_xpath("//div[contains(@class, '_pt5')]//span[@class='_50f4']")[0]
    gender = d.execute_script("return arguments[0].innerText", genderElem)
    res = gender if (gender == "Male" or gender == "Female") else ""
    d.close()
    return res

def getUserStudyPlace(usr_id):
    d = openAboutPage(usr_id)
    studyPlaceElement = d.find_elements_by_xpath(
        "//div[contains(@class, '_6a')]//span[contains(@class, '_50f8')  and contains(@class, '_50f4')]")
    studyplace = d.execute_script("return arguments[0].innerText", studyPlaceElement[1])
    d.close()

    return studyplace if (studyplace != "No schools to show") else ""


def getUserHometown(usr_id):
    d = openAboutPage(usr_id)
    d.execute_script("window.scrollTo(0,100)")
    time.sleep(2)
    homeTab = d.find_elements(By.PARTIAL_LINK_TEXT, "Lived")
    time.sleep(1)
    homeTab[0].click()
    time.sleep(1)
    currCity = d.find_elements_by_id('current_city')
    res = "" if (len(currCity) == 0) else d.execute_script("return arguments[0].innerText", currCity[0]).split('\n')[1]
    d.close()
    return res

def getUserGender(usr_id):
    d = openAboutPage(usr_id)
    detailsTab = d.find_elements(By.PARTIAL_LINK_TEXT, "Contact and Basic Info")
    time.sleep(1)
    detailsTab[0].click()
    time.sleep(1)
    genderElem = d.find_elements_by_xpath("//div[contains(@class, '_pt5')]//span[@class='_50f4']")[0]
    gender = d.execute_script("return arguments[0].innerText", genderElem)
    res = gender if (gender == "Male" or gender == "Female") else ""
    d.close()
    return res

# ~~~~~ Groups Methods
def getGroupMembers(groupName):
    d = login(usr_name, usr_pass)
    d.get("https://www.facebook.com/groups/" + groupName + '/members')
    while (d.page_source.find("See More") > 0):
        elm_see_more = d.find_elements(By.PARTIAL_LINK_TEXT, "More")[0]
        elm_see_more.click()
        time.sleep(4) 
    lst_ids = extractIdsFromHtml(d.page_source, d)
    d.close()
    return lst_ids


# ~~~~~ Common Methods
def scrollDown(d):
    var_cont = True
    last_height = 0
    while var_cont:
        d.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(4)
        height = d.execute_script("return document.body.scrollHeight")
        var_cont = (height != last_height)
        last_height = height


def openAboutPage(usr_id):
    d = login(usr_name, usr_pass)
    d.get("https://www.facebook.com/" + usr_id + "/about")
    return d


def ConvertDataToFile(data):
    return 1

def extractIdsFromHtml(html, d): 
    strr = html
    if strr.find("profile.php") == 0:
        lst_ids = [strr[m.start( ) + 4:m.start( ) + 19] for m in list(re.finditer('"id":', strr))]
        lst_ids = lst_ids[:-2]
    else:
        lst_ids = [strr[m.start() + 10:m.start() + 30] for m in list(re.finditer("profile.php", strr))]
        lst_ids = [idd[re.search("=[0-9]+", idd).start()+1:re.search("=[0-9]+", idd).end()] for idd in lst_ids]
    return lst_ids

# ~~~~~~~~~~~ Ideas
def extractUserIdsFromUrl(url):
    return 1


def getFriendsListForUser(usr_id):
    return 1


def getMutualFriends(usr_id):
    return 1

def extractGroupsFromHtml(html):
    return 1

    # ~~~~~~ User JSON export handler
    # groups
    # friends
    # profile picture
    # picture related sites
    # mutual friends with fictive users
    # date of create account
    # dates of friends added
    # friends in group

# adami = getFriendsStatistics("100008258685419")
# #adami = getFriends("100008258685419")