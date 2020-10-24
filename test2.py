 #!/usr/bin/python3.8
import time
import traceback
import logging 
from telethon import TelegramClient


api_id =16524264262 ###from telegram
api_hash = '2526416521258hjjjsv65121'#####from telegram
client = TelegramClient('anon', api_id, api_hash)


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import simon
#from mitsuku import PandoraBot


from simon.accounts.pages import LoginPage
from simon.chat.pages import ChatPage
from simon.chats.pages import PanePage
from simon.header.pages import HeaderPage



# Creating the driver (browser)
options =webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/home/mclnerney/mitsuku-and-whatsapp')

driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=options)#webdriver.Firefox()
def start():
    driver.maximize_window()


    login_page = LoginPage(driver)
    login_page.load()
    time.sleep(7)
    pane_page = PanePage(driver)

    opened_chats = pane_page.opened_chats
    
   
    
   
    wait=WebDriverWait(driver,600)
#   
    for oc in opened_chats:
        name=str(oc.name)  
         
        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()
        msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') 
        last_message=str(oc.last_message)
        async def bot():
   
            mes=await client.send_message('mitsuku_bot', last_message)
    
            time.sleep(15)
            for message in  await client.get_messages('mitsuku_bot'):
                
                msg=message.text
                  
                for i in range(1):
                   msg_box.send_keys(msg)
        # The classname of send button may vary.
                   button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button') 
                   button.click() 
                   #print('Done')
    

        with client:
            client.loop.run_until_complete(bot())
        
        
            
            
        
    
        

   
   



#start()
import traceback
def every(delay,task):
    next_time=time.time() + delay
    while True:
        time.sleep(max(0,next_time - time.time()))
        try:
            task()
        except Exception:
            traceback.print_exc()
        next_time += (time.time()-next_time)//delay * delay + delay
        

# Close the browser
#driver.quit()
every(30,start)



