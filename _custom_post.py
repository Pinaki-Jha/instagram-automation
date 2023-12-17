

def get_slide_count():
    while True:
        slide_count = int(input("Enter the no. of slides:"))
        if slide_count<=10:
            break
        print("Total slides cannot be greater than 10")
    print("yay")
    return slide_count


def create_custom_post():
    slide_count = get_slide_count()
    print(slide_count)





