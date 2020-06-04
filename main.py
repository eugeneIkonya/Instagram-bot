from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import pw


class instagram_bot:
    def __init__(self,username,pw):
        self.username=username
        self.search_name=input("Enter 'username to send message: ")
        self.options=webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.driver =webdriver.Chrome(options=self.options)
        self.message=''
        self.driver.get("https://instagram.com")
        sleep(4)
        #self.driver.find_element_by_xpath("// a[contains(text(),'Log in')]")\.click()//  to click on the log in button when the page opens as  sign up
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    
        

    def get_names(self):
        sleep(2)
        
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
        names=['@'+name.text for name in links if name.text!='']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        sleep(1)
        return names
        

    def get_unfollowers(self):
        self.search_for_user()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        followers=self.get_names()
        print(len(followers))
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/following/')]".format(self.search_name)).click()
        following=self.get_names()
        print(len(following))
        not_following_back=[user for user in following if user not in followers]
        n=20
        final = [not_following_back[i * n:(i + 1) * n] for i in range((len(not_following_back) + n - 1) // n )]
        return final
        

    def get_fans(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/followers/')]".format(self.username)).click()
        followers=self.get_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/following/')]".format(self.username)).click()
        following=self.get_names()
        fans=[user for user in followers if user not in following]
        fans_string=','.join(fans)
        return fans_string

    def search_for_user(self):
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(self.search_name)
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div").click()
        sleep(2)

    def delete_chat(self):
        self.search_for_user()
        self.driver.find_element_by_xpath("//button[contains(text(),'Message')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/button").click()
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/button").click()
        sleep(1)
        self.driver.find_element_by_xpath("//button[contains(text(),'Delete')]").click()
        sleep(2)
        
    def send_message(self):
        #self.search_for_user()
        #self.driver.find_element_by_xpath("//button[contains(text(),'Message')]").click()
        sleep(2)
        message_area=self.driver.find_element_by_tag_name('textarea')
        message_area.click()
        sleep(2)
        message_area.send_keys(self.message)
        message_area.send_keys(Keys.RETURN)
       

    def read_message(self,):
        self.delete_chat()
        self.search_for_user()
        self.driver.find_element_by_xpath("//button[contains(text(),'Message')]").click()
        messages=self.driver.find_elements_by_class_name("ZyFrc")
        for texts in messages:
            print(texts.text)
        sleep(10)
    

    
    def send_unfollowers(self):
        unfollowers=self.get_unfollowers()
        self.driver.find_element_by_xpath("//button[contains(text(),'Message')]").click()
        for groups in unfollowers:
                self.message=', '.join(groups)
                self.send_message() 
        sleep(2)
        
           



        

   
my_bot=instagram_bot('ikonyabot',pw)
#my_bot.send_unfollowers()
 
