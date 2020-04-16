#Ahmad Amjad Mughal
#121672
#Necessary libraries
import PIL
from PIL import Image

#required function for Normalizing Red Band
def RedNormalization(intensity):
    minImage = 90
    maxImage = 200
    output = (intensity - minImage)*(((255 - 0)/(maxImage - minImage)) + 0)

    return output
#required function for Normalizing Green Band
def GreenNormalization(intensity):
    minImage = 95
    maxImage = 205
    output = (intensity - minImage)*(((255 - 0)/(maxImage - minImage)) + 0)
    return output

#required function for Normalizing Blue Band
def BlueNormalization(intensity):
    minImage = 101
    maxImage = 220
    output = (intensity - minImage)*(((255 - 0)/(maxImage - minImage)) + 0)
    return output

#Open an Image and convert it into RGB
image = Image.open('myImage.jpg').convert('RGB')

#Split the image into respective Colour bands
splitImage = image.split()

#Getting the improved intensity value of reespective color band and update intensiy level 
redBand = splitImage[0].point(RedNormalization)
greenBand = splitImage[1].point(GreenNormalization)
blueBand = splitImage[2].point(BlueNormalization)

#merging the splitted image into one RGB Image
mergedImage = Image.merge('RGB',(redBand,greenBand,blueBand))

mergedImage.show()
mergedImage.save('NewContrastedImage.jpg')
