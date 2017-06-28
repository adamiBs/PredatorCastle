import selenium
import re
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

usr_name = 'aviron@tutanota.com'
usr_pass = 'Aviron669!@#'


def extractIdsFromHtml(d):
    strr = d.page_source
    lst_ids = [strr[m.start() + 15:m.start() + 30] for m in list(re.finditer("profile.php", strr))]
    lst_ids = [idd[0:re.search("id=[0-9]+", idd).end()] for idd in lst_ids]
    d.close()
    return lst_ids


def login(username, usr_password):
    d = webdriver.Chrome()
    d.get("https://www.facebook.com")
    elm_email = d.find_element_by_id("email")
    elm_pass = d.find_element_by_id("pass")
    elm_login = d.find_element_by_id("loginbutton")

    elm_email.send_keys(username)
    elm_pass.send_keys(usr_password)
    elm_login.click()
    return d


# ~~~~~~~~~~~~~ User Methods
def getFriends(usr_id):
    d = login(usr_name, usr_pass)
    d.get("https://m.facebook.com/search/" + usr_id + "/friends")
    d.close()
    return extractIdsFromHtml(d)


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
                "unknown": 0},
        "amount": 0,
        "common":
            {
                "work": 0,
                "city": 0,
                "study": 0
            }
    }
    lstFriends = getFriends(usr_id)
    d = login(usr_name, usr_pass)

    d.get("https://m.facebook.com/" + usr_id)
    suspectData.work = getUserWorkPlaceName(usr_id)
    suspectData.city = getUserHometown(usr_id)
    suspectData.study = getUserStudyPlace(usr_id)

    for currId in lstFriends:
        d.get("https://m.facebook.com/" + currId)
        if suspectData.work != '' and \
                        getUserWorkPlaceName(currId) == suspectData.work:
            data.common.work = data.common.work + 1
        if suspectData.city != '' and \
                        getUserHometown(currId) == suspectData.city:
            data.common.city = data.common.city + 1
        if suspectData.study != '' and \
                        getUserStudyPlace(currId) == suspectData.study:
            data.common.study = data.common.study + 1

    data.amount = len(lstFriends)
    d.close()
    return data


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


# ~~~~~~~~~~~~~ Groups Methods
def getGroupMembers(groupName):
    d = login(usr_name, usr_pass)
    d.get("https://www.facebook.com/groups/" + groupName + '/members')
    while (d.page_source.find("See More") > 0):
        elm_see_more = d.find_elements(By.PARTIAL_LINK_TEXT, "More")[0]
        elm_see_more.click()
        time.sleep(4)
    lst_ids = extractIdsFromHtml(d)
    d.close()
    return lst_ids


# ~~~~~~~~~~~~~ Common Methods
def scrollDown(d):
    var_cont = True
    last_height = 0
    while var_cont:
        d.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(4)
        height = d.execute_script("return document.body.scrollHeight")
        var_cont = (height != last_height)
        last_height = height


def ConvertDataToFile(data):
    return 1


# ~~~~~ User Details Methods
def getUserWorkPlaceName(usr_id):
    d = openAboutPage(usr_id)
    workPlaceElement = d.find_elements_by_xpath(
        "//div[contains(@class, '_6a')]//span[contains(@class, '_50f8')  and contains(@class, '_50f4')]")
    workplace = d.execute_script("return arguments[0].innerText", workPlaceElement[0])
    return workplace if (workplace != "No workplaces to show") else ""


def getUserStudyPlace(usr_id):
    d = openAboutPage(usr_id)
    workPlaceElement = d.find_elements_by_xpath(
        "//div[contains(@class, '_6a')]//span[contains(@class, '_50f8')  and contains(@class, '_50f4')]")
    studyplace = d.execute_script("return arguments[0].innerText", workPlaceElement[1])
    return studyplace if (studyplace != "No schools to show") else ""


def getUserHometown(usr_id):
    d = openAboutPage(usr_id)
    homeTab = d.find_elements(By.PARTIAL_LINK_TEXT, "Places He's Lived")
    if len(homeTab) == 0:
        homeTab = d.find_elements(By.PARTIAL_LINK_TEXT, "Places She's Lived")
    homeTab[0].click()
    time.wait(1)
    currCity = d.find_elements_by_id('current_city')
    return "" if (len(currCity) == 0) else d.execute_script("return arguments[0].innerText", currCity[0])


def openAboutPage(usr_id):
    d = login(usr_name, usr_pass)
    d.get("https://www.facebook.com/" + usr_id + "/about")
    return d


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Ideas
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

# ~~~~~~~~~~~~~~~~ User JSON export handler
# groups
# friends
# profile picture
# picture related sites
# mutual friends with fictive users
# date of create account
# dates of friends added
# friends in group
