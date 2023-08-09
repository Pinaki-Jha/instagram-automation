from _bg_functions import *
from _motivational_reel_create import *




'''
------------------------------------------------------------------FOR CREATING POSTS-------------------------------------------------------------------------
'''
def master_function_goodreads():
    run=True
    pages_list = read_pagelist_data("pages_list_data.csv") 
    while(run):
        try:
            posted = read_posted_data("posted_data.csv")
        except:
            write_data([True],"posted_data.csv")
            posted = read_posted_data("posted_data.csv")
                                                          # gives a list of whether a quote has been posted on instagram or not
        
        left_to_post = False                              # Checks if all the current posts have been posted
        for i in range(0,len(posted)):
            print(type(posted[i]))
            if (posted[i]==False):
                left_to_post = True
                break                                              
                                                       #If all current quotes have been made and posted
        if(left_to_post==False):
            print("Na bhai kuchh na bacha post karne ko")
            print("ruk banata main kuchh")
            
            page_count=0
            
            while(page_count<len(pages_list) and pages_list[page_count][2]==True):
                page_count+=1
                
            pages = [pages_list[page_count][0],pages_list[page_count][1]]
            print("getting pages",pages[0],"to",pages[1])
        
            #filename = str(pages[0]) + "to" + str(pages[1])
        
            unrefined_quotes, authors, posted = get_motivational_quotes(pages)
            quotes = refine_quotes(unrefined_quotes)
            write_data(posted,"posted_data.csv")
            write_data(quotes,"quotes_data.csv")
            write_data(authors,"authors_data.csv")
            
            pages_list[page_count][2]=True
            
            
            
        else:
            to_post_positions=[]
            quotes = read_data("quotes_data.csv")
            authors = read_data("authors_data.csv")
            for i in range(0,len(posted)):
                if posted[i]==False:
                    to_post_positions.append(i)
            #print(to_post_positions)  
            #try:
            post_number = random.choice(to_post_positions)
            posted[post_number]=True
            to_post_positions.remove(post_number)
            #print(datetime.now())
            image_name = str(datetime.date.today()) + "-" + str(post_number) 
            #print(image_name)
            img = motivation_post_create(quotes[post_number],authors[post_number],image_name)
                
            #except:
                #print("not enough quotes!")
                #left_to_post=False
            #print(posted)
            #print(to_post_positions)
            write_data(posted,"posted_data.csv")
            run=False
    write_pagelist_data(pages_list,"pages_list_data.csv")
    return posted, pages_list,to_post_positions,img







'''
------------------------------------------------------------------FOR CREATING REELS-------------------------------------------------------------------------
'''

def master_function_goodreads_reels():
    run=True
    pages_list_reels = read_pagelist_data("pages_list_data_reels.csv") 
    while(run):
        try:
            posted_reels = read_posted_data("posted_data_reels.csv")
        except:
            write_data([True],"posted_data_reels.csv")
            posted_reels = read_posted_data("posted_data_reels.csv")
                                                          # gives a list of whether a quote has been posted on instagram or not
        
        #print(posted)
        left_to_post_reels = False                              # Checks if all the current posts have been posted
        for i in range(0,len(posted_reels)):
            #print(type(posted_reels[i]))
            if (posted_reels[i]==False):
                left_to_post_reels = True
                break
            
        #print(left_to_post)                                               
                                                       #If all current quotes have been made and posted
    
        if(left_to_post_reels==False):
            print("Na bhai kuchh na bacha post karne ko")
            print("ruk banata main kuchh")
            
            
            page_count_reels=0
            while(page_count_reels<len(pages_list_reels) and pages_list_reels[page_count_reels][2]==True):
                page_count_reels+=1
                
            pages_reels = [pages_list_reels[page_count_reels][0],pages_list_reels[page_count_reels][1]]
            print("getting pages",pages_reels[0],"to",pages_reels[1])
        
            #filename_reels = str(pages_reels[0]) + "to" + str(pages_reels[1])
        
            unrefined_quotes, authors, posted_reels = get_motivational_quotes(pages_reels)
            quotes = refine_quotes(unrefined_quotes)
            write_data(posted_reels,"posted_data_reels.csv")
            write_data(quotes,"quotes_data_reels.csv")
            write_data(authors,"authors_data_reels.csv")
            write_data(unrefined_quotes,"unrefined_quotes_reels.csv")
            pages_list_reels[page_count_reels][2]=True
            
            
            
        else:
            to_post_positions_reels=[]
            quotes = read_data("quotes_data_reels.csv")
            authors = read_data("authors_data_reels.csv")
            unrefined_quotes = read_data("unrefined_quotes_reels.csv")
            for i in range(0,len(posted_reels)):
                if posted_reels[i]==False:
                    to_post_positions_reels.append(i)
            #print(to_post_positions)  
            #try:
            post_number_reels = random.choice(to_post_positions_reels)
            posted_reels[post_number_reels]=True
            to_post_positions_reels.remove(post_number_reels)
            #print(datetime.now())
            reel_name = str(datetime.date.today()) + "-" + str(post_number_reels) 
            #print(image_name)
            #to post reels
            reel = motivational_reel_create(quotes[post_number_reels],unrefined_quotes[post_number_reels],authors[post_number_reels],reel_name)    
            #except:
                #print("not enough quotes!")
                #left_to_post=False
            #print(posted)
            #print(to_post_positions)
            write_data(posted_reels,"posted_data_reels.csv")
            run=False
    write_pagelist_data(pages_list_reels,"pages_list_data_reels.csv")
    return posted_reels, pages_list_reels,to_post_positions_reels,reel
