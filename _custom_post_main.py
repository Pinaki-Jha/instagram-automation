import customtkinter as ctk
from _custom_post import *


def update_char_count(entry,label,char_count,char_limit=200):
    char_count.set(len(entry.get()))    
    if len(entry.get()) >= char_limit:
        label.configure(text="I SAID. UNDER. 200. WORDS. Word Count :  ")
    else:
        label.configure(text="Please keep it under 200 words. Word Count :")
        
        
def custom_post_main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    root = ctk.CTk()
    root.geometry("500x350")
    root.title("Custom Post Generator")
    
    char_count = ctk.IntVar()
    char_count.set(0)
    
    
    frame_title=ctk.CTkFrame(master=root)
    frame_title.pack(fill="both")
    label_heading= ctk.CTkLabel(master=frame_title,text="Custom Post Generator",font=("Impact",30))
    label_heading.pack(pady=10)
    
    frame_parent = ctk.CTkFrame(master=root)
    frame_parent.pack(pady=10,padx=20,fill="both",expand=True)
    
    frame_title = ctk.CTkFrame(master=frame_parent)
    frame_title.pack(fill="both")
    label_title = ctk.CTkLabel(master=frame_title,text="Title", font=("Impact",24))
    label_title.pack(side="left",pady=10,padx=20)
    entry_title = ctk.CTkEntry(master=frame_title)
    entry_title.pack(side="left")
    
    frame_content = ctk.CTkFrame(master=frame_parent)
    frame_content.pack(fill="both")
    label_content = ctk.CTkLabel(master=frame_content,text="Content",font=("Impact",18))
    label_content.pack(side="left",padx=10)
    entry_content = ctk.CTkEntry(master=frame_content,width=300)
    #entry_content.configure(font=("Montserrat", 12))
    entry_content.pack()
    cc_label = ctk.CTkLabel(master=frame_content, text="Please keep it under 200 words. Word Count :")
    cc_label.pack(side = "left")
    
    entry_content.bind("<Key>", lambda event: update_char_count(entry_content,cc_label,char_count,200))
    
    char_count_label = ctk.CTkLabel(master=frame_content, textvariable=char_count)
    char_count_label.pack(side="right",padx=10)
    
    #yeh 10 baar karna hai


    
    
    root.mainloop()
    

    
    
    
    





custom_post_main()