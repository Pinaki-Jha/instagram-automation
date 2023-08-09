#IMPORTING MODULES
from bs4 import BeautifulSoup
import pandas as pd
import requests
import urllib.request
from PIL import Image, ImageDraw, ImageFont
import csv
import random
import datetime
from pathlib import Path

'''------------------------------------------GET QUOTES FROM GOODREADS---------------------------------------------------'''
def get_quotes_from_goodreads(base_url,page, quotes, authors):
    
    url = base_url+str(page) #final url link created
    print("fetching quotes for",page)
    webpage = requests.get(url) #Requesting the website for the data
    soup = BeautifulSoup(webpage.text,'html.parser') #Parsing the text data from the website
    print("quotes found")
    quote_text = soup.find_all('div',attrs={"class":"quoteText"}) #Get a list of all the text in the quote divs
    
    for i in quote_text:                               
        all_text = i.text.strip().split('\n') #Split text by newline
        quote = all_text[0]  #The first element is the quote
        if(len(quote)<576): #Check if the quote is too big to fit into the insta post template
            quotes.append(quote)  #append to the quotes list 
        author = i.find("span",attrs={"class":"authorOrTitle"}).text.strip().split(",")[0]   #Get the author that corresponds to the quote
        authors.append(author) #append to the authors list
    print("Data Appended")

'''--------------------------------GET MOTIVATIONAL QUOTES FROM GOODREADS--------------------------------------------------'''
def get_motivational_quotes(page_list):  #to get motivational quotes from goodreads
    start_page = page_list[0]                     #Starting page
    end_page = page_list[1]                       #Ending page
    base_url ="https://www.goodreads.com/quotes/tag/motivational?page="   #Supplying the the base url ----change this to import from a csv file with boolean values for if the url has exhausted or not ----MIGHT CREATE AN ALTERNATE FUNCTION ALTOGETHER FOR DIFFFERENT URLS, BUT THAT SEEMS FAR TOO INEFFICIENT
    quotes=[]                                                             #Quotes list for all the quotes in the pages
    authors=[]                                                            #Corresponding author list
    posted=[]                                                             #Initialize the corresponding posted list(to tell if it has been posted to instagram or not)
    for page in range(start_page,end_page+1):                             #Iterating through the pages and fetching all the quotes
        get_quotes_from_goodreads(base_url,page,quotes,authors)           
    for i in range(0,len(quotes)):                                        #Initializing all posted values as False
        posted.append(False)
    print("finished creating lists: authors, quotes, posted")
    return quotes, authors,posted

'''-----------------------------------REFINE THE QUOTES LIST-----------------------------------------------------------------'''
def refine_quotes(quotes):                           #For refining the quotes list for the instagram post/reel
    quotes_new = []
    for quote in quotes:
        quote= quote[1:-1]                           #Removing double quotes (") from the start and end
        quote_list = quote.split( )                  #Splitting for every word
        new_quote = ""
        count = 1
        for i in range(0,len(quote_list)):        #Adding newline characters after a line crosses 32 characters  
            if count>=32:                                  
                new_quote = new_quote+" " + "\n" 
                new_quote = new_quote + " " + quote_list[i]
                count=1;
            else:
                new_quote = new_quote + " " + quote_list[i]
                count = count+ len(quote_list[i])
        quotes_new.append(new_quote)
    print("all quotes refined.")
    return quotes_new 


'''-------------------------------CREATE THE MOTIVATIONAL QUOTE IMAGE---------------------------------------------------------'''
def motivation_post_create(quote,author,image_name):
    with Image.open("_quotes_template.png") as im:     #Opening the quote template   
        d = ImageDraw.Draw(im)                         #Creating the Draw object for the image imported
        fnt = ImageFont.truetype("arial.ttf", 30)      #Selecting the font
        _,_,w,h = d.textbbox((0,0),quote,font=fnt)     #For centering, getting the height and width of the textbox for the quote
        d.multiline_text(((1080-w)/2,((1080-h)/2)-50),quote, font=fnt, fill=(0,0,0))  #"Drawing" the quote onto the instagram template post
        _, _, w, h = d.textbbox((0, 0),author, font=fnt)   #For centering, getting the height and width of the author textbox
        d.text(((1080-w)/2,680), author, font=fnt, fill=(0,0,0)) #Drawing the author onto the image
        #im.show()
        image_address = Path('..\inspiragrow_automation\images\{}.png'.format(image_name))   #Image address defined
        im.save(image_address)                       #Saving the image
        print("Picture created and saved.")
        return image_name +".png"                    #Returning the image name


'''-----------------------------HANDLING CSV FILES OTHER THAN THE PAGES_LIST_DATA----------------------------------------'''
#WRITE THE DATA TO CSV FILE
def write_data(the_list,the_data):                    
    with open(the_data, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(the_list)
        print("data written.")

#Might Merge the Two functions below to One
#READ THE DATA FROM THE POSTED CSV FILE(SEPARATE FUNCTION TO HANDLE THE TRUE AND FALSE VALUES)
def read_posted_data(the_data):
    with open(the_data, mode='r', newline='') as file:
        reader = csv.reader(file)
        data_list = next(reader)
        data_list = [i=="True" for i in data_list]
        print("posted data read.")
    return data_list
#READ THE DATA FROM THE OTHER CSV FILES
def read_data(the_data):
    with open(the_data, mode='r', newline='') as file:
        reader = csv.reader(file)
        data_list = next(reader)
        print("data read.")
    return data_list


'''------------------------------------------------------CREATING A PAGELIST--------------------------------------'''

#WRITE TO PAGELIST------------------------------------------------------------------------'''
def write_pagelist_data(data_list, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_list)
        print("written to pagelist.")
#READ FROM PAGELIST-------------------------------------------------------------------'''
def read_pagelist_data(file_path):
    print("reading pagelist data.")
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        data_list = [list(map(eval, row)) for row in reader]
        print("read pagelist data.")
    return data_list
#CREATE THE PAGELIST-------------------------------------------------------------------'''
def create_pages_list(file_name):
    print("Creating pagelist...")
    pages_list = []                       #generate a list of pages
    for i in range (1,101,4):
        pages_list.append([i,i+3,False])
    write_pagelist_data(pages_list,file_name)
    print("Pagelist created.")
    return pages_list

