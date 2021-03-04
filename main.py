from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.parse
import hashlib
browser = webdriver.Chrome(executable_path=r'./chromedriver')

meetingID = "MyClass"
securitySalt = "###"
apiEndpoint = "https://bbb.example.com/bigbluebutton/api/"
botName = "Participant"

def join(count):
    for x in range(count):
        call = "join"
        fullName = urllib.parse.quote(botName+" #"+str(x))
        if(x!=0):
            request = "fullName="+fullName+"&redirect=true&password=123456&&meetingID="+meetingID
        else:
            request = "fullName="+fullName+"&redirect=true&password=654321&&meetingID="+meetingID
        mix = call+request+securitySalt
        checksum = hashlib.sha1(str(mix).encode('utf-8')).hexdigest()
        url = apiEndpoint+call+"?"+request+"&checksum="+str(checksum)
        browser.get(url)
        if(x < count -1):
            browser.execute_script("window.open('');")
            browser.switch_to.window(browser.window_handles[x+1])

def create():
    call = "create"
    request = "name=TestRoom&lockSettingsDisableMic=true&attendeePW=123456&moderatorPW=654321&meetingID="+meetingID
    mix = call+request+securitySalt
    checksum = hashlib.sha1(str(mix).encode('utf-8')).hexdigest()
    url = apiEndpoint+call+"?"+request+"&checksum="+str(checksum)
    browser.get(url)

create()
join(30)

