from _master_function import *

#Get the openAI thingy?
#syllaby.io for script generation
#Synthesia.io for video generation


def insta_reel_create():
    try:
        pagelist_reels = read_pagelist_data("pages_list_data_reels.csv")
    except:
        create_pages_list("pages_list_data_reels.csv")
        
    posted,pages_list,to_post_positions,reel_name = master_function_goodreads_reels()
    
    
    return posted, pages_list ,to_post_positions,reel_name



#insta_reel_create()


#posted, pages_list,to_post_positions,img = master_function_goodreads()    
#print(posted)
