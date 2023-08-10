from _post_on_instagram import *
import customtkinter as ctk


#future updates -- add a scroll widget and add panels for other inspirarchive channels

#Setting up root
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root = ctk.CTk()
root.geometry("500x350")

#defining button functionalities

#for INSPIRAGROW
#to share a post
def inspiragrow_post_btn():
    consistent_image_path = str(Path("E:\Inspirarchive\Inspiragrowth\inspiragrow_automation\_quotes_template.png"))
    caption_post="goo goo ga ga"
    post_on_instagram(consistent_image_path,caption_post)
#to share a reel        
def inspiragrow_reel_btn():
    caption_reel="googa"
    reel_on_instagram(caption_reel)
    
#for INSPIRADREAM
#to share a post
def inspiradream_post_btn():
    print("functionality not available")
#to share a reel
def inspiradream_reel_btn():
    print("functionality not available")


#defining function to collapse and expand sections
def toggle_frame(frame):
    if frame.winfo_ismapped():
        frame.pack_forget()
    else:
        frame.pack(fill="both", pady=2)
        
        
#Creating the title frame
frame_title=ctk.CTkFrame(master=root)
frame_title.pack(fill="both")
label_heading= ctk.CTkLabel(master=frame_title,text="Inspirarchive Control Panel",font=("Impact",30))
label_heading.pack(pady=10)

#Creating the parent frame    
frame_parent = ctk.CTkFrame(master=root)
frame_parent.pack(pady=10,padx=20,fill="both",expand=True)

#Creating the Inspiragrow frame
frame_inspiragrow = ctk.CTkFrame(master=frame_parent)
frame_inspiragrow.pack(fill="both",pady=2)

frame_inspiragrow_subheading = ctk.CTkFrame(master=frame_inspiragrow, fg_color="chartreuse4")
frame_inspiragrow_subheading.pack(fill="both")
label_subheading_inspiragrow = ctk.CTkLabel(master=frame_inspiragrow_subheading,text="InspiraGrow", font=("Impact",24))
label_subheading_inspiragrow.pack(pady=10)

frame_inspiragrow_content = ctk.CTkFrame(master=frame_inspiragrow)
frame_inspiragrow_content.pack(fill="both")

post_button_inspiragrow = ctk.CTkButton(master=frame_inspiragrow_content,text="Share a Post",font=("Montserrat",16),command=inspiragrow_post_btn)
post_button_inspiragrow.pack(side="left",padx=(50,10),pady=(20,10))
reel_button_inspiragrow = ctk.CTkButton(master=frame_inspiragrow_content,text="Share a Reel",font=("Montserrat",16),command=inspiragrow_reel_btn)
reel_button_inspiragrow.pack(side="left", padx=(50,10),pady=(20,10))

frame_inspiragrow_content.pack_forget()
label_subheading_inspiragrow.bind("<Button-1>", lambda event: toggle_frame(frame_inspiragrow_content))






#Create a placeholder inspiradream frame
frame_inspiradream = ctk.CTkFrame(master=frame_parent)
frame_inspiradream.pack(fill="both",pady=5)

frame_inspiradream_subheading = ctk.CTkFrame(master=frame_inspiradream, fg_color="chartreuse4")
frame_inspiradream_subheading.pack(fill="both")
label_subheading_inspiradream = ctk.CTkLabel(master=frame_inspiradream_subheading,text="InspiraDream", font=("Impact",24))
label_subheading_inspiradream.pack(pady=10)

frame_inspiradream_content = ctk.CTkFrame(master=frame_inspiradream)
frame_inspiradream_content.pack(fill="both")

post_button_inspiradream = ctk.CTkButton(master=frame_inspiradream_content,text="Share a Post",font=("Montserrat",16),command=inspiradream_post_btn)
post_button_inspiradream.pack(side="left",padx=(50,10),pady=(20,10))
reel_button_inspiradream = ctk.CTkButton(master=frame_inspiradream_content,text="Share a Reel",font=("Montserrat",16),command=inspiradream_reel_btn)
reel_button_inspiradream.pack(side="left", padx=(50,10),pady=(20,10))

frame_inspiradream_content.pack_forget()
label_subheading_inspiradream.bind("<Button-1>", lambda event: toggle_frame(frame_inspiradream_content))



root.mainloop()