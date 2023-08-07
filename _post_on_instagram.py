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
        
        #Get to the create button
        create_btn = page.query_selector(f'span:text("Create")')
        create_btn.click()
        sleep(2)
        
        #Create and upload the instagram post
        
        #Create and save the first picture along with its address, add the address of the second picture
        posted, pages_list, to_post_positions, image_name = insta_post_create()
        image_address = '"' + str(Path('E:\Inspirarchive\Inspiragrowth\inspiragrow_automation\images\{}'.format(image_name))) + '" "' + consistent_image_path +'"'
        print(image_address)
        
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
            
        #page.screenshot(path="screenshot1.png")
        #Posting the picture now
        next_btn_1 = page.query_selector(f'div:text("Next")')
        if(next_btn_1 is not None):
            next_btn_1.click()
            sleep(2)
        next_btn_2 = page.query_selector(f'div:text("Next")')
        if(next_btn_2 is not None):
            next_btn_2.click()
            sleep(2)
        #page.screenshot(path="screenshot2.png")
        #Writing the caption for the picture
        caption_path = page.query_selector('[role="textbox"]')
        caption_path.fill(caption)
        print("heehee")
        sleep(5)
        share_button = page.query_selector(f'div:text("Share")')
        share_button.click()
        sleep(10)
        browser.close()
        
        #sleep(100)
            
print("hi")
consistent_image_path = str(Path("E:\Inspirarchive\Inspiragrowth\inspiragrow_automation\_quotes_template.png"))
caption="goo goo ga ga"
post_on_instagram(consistent_image_path,caption)


'''------------------------------------------TO POST A REEL ON INSTAGRAM--------------------------------------------------'''

def reel_post(caption,reel_name):
    #Open the playwright file
    with sync_playwright() as p:
        #launch -- Set headless = False to actually see what is going on
        browser = p.firefox.launch(headless=False, slow_mo=250)
        page = browser.new_page()
        #get to page
        page.goto("https://www.instagram.com/")
        sleep(5)
        
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
        
        #Get to the create button
        create_btn = page.query_selector(f'span:text("Create")')
        create_btn.click()
        sleep(2)
        
        #Create and upload the instagram post
        
        #Create and save the first picture along with its address, add the address of the second picture
        #posted, pages_list, to_post_positions, reel_name = insta_reel_create()
        reel_address = '"' + str(Path('E:\Inspirarchive\Inspiragrowth\inspiragrow_automation\end_reels\{}'.format(reel_name)))
        print(reel_address)
        
        #get to the upload button
        upload_img_btn = page.query_selector(f'button:text("Select from computer")')
        upload_img_btn.click()
        sleep(10)
        
        autoit.control_send("File Upload","Edit1",reel_address)
        #autoit.control_send("Open","Edit1",reel_address)
        sleep(5)                          #File Upload #32770 Edit1
        autoit.control_click("File Upload","Button1")
        sleep(12)
        
        ok_btn = page.query_selector(f'button:text("OK")')
        #<button class="_acan _acap _acaq _acas _acav _aj1-" type="button">OK</button>
        if(ok_btn is not None):
            ok_btn.click()
        
        set_size_btn = page.query_selector('svg[aria-label="Select crop"]')   #<button class="_acan _acao _acas _aj1-" type="button"><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1y1aw1k x1sxyh0 xwib8y2 xurb0ha x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh xl56j7k"><svg aria-label="Select crop" class="_ab6-" color="rgb(255, 255, 255)" fill="rgb(255, 255, 255)" height="16" role="img" viewBox="0 0 24 24" width="16"><path d="M10 20H4v-6a1 1 0 0 0-2 0v7a1 1 0 0 0 1 1h7a1 1 0 0 0 0-2ZM20.999 2H14a1 1 0 0 0 0 2h5.999v6a1 1 0 0 0 2 0V3a1 1 0 0 0-1-1Z"></path></svg></div></button>
        set_size_btn.click()
        
        sleep(5)
        
        select_9_12_btn = page.query_selector(f'span:text("9:16")')
        '''<span class="x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp x1s688f x9bdzbf x1tu3fi x3x7a5m x10wh9bi x1wdrske x8viiok x18hxmgj" 
        dir="auto" style="line-height: var(--base-line-clamp-line-height); --base-line-clamp-line-height: 18px;">
        9:16</span>'''
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
        print("heehee")
        sleep(5)
        share_button = page.query_selector(f'div:text("Share")')
        share_button.click()
        sleep(10)
        browser.close()
        
        
        
        
        
        sleep(100)
        
        
        


def reel_on_instagram(caption):
    posted, pages_list, to_post_positions, reel_name = insta_reel_create()
    #reel_name = "lalala.mp4"
    reel_post(caption,reel_name)
    
        
#reel_on_instagram("googa")

