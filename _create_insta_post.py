from _master_function import *
def insta_post_create():
    try:
        read_pagelist_data("pages_list_data.csv")       #See if a pagelist already exists
    except:
        print("No pagelist available.")
        print("Creating a new pages list")
        create_pages_list("pages_list_data.csv")        #If a pagelist doesn't exist, create one
        
    posted,pages_list,to_post_positions,image_name = master_function_goodreads()
    print(image_name+" created.")
    return posted, pages_list ,to_post_positions,image_name