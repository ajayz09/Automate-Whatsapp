import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.chrome.options import Options

option=Options()
option.add_argument('user-data-dir=selenium')
print("===========================")
print("-----  WHATSAPP BOT  ------")
print("===========================")
print("\nPress any key to continue and launch whatsapp")
input("")
firstTime = True
driver=webdriver.Chrome(options=option)
driver.get("https://web.whatsapp.com/")
input("After Scanning press any key to continue")

def getUserName():
    user_name=input("Whom do you want to send the message")
    chat=driver.find_element_by_xpath('//span[text()="%s"]'%(user_name))
    chat.click()

def sendTexts():
    lane=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    message=input("Enter the message to send")
    lane.send_keys(message)
    lane.send_keys(Keys.RETURN)

def profile_click():
    dp_click=driver.find_element_by_xpath('//*[@id="main"]/header/div[1]')
    dp_click()

def view_profileImage():
    try:
        dp_click=driver.find_element_by_xpath('//img[@class="_2goTk _1Jdop _3Whw5"]')
        dp_click.click()
        time.sleep(2)
        image_element=driver.find_element_by_xpath('//img[@class="_3Whw5"]')
        hov = ActionChains(driver).move_to_element(image_element)
        hov.perform()
        change_photo=driver.find_element_by_xpath('//div[@class="_2H1bg"]')
        change_photo.click()
        view_photo=driver.find_element_by_xpath('//div[@title="View photo"]')
        view_photo.click()
        main()
    except:
        print("Error viewing profile picture...")
        main()


def forwardMessageToMuliple():
    namelist=[]
    choice=0
    iol=0
    while choice!="1":
        receipentName=input("Enter the name of person: ")
        namelist.append(receipentName)
        iol+=1
        choice=input("Press 1 to exit, press any other key to continue adding list ")
    print("Contacts name are : ")

    def list_print():
            for x in range(iol):
                print("    %d - %s"%(x+1,namelist[x]))

    def ex_forwarder():
        print("""
                     1. Add more contact
                     2. Delete some contacts
                     3. Continue """)
        choice = input("Choose any from above...")
        if choice=="1":
            receipentName=input("Enter the name of person: ")
            namelist.append(receipentName)
        elif choice=="2":
            print("Current List is: ")
            list_print()
            receipentNameToRemove=input("Enter the Name of the person to remove!! please be accurate")
            kr=0
            for y in range(iol):
                if namelist[y]==receipentNameToRemove:
                    namelist.remove(receipentNameToRemove)
                    kr=1
            if kr==0:
                print("NO such contact found recalling")
                ex_forwarder()
            else:
                execute_forwarder()
        elif choice=="3":
            execute_forwarder()
        else:
            print("Wrong choice...")
            ex_forwarder()

    def execute_forwarder():
        izr_text=input("Enter the message")
        for xoz in range(iol):
            use_this=namelist[xoz]
            opener=driver.find_element_by_xpath('//span[text()="%s"]'%(use_this))
            opener.click()
            lane_rn=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

            try:
                lane_rn.send_keys(izr_text)
                lane_rn.send_keys(Keys.RETURN)
            except:
                print("Error in forwarding to multiple people")
                main()
        main()
    list_print()
    ex_forwarder()

def sendMessage():
    try:
        choice=0
        while choice!=1:
            getUserName()
            sendTexts()
            choice=input("Press 1 to exit...")
            if choice=="1":
                main()
    except:
        print("Error sending message")
        print("Trying Again")
        sendMessage()

def main(firstTime=False):
        menu_item=True
        while menu_item:
            print ("""
            1. Send messages to a person
            2. Forward a message to multiple persons at once
            3. See how good is your display picture
            4. Exit from the BOT
            """)
            ans= input("What would you like to do? ")

            if not firstTime:
                driver.get("https://web.whatsapp.com/")
                time.sleep(3)

            if ans=="1":
                sendMessage()
            elif ans=="2":
                forwardMessageToMuliple()
            elif ans=="3":
                view_profileImage()
            elif ans=="4":
                print("==== Thanks for using whatsapp bot ====")
                print("Goodbye")
            elif ans !="":
                print("\n Not Valid Choice Try again")
                main()
            firstTime = False

if __name__ == "__main__":
    main(firstTime=True)