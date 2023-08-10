from _post_on_instagram import *
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Inspirarchive Control Panel")

root.configure(bg="white")

window_width = 400
window_height = 400
#root.geometry(f"{window_width}x{window_height}")



#Create canvas for heading
canvas = tk.Canvas(root, width=400, height=50)
canvas.pack()
canvas.create_rectangle(0,0,400,50, fill="black")
canvas.create_text(200,25,text="INSPIRARCHIVE CONTROL PANEL",font=("Impact", 24),fill="white")

#post and reel button command functions
def post_button_command():
    consistent_image_path = str(Path("E:\Inspirarchive\Inspiragrowth\inspiragrow_automation\_quotes_template.png"))
    caption_post="goo goo ga ga"
    post_on_instagram(consistent_image_path,caption_post)
        
def reel_button_command():
    caption_reel="googa"
    reel_on_instagram(caption_reel)

#a lil bit of beautification
border_label = tk.Label(root,text="--------------------------------------------------------------") 
inspiragrow_title_label = tk.Label(root,text="Inspiragrow Control",font=("Impact", 24)) 
border_label.pack()
inspiragrow_title_label.pack()
border_label = tk.Label(root,text="--------------------------------------------------------------") 
border_label.pack()
  
#Creating the button to share a post
post_button = tk.Button(root, text="New Instagram Post",font=("Montserrat", 16), bg="black",fg="white", activebackground="white", activeforeground="black",relief="ridge", command=post_button_command)
post_button.pack(pady=20,padx=10)
#Creating a button to share a reel
reel_button = tk.Button(root, text="New Instagram Reel", font=("Montserrat", 16), bg="black",fg="white", activebackground="white", activeforeground="black",relief="ridge", command=reel_button_command)
reel_button.pack(pady=20,padx=10)



# Start the Tkinter event loop
root.mainloop()
