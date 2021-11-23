import pyrebase

from selenium import webdriver
import time
import schedule
import os
from selenium.webdriver.chrome.options import Options



chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)



firebaseConfig={"apiKey": "AIzaSyAUWXiej6-Ee0C0HBbX6nrM1lDi3cJ5K_Y",
    "authDomain": "backbenchershub-aeb1b.firebaseapp.com",
    "databaseURL": "https://backbenchershub-aeb1b-default-rtdb.firebaseio.com",
    "projectId": "backbenchershub-aeb1b",
    "storageBucket": "backbenchershub-aeb1b.appspot.com",
    "messagingSenderId": "370610983109",
    "appId": "1:370610983109:web:eb2e6c9bff4ae0fa4be0ac",
    "measurementId": "G-DTZMG1YK31"
    }

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

#driver=webdriver.Chrome()





chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)








CommonLink="https://ilizone.iul.ac.in/2021/mod/attendance/view.php?id=";




print("Program Started")





def LogIn(enroll,passw):
        driver.find_element_by_id('username').send_keys(enroll)
        driver.find_element_by_id('password').send_keys(passw)
        time.sleep(1)
        driver.find_element_by_id('loginbtn').click()
        
        
def MarkAttendence(Subject_Name,enroll):
        try:
                driver.find_element_by_link_text("Submit attendance").click()
                driver.find_element_by_xpath("//span[text()='Present']").click()
                driver.find_element_by_xpath("//input[@value='Save changes']").click()
                print(Subject_Name+":" +enroll+" Attendance Submitted")

        except:
                print(Subject_Name+": "+enroll+" Attendance Not Submitted..........")
        

def LogOut():
        try:
                driver.find_element_by_id('action-menu-toggle-1').click()
                driver.find_element_by_id('actionmenuaction-6').click()
               
        except:
                print("Reason : Login Failed !")



def Subject(Subject_Name,Subject_Id,Branch,Year):
    user=db.child("Integral University").child("Bachelor of Technology")
    for user in user.child(Branch).child(Year).get().each():
        enroll=user.val()["enroll"]
        passw=user.val()["pass"]
        
        driver.get(CommonLink+Subject_Id)
        
        LogIn(enroll,passw)
        MarkAttendence(Subject_Name,str(enroll))
        #time.sleep(2)
        LogOut()





def SubjectBPth(Subject_Name,Subject_Id,Branch,Year):
    user=db.child("Integral University").child("Bachelor of Physiotherapy")
    for user in user.child(Branch).child(Year).get().each():
        enroll=user.val()["enroll"]
        passw=user.val()["pass"]
        
        driver.get(CommonLink+Subject_Id)
        
        LogIn(enroll,passw)
        MarkAttendence(Subject_Name,str(enroll))
        time.sleep(2)
        LogOut()






def CSE1_2y(Subject_Name,Subject_Id):
    Subject(Subject_Name,Subject_Id,"CSE-1","Second Year")


def CSE2_2y(Subject_Name,Subject_Id):
    Subject(Subject_Name,Subject_Id,"CSE-2","Second Year")


def CSE3_2y(Subject_Name,Subject_Id):
    Subject(Subject_Name,Subject_Id,"CSE-3","Second Year")









def CSE3_3y(Subject_Name,Subject_Id):
    Subject(Subject_Name,Subject_Id,"CSE-1","Third Year")
    




#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------4 CSE-1 start-----------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

def CSE1_4y(Subject_Name,Subject_Id):
    Subject(Subject_Name,Subject_Id,"CSE-1","Fourth Year")

CSE1_4y("Data Compression","26863")
CSE1_4y("Mobile Computing","26660")
CSE1_4y("Cryptography","26793")

schedule.every().monday.at("09:05").do(lambda:CSE1_4y("Data Compression","26863"))


schedule.every().tuesday.at("09:02").do(lambda:CSE1_4y("Data Compression","26863"))
schedule.every().tuesday.at("09:52").do(lambda:CSE1_4y("Mobile Computing","26660"))
schedule.every().tuesday.at("10:42").do(lambda:CSE1_4y("Mobile Computing","26660"))
schedule.every().tuesday.at("11:52").do(lambda:CSE1_4y("Cryptography","26793"))


schedule.every().wednesday.at("10:42").do(lambda:CSE1_4y("Cryptography","26793"))



schedule.every().thursday.at("09:05").do(lambda:CSE1_4y("Data Compression","26863"))

schedule.every().thursday.at("13:32").do(lambda:CSE1_4y("Mobile Computing","26660"))
schedule.every().thursday.at("14:22").do(lambda:CSE1_4y("Mobile Computing","26660"))



schedule.every().friday.at("09:05").do(lambda:CSE1_4y("Data Compression","26863"))
schedule.every().friday.at("10:42").do(lambda:CSE1_4y("Cryptography","26793"))
schedule.every().friday.at("11:32").do(lambda:CSE1_4y("Cryptography","26793"))




#---------------------------------------------------------------3 CSE-1 end-------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------





#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------3 CSE-2 start-----------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------


def CSE2_3y(Subject_Name,Subject_Id):
    Subject(Subject_Name,Subject_Id,"CSE-2","Third Year")
    




#---------------------------------------------------------------3 CSE-2 end-------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------3 CSE-3 start-------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------


def CSE3_3y(Subject_Name,Subject_Id):
        Subject(Subject_Name,Subject_Id,"CSE-3","Third Year")





#---------------------------------------------------------------3 CSE-3 end-------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------3 Ag start-------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------

def Ag_3y(Subject_Name,Subject_Id):
        Subject(Subject_Name,Subject_Id,"Agriculture Engg","Third Year")




#---------------------------------------------------------------3 Ag end-------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------3 BPth start-------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------


def BPth_3y(Subject_Name,Subject_Id):
        SubjectBPth(Subject_Name,Subject_Id,"Bachelor of Physiotherapy","Third Year")
        

        


#---------------------------------------------------------------3 BPth end-------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------2 CSE-2 start-------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------

def CSE2_2y(Subject_Name,Subject_Id):
        Subject(Subject_Name,Subject_Id,"CSE-2","Second Year")








#---------------------------------------------------------------2 CSE-2 end-------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------




while True:
        schedule.run_pending()
        time.sleep(1)
