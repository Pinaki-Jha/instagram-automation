from _master_function import *
def insta_post_create():
    try:
        pages_list_temp = read_pagelist_data("pages_list_data.csv")
    except:
        create_pages_list("pages_list_data.csv")
        
    posted,pages_list,to_post_positions,image_name = master_function_goodreads()
    #print(image_name)
    return posted, pages_list ,to_post_positions,image_name

#insta_post_create()