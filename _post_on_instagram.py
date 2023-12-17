from _create_insta_post import insta_post_create
from _create_insta_reel import insta_reel_create
from playwright.sync_api import sync_playwright
from pathlib import Path
from time import sleep
import autoit
import _secret_info

#IMPROVEMENTS TO BE MADE:
#Check the master function using insta_post_create, if it works after exhausting the first 4 pages
#Make the page group selection randomized
#Implement except conditions for when all of the page groups have been exhausted - send a message and reset all pagegroup false values to true
#Implement deleting older images (over ten days old)
#Implement loop that runs 24/7 and posts the right stuff at the time
#Finish the implementation of the reels function
#Clean up the codes, specially the try-except blocks of post_on_instagram function's code

'''-----------------------------------------TO POST A PICTURE ON INSTAGRAM----------------------------------------------------'''
def post_on_instagram(consistent_image_path, caption):
    #Open the playwright file
    with sync_playwright() as p:
        #launch -- Set headless = False to actually see what is going on
        browser = p.firefox.launch(headless=False, slow_mo=250)
        page = browser.new_page()
        #get to page
        page.goto("https://www.instagram.com/")
        sleep(5)
        print("Reached the instagram page...")
        
        #login form components defined
        login_form = '//*[@id="loginForm"]/div/div[1]/div/label/input'  
        password_form = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        login_btn = '//*[@id="loginForm"]/div/div[3]/button'
        
        #Login form data fill
        page.fill(login_form, _secret_info.username)
        sleep(2)
        page.fill(password_form, _secret_info.password)
        sleep(3)
        page.click(login_btn)
        sleep(10)
        print("Login Successful...")
        
        #Deny save login information
        not_now_btn = page.query_selector(f'div:text("Not Now")')
        if(not_now_btn):
            not_now_btn.click()
        sleep(10)
        
        #Deny turning on notifications
        not_now_btn_2 = page.query_selector(f'button:text("Not Now")')
        if(not_now_btn_2 is not None):
            not_now_btn_2.click()
            sleep(10)
        print("Notifications handled...")
        
        #Get to the create button
        create_btn = page.query_selector(f'span:text("Create")')
        create_btn.click()
        sleep(2)
        
        #Create and upload the instagram post
        
        #Create and save the first picture along with its address, add the address of the second picture
        posted, pages_list, to_post_positions, image_name = insta_post_create()
        image_address = '"' + str(Path('E:\Inspirarchive\Inspiragrowth\inspiragrow_automation\images\{}'.format(image_name))) + '"'
        print(image_address)
        print("Image created...")
        #get to the upload button
        upload_img_btn = page.query_selector(f'button:text("Select from computer")')
        upload_img_btn.click()
        sleep(10)
        
        #Native file window opens. Handling it with PyAutoIt to select the image to upload
        try:
            autoit.control_send("File Upload","Edit1",image_address)
            sleep(5)
            autoit.control_click("File Upload","Button1")
            sleep(10)
        except:
            file_input = page.query_selector('input[type="file"]')
            image_address = str(Path('E:\Inspirarchive\Inspiragrowth\inspiragrow_automation\{}'.format(image_name)))
            file_input.set_input_files(image_address)
            upload_button = page.query_selector('button[type="submit"]')
            if upload_button:
                upload_button.click()
        
        print("image uploaded...")    

        #Posting the picture now
        next_btn_1 = page.query_selector(f'div:text("Next")')
        if(next_btn_1 is not None):
            next_btn_1.click()
            sleep(2)
        next_btn_2 = page.query_selector(f'div:text("Next")')
        if(next_btn_2 is not None):
            next_btn_2.click()
            sleep(2)
        #Writing the caption for the picture
        caption_path = page.query_selector('[role="textbox"]')
        
        caption_path.fill(caption)
        print("image posted...")
        sleep(5)
        share_button = page.query_selector(f'div:text("Share")')
        share_button.click()
        sleep(10)
        browser.close()
        
            

#consistent_image_path = str(Path("E:\Inspirarchive\Inspiragrowth\inspiragrow_automation\_quotes_template.png"))
#caption="goo goo ga ga"
#post_on_instagram(consistent_image_path,caption)


'''------------------------------------------TO POST A REEL ON INSTAGRAM--------------------------------------------------'''

def reel_post(caption,reel_name):
    
    with sync_playwright() as p:
        
        browser = p.firefox.launch(headless=False, slow_mo=250) #have to set headless to false for the native dialog to open
        page = browser.new_page()
        
        #get to the instagram page
        page.goto("https://www.instagram.com/")
        sleep(5)
        print("Reached the instagram page...")
        
        #login form components defined
        login_form = '//*[@id="loginForm"]/div/div[1]/div/label/input'  
        password_form = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        login_btn = '//*[@id="loginForm"]/div/div[3]/button'
        
        #Login form data fill
        page.fill(login_form, _secret_info.username)
        sleep(2)
        page.fill(password_form, _secret_info.password)
        sleep(3)
        page.click(login_btn)
        sleep(10)
        print("login successful...")
        
        #Deny save login information
        not_now_btn = page.query_selector(f'div:text("Not Now")')
        if(not_now_btn):
            not_now_btn.click()
        sleep(10)
        #Deny turning on notifications
        not_now_btn_2 = page.query_selector(f'button:text("Not Now")')
        if(not_now_btn_2 is not None):
            not_now_btn_2.click()
            sleep(10)
        print("Notifications handled...")
        
        #Get to the create button
        create_btn = page.query_selector(f'span:text("Create")')
        create_btn.click()
        sleep(2)
        
        #Get the full address of the reel
        reel_address = '"' + str(Path('E:\Inspirarchive\Inspiragrowth\inspiragrow_automation\end_reels\{}'.format(reel_name)))
        print(reel_address)
        
        #get to the upload button
        upload_img_btn = page.query_selector(f'button:text("Select from computer")')
        upload_img_btn.click()
        sleep(10)
        
        print("Uploading reel...")
        
        autoit.control_send("File Upload","Edit1",reel_address)
        sleep(5)           
        autoit.control_click("File Upload","Button1")
        sleep(12)
        
        ok_btn = page.query_selector(f'button:text("OK")')
        if(ok_btn is not None):
            ok_btn.click()
        
        print("Reel uploaded...")
        
        set_size_btn = page.query_selector('svg[aria-label="Select crop"]')   
        set_size_btn.click()
        
        sleep(5)
        
        select_9_12_btn = page.query_selector(f'span:text("9:16")')
        select_9_12_btn.click()
            
        next_btn_1 = page.query_selector(f'div:text("Next")')
        if(next_btn_1 is not None):
            next_btn_1.click()
            sleep(2)
        next_btn_2 = page.query_selector(f'div:text("Next")')
        if(next_btn_2 is not None):
            next_btn_2.click()
            sleep(2)
        caption_path = page.query_selector('[role="textbox"]')
        caption_path.fill(caption)
        sleep(5)
        share_button = page.query_selector(f'div:text("Share")')
        share_button.click()
        print("Reel Shared")
        sleep(10)
        browser.close()
        
        
        
        
        
        
        
        


def reel_on_instagram(caption):
    posted, pages_list, to_post_positions, reel_name = insta_reel_create()  
    reel_post(caption,reel_name)
    
        
#reel_on_instagram("googa")

