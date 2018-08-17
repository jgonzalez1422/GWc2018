from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

black = (0, 0, 0)
darkGray = (45, 45, 45)
lightGray = (160, 160, 160)
white = (255, 255, 255)

turquoise = (175, 238, 238)
pink = (255, 192, 203)
green = (152, 251, 152)
purple = (216, 191, 216)

# Import image.
image = input("What image do you want to edit? (Ex: Kitten.jpg) ")
my_image = Image.open(image) #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
filter = input("Do you want a patriotic filter(a), grayscale filter(b), or a pastel filter(c); type 'a', 'b', or 'c': ")
filter = filter.lower()
if filter == "a":
    for pixel in image_list:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            recolored.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            recolored.append(red)
        elif intensity >= 364 and intensity < 546:
            recolored.append(lightBlue)
        elif intensity >= 546:
            recolored.append(yellow)
elif filter == "b":
    for pixel in image_list:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            recolored.append(black)
        elif intensity >= 182 and intensity < 364:
            recolored.append(darkGray)
        elif intensity >= 364 and intensity < 546:
            recolored.append(lightGray)
        elif intensity >= 546:
            recolored.append(white)
elif filter == "c":
    for pixel in image_list:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            recolored.append(purple)
        elif intensity >= 182 and intensity < 364:
            recolored.append(turquoise)
        elif intensity >= 364 and intensity < 546:
            recolored.append(pink)
        elif intensity >= 546:
            recolored.append(green)

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
