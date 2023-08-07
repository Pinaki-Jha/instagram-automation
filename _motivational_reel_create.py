#Importing the required libraries
from moviepy.editor import *
from playwright.sync_api import sync_playwright
import time
from time import sleep
from elevenlabs import generate,save,set_api_key
import _secret_info
from _secret_info import api_key_elevenlabs
from bs4 import BeautifulSoup
import random
import urllib.request
from pathlib import Path


#Globally setting the API key for ElevenLabs
#set_api_key(api_key_elevenlabs)



#tried using tensorart to generate images because picfinder fails at random occasions
#Ran into the problem of google not allowing an account login, which is required to log into tensorart


#BACKGROUND CREATION FUNCTION USING A.I.
#Solved the random fails by writing a time based looping condition. 
# Will abort the function if image generation takes more than 3 minutes
def background_creation():
    prompts = [
    "Sunrise over calm lake.",
    "Cloudy mountain landscape.",
    "Beach with gentle waves.",
    "Starry sky over meadow.",
    "Sunlight through forest leaves.",
    "City at sunset.",
    "Cozy fireplace nook.",
    "Garden with flowers.",
    "Winding roads view.",
    "Rainbow over a field.",
    "Waterfall in wilderness.",
    "Boat on reflective lake.",
    "Desert sunrise.",
    "Ancient ruins.",
    "Snowy mountains.",
    "Cabin by a river.",
    "Hot air balloons in sky.",
    "Castle on a hill.",
    "Cliffside path by ocean.",
    "Foggy mystical forest.",
    "Night city lights.",
    "Sunflowers in field.",
    "Hammock between palm trees.",
    "Waves against cliffs.",
    "Cobblestone alley.",
    "Pool meeting ocean.",
    "Golden hour at shore.",
    "Autumn leaves on ground.",
    "Canoe on calm river.",
    "Sun through cathedral windows.",
    "Footprints on sandy path.",
    "Bridge over brook.",
    "City skyline at night.",
    "Stepping stones in garden.",
    "Sand dunes under blue sky.",
    "Wet streets at night.",
    "Wild horses running.",
    "Cozy cafe tables.",
    "Swing on tree.",
    "Colorful houses on street.",
    "Sunset through clouds.",
    "Rowboat by water.",
    "Palm trees at sunset.",
    "Lavender field path.",
    "Icicles on cabin.",
    "Ancient wise tree.",
    "Market with fruits.",
    "Peaceful pagoda.",
    "Lighthouse by waves.",
    "Lantern-lit alley.",
    "Soaring eagle.",
    "Balcony over square.",
    "Tulip fields.",
    "Koi pond with greenery.",
    "Cherry blossom canopy.",
    "Lively carnival.",
    "Firefly-lit forest path.",
    "Mountain peak view.",
    "Thatched roof cottage.",
    "Solitary boat on lake.",
    "Rooftop garden in city.",
    "Rocky coast meeting waves.",
    "Vintage bookstore.",
    "Vineyards on hills.",
    "Hidden waterfall.",
    "Gondola through canals.",
    "Hikers on trail.",
    "Colorful bazaar.",
    "Stone archway courtyard.",
    "Snowy cabin.",
    "Windmill in wheat fields.",
    "Moonlit path in grove.",
    "Boats at calm harbor.",
    "Yoga retreat with mountains.",
    "Bustling street market.",
    "Castle overlooking sea.",
    "Tea house in garden.",
    "Charming flower cottage.",
    "Desert oasis.",
    "Gazebo by pond.",
    "Train tracks through city.",
    "Wooden bridge over brook.",
    "Farmhouse with sunflowers.",
    "Stone steps on hill.",
    "Hot air balloons in sky.",
    "Cozy cabin interior.",
    "Rocky shore with waves.",
    "Pagoda in misty valley.",
    "Bench under cherry tree.",
    "Endless road view.",
    "Busy market square.",
    "Hidden waterfall.",
    "Lakeside retreat.",
    "Quaint hillside cottage.",
    "Boat dock under starry sky.",
    "Ornate courtyard doors.",
    "Treehouse in jungle.",
    "Colorful urban mural.",
    "Hillside staircase.",
    "Picnic spot by brook."
]

    
    prompt = random.choice(prompts)
    print(prompt)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=100)
        page = browser.new_page()
        #get to page
        page.goto("https://picfinder.ai/")
        sleep(5)
        #Get to a page where login is accessible
        
        #get the prompt area
        prompt_area = '//*[@id="form-search-bar[search-box]"]'
        #fill the default prompt
        page.fill(prompt_area,"lush green mountains \n")
        sleep(1)
        #submit the prompt
        submit_button = '//*[@id="aux-buttons"]/a[1]'
        page.click(submit_button)
        sleep(5)
        #get to the login page
        account_button = '//*[@id="account-menu-button"]'
        login_button = '//*[@id="account-window"]/div/ul/li[1]/a'
        page.click(account_button)
        page.click(login_button)
        print("login page reached")
        
        #login now
        username_field =  '//*[@id="form-sign-in[user-email]"]'
        password_field = '//*[@id="form-sign-in[user-password]"]'
        page.fill(username_field,_secret_info.username)
        page.fill(password_field,_secret_info.password_picfinder)
        login_submit = '//*[@id="form-sign-in[signin-submit]"]'
        page.click(login_submit)
        print("login successful")
        #lOGIN FINISH
        sleep(5)
        
        #fill the real prompt
        #prompt="lusty green mountains"
        page.fill(prompt_area,prompt)
        sleep(1)
        #submit the prompt
        submit_button = '//*[@id="aux-buttons"]/a[1]'
        page.click(submit_button)
        sleep(5)
        
        #get to the settings, set the image size
        settings_button = '//*[@id="settings-menu-button"]'
        ratio_9_12_button = '//*[@id="settings-window"]/div/div[1]/div/div[8]'
        page.click(settings_button)
        page.click(ratio_9_12_button)
        #get the image generated through webscraping
        #download_button = page.query_selector('img')
        #download_button.click()
        print("prompt submitted")
        
        #loop to find the image
        find_image = False
        trying_time =  180
        start_time = time.time()
        while (time.time()-start_time<=trying_time) and find_image==False:
            if(page.is_visible('div[data-bnsfwc="false"]')):
                image_element = page.query_selector('div[data-bnsfwc="false"]')
                html = image_element.inner_html()
                print("image found")
                find_image=True
                
        #If image not generated in the specified time        
        if (find_image)==False:
            print("na bhai nahi mila")
            return "na bhai nahi mila"
        
        #else, if image found
        sleep(3)
        #image_element = page.query_selector
        #print(html)
        print("hi")
        soup = BeautifulSoup(html,"html.parser")
        images = soup.find_all('img')
        image = images[0]
        image = str(image).split()
        #print(image)
        source = image[-1].split('"')[1]
        print(source)
        return source    




#AUDIO GENERATION FOR THE REEL
#Didn't use pyttsx3 cause too monotonous and error prone
#Didn't use gtts because female voice is the only voice available
#Was thus forced to learn Elevenlabs api usage lmao
def audio_generation(quote,author,filename):
    

    audio = generate(
        text=quote,
        voice="Arnold",
        model='eleven_monolingual_v1'
    )

    
    
    # engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # print(len(voices))
    # engine.setProperty('voice', voices[0].id)
    # #engine.say(quote)
    # engine.setProperty('rate',140)
    # engine.setProperty('volume',0.8)
    
    
    save_file_path = str(Path('..\inspiragrow_automation\sound_reels\{}.mp3'.format(filename)))
    save(audio,save_file_path)
    # engine.save_to_file(quote,save_file_path)
    # engine.runAndWait()
    return filename+'.mp3'
    
    
    
#audio_generation("Never stop believing in yourself.","author Pinaki Bhai","lalalala")



#NEED TO ADD SOME BACKGROUND AUDIO AS WELL
#MAY WEBSCRAPE AI FOR THAT AS WELL LMAO
#OR DOWNLOAD SOME SAMPLE ONES TO USE
#ACTUAL REEL VIDEO CREATION


def motivational_reel_create(quote, unrefined_quote, author, reel_file_name):
    
    # Generate the audio file
    filename = reel_file_name + "audio"
    unrefined_quote = unrefined_quote[1:-1] + '.'
    audio_file = audio_generation(unrefined_quote, author, filename)  #generate audio
    
    # Get the audio file
    audio_clip = AudioFileClip(str(Path('..\inspiragrow_automation\sound_reels\{}'.format(audio_file))))
    
    #Reel duration
    duration = audio_clip.duration  + 3    
    
    # Creating the quote text
    text_clip = TextClip(txt=quote, size=(500, 0), color="white")
    text_clip = text_clip.set_position("center")
    tc_width, tc_height = text_clip.size
    
    # Background for the quote
    color_clip = ColorClip(size=(tc_width + 100, tc_height + 100), color=(0, 0, 0, 90))
    
    # Merging the background with the quote
    final_clip = CompositeVideoClip([color_clip, text_clip])
    final_clip = final_clip.set_position('center')
  
    # GET THE IMAGE HERE
    get_bg_image=False
    while not get_bg_image:
        try:
            source = background_creation()
            #source = 'https://im.picfinder.ai/image/ii/f8f2d3d5-b4d5-4921-85d3-9ecd839c7e50.jpg'
            image_file_name = reel_file_name + ".jpg"
            image_file_path = str(Path('..\inspiragrow_automation\images_reels\{}'.format(image_file_name)))
            #source = background_creation()
            #source = 'https://im.picfinder.ai/image/ii/f5ab7e74-17a4-45ff-9495-0526ec53806d.jpg'
    
            # Create a Request object with headers
            request = urllib.request.Request(source, headers={"User-Agent": _secret_info.user_agent})

            #Open the URL with the specified headers
            response = urllib.request.urlopen(request)

            # Retrieve the content and save it to the file
            with open(image_file_path, "wb") as f:
                f.write(response.read())
            
            get_bg_image= True
            
        except:
            print("trying again")
            sleep(5)
        #place another except block here to handle when post could not be fetched multiple times
        #mostly for testing purposes, its annoying to start this up again and again just cuz 
        #I accidentally pressed run qwq 
            

    #response = requests.get(source)
    #print(response.content)
    #image_data = BytesIO(response.content)
    #print(image_data)
    im_clip = ImageClip(image_file_path)
    
    
    # Create the final output by composing the image and the quote clip
    final_output = CompositeVideoClip([im_clip.set_duration(duration), final_clip.set_duration(duration-2).fadein(0.5).fadeout(0.5)])
    final_output = final_output.set_audio(audio_clip)  # Set the audio
    
    # Write the final composite video clip with audio
    end_result_name = reel_file_name +".mp4"
    end_result_address = str(Path('E:\Inspirarchive\Inspiragrowth\inspiragrow_automation\end_reels\{}'.format(end_result_name)))
    final_output.write_videofile(end_result_address, codec="libx264",fps=30)
    return end_result_name
    
    

    
    
    
    
#motivational_reel_create("hi hello wassup i'm good \n wbu ahaha wao \n lmao qwq kya ho raha hai yeh","hi hello wassup i'm good wbu ahaha wao lmao qwq kya ho raha hai yeh","lalala","lalala")