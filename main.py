from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import pw


class instagram_bot:
    def __init__(self,username,pw):
        self.driver =webdriver.Chrome()
        self.username=username
        self.search_name="ikonya_"
        self.driver.get("https://instagram.com")
        sleep(2)
       # self.driver.find_element_by_xpath("// a[contains(text(),'Log in')]")\.click()//  to click on the log in button when the page opens as  sign up
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    def get_names(self):
        sleep(1)
        
        scroll_box=self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht,ht=0,1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht=self.driver.execute_script("""
                arguments[0].scrollTo(0,arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
            """,scroll_box)
        links=scroll_box.find_elements_by_tag_name('a')
        names=[name.text for name in links if name.text!='']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        sleep(1)
        return names
        

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/followers/')]".format(self.username)).click()
        followers=self.get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/following/')]".format(self.username)).click()
        following=self.get_names()
        not_following_back=[user for user in following if user not in followers]
        for x in range(len(not_following_back)): 
            print (not_following_back[x]+"\n") 

    def get_fans(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/followers/')]".format(self.username)).click()
        followers=self.get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/following/')]".format(self.username)).click()
        following=self.get_names()
        fans=[user for user in followers if user not in following]
        for x in range(len(fans)): 
            print (fans[x]+"\n")

    def search_for_user(self):
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(self.search_name)
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(self.search_name)).click()
        sleep(2)
    def delete_chats(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/direct/inbox/')]").click()
        sleep(4)
        self.driver.find_element_by_xpath("//img[contains(@alt,'{}'s profile picture')]".format(self.search_name)).click()
        
    def send_message(self):
        self.search_for_user()
        self.driver.find_element_by_xpath("//button[contains(text(),'Message')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//textarea[contains(@placeholder,'Message...')]").click()
        sleep(2)
        #self.driver.find_element_by_xpath("//textarea[contains(@placeholder,'Message...')]").send_keys("hello There")
        self.driver.find_element_by_xpath("//textarea[contains(@placeholder,'Message...')]").send_keys(Keys.RETURN)
        messages=self.driver.find_elements_by_class_name("ZyFrc")
        for texts in messages:
            print(texts.text)
        sleep(10)


        

   

my_bot=instagram_bot('ikonyabot',pw)
my_bot.delete_chats()
 
