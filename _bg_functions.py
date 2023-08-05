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

#GET QUOTES FROM GOODREADS
def get_quotes_from_goodreads(base_url,page, quotes, authors):
    url = base_url+str(page)      #final url link created
    webpage = requests.get(url)   #Requesting the website for the data
    soup = BeautifulSoup(webpage.text,'html.parser') #Parsing the text data from the website
    quote_text = soup.find_all('div',attrs={"class":"quoteText"}) #Get a list of all the text in the quote divs
    
    for i in quote_text:                               
        all_text = i.text.strip().split('\n')       #Split text by newline
        quote = all_text[0]                         #The first element is the quote
        if(len(quote)<576):                         #Reject if the quote is too big to fit into the insta post(>576 characters)
            quotes.append(quote)
        author = i.find("span",attrs={"class":"authorOrTitle"}).text.strip().split(",")[0]   #Get the author of the quote
        authors.append(author)

#GET MOTIVATIONAL QUOTES FROM GOODREADS
def get_motivational_quotes(page_list):  #to get motivational quotes from goodreads
    start_page = page_list[0]                     #Starting page
    end_page = page_list[1]                       #Ending page
    base_url ="https://www.goodreads.com/quotes/tag/motivational?page="   #the base url
    quotes=[]                                                             #Quotes list for all the quotes in the pages
    authors=[]                                                            #Corresponding author list
    posted=[]                                                             #Corresponding posted list(to tell if it has been posted to instagram or not)
    for page in range(start_page,end_page+1):
        get_quotes_from_goodreads(base_url,page,quotes,authors)
    #quotes_data= pd.DataFrame({"quote":quotes,"author":authors})
    #quotes_data.to_csv(filename + ".csv",index=False)
    for i in range(0,len(quotes)):
        posted.append(False)
    return quotes, authors,posted

#REFINE THE QUOTES LIST
def refine_quotes(quotes):                           #For refining the quotes list
    quotes_new = []
    for quote in quotes:
        print(quote)
        quote= quote[1:-1]                           #Removing ' " ' and ' " '
        #print(quote)
        quote_list = quote.split( )                #Splitting for every word
        #print(quote_list)
        new_quote = ""
        #print(quote_list)
        count = 1
        for i in range(0,len(quote_list)):        #Adding newline characters   
            if count>=32:
                new_quote = new_quote+" " + "\n" 
                new_quote = new_quote + " " + quote_list[i]
                count=1;
            else:
                new_quote = new_quote + " " + quote_list[i]
                count = count+ len(quote_list[i])
        quotes_new.append(new_quote)
    return quotes_new 




#CREATE THE MOTIVATIONAL QUOTE IMAGE
def motivation_post_create(quote,author,image_name):
    with Image.open("_quotes_template.png") as im:        
        d = ImageDraw.Draw(im)
        fnt = ImageFont.truetype("arial.ttf", 30)
        _,_,w,h = d.textbbox((0,0),quote,font=fnt)
        d.multiline_text(((1080-w)/2,((1080-h)/2)-50),quote, font=fnt, fill=(0,0,0))
        _, _, w, h = d.textbbox((0, 0),author, font=fnt)
        d.text(((1080-w)/2,680), author, font=fnt, fill=(0,0,0))
        #im.show()
        image_address = Path('..\inspiragrow_automation\images\{}.png'.format(image_name))
        im.save(image_address)
        return image_name +".png"

#motivation_post_create("lalala","lalala","lalala")
    

#HANDLING CSV FILES OTHER THAN THE PAGES_LIST_DATA
#WRITE THE DATA TO CSV FILE
def write_data(the_list,the_data):
    with open(the_data, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(the_list)

#READ THE DATA FROM THE POSTED CSV FILE(SEPARATE FUNCTION TO HANDLE THE TRUE AND FALSE VALUES)
def read_posted_data(the_data):
    with open(the_data, mode='r', newline='') as file:
        reader = csv.reader(file)
        data_list = next(reader)
        data_list = [i=="True" for i in data_list]
    return data_list

#READ THE DATA FROM THE OTHER CSV FILES
def read_data(the_data):
    with open(the_data, mode='r', newline='') as file:
        reader = csv.reader(file)
        data_list = next(reader)
    return data_list



##CREATING A PAGELIST
#WRITE TO PAGELIST
def write_pagelist_data(data_list, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_list)
#READ FROM PAGELIST
def read_pagelist_data(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        data_list = [list(map(eval, row)) for row in reader]
    return data_list
#CREATE THE PAGELIST
def create_pages_list(file_name):
    pages_list = []                       #generate a list of pages
    for i in range (1,101,4):
        pages_list.append([i,i+3,False])
    write_pagelist_data(pages_list,file_name)
    return pages_list


#motivation_post_create("lalala","lalala","lalala")