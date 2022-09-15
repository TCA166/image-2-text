from PIL import Image
from tqdm import trange
import math
import traceback
#this be classic table with 69 elements haha funny
table_asci = ['$','@','B','%','8','&','W','M','#','*','o','a','h','k','b','d','p','q','w','m','Z','O','0','Q','L','C','J','U','Y','X','z','c','v','u','n','x','r','j','f','t','/','|','(',')','1','{','}','[',']','?','-','_','+','~','<','>','i','!','l','I',';',':',',','"','^','`',"'",'.',' ']
#my favourite
table_3colour = ['█', '▄', ' ']
#shade
table_shade = ['█', '▓', '▒', '░', ' ']
#expanded 3
table_5colour = ['█', '▄', '=', '_', ' ']
#expanded 5
table_7colour = ['█', '▓', '▒', '░', '_', '.', ' ']
#expanded 7
table_9colour = ['█', '▓', '▒', '░', '=', '_', '+', '.', ' ']

def generate_ascii_image(image_path,table):
    #string result variable
    result = ''
    #brightness offset between table elements
    bright_diff = math.ceil(256/len(table))
    #feedback
    print('Brightness table length: ' + str(len(table)))
    print('Brightness resolution: ' + str(bright_diff))
    #get image
    imag = Image.open(image_path)
    imag = imag.convert ('RGB')
    #this is here to compenstate for width
    aspect_ratio = math.ceil(imag.width/imag.height) * 2
    #foreach pixel row
    for h in trange(0,imag.height):
        #foreach pixel column
        for w in range(0,imag.width):
            pixelRGB = imag.getpixel((w,h))
            R,G,B = pixelRGB 
            brightness = sum([R,G,B])/3
            index = math.floor(brightness/bright_diff)
            #print(index)
            result = result + (table[index]*aspect_ratio)
        result = result + '\n'
    return result

if __name__ == "__main__":
    image_path = input('Image Path:')
    result = generate_ascii_image(image_path,table_shade)
    try:
        try:
            with open(image_path + '.txt', 'x', encoding="utf-8") as f:
                f.write(result)
                f.close()
        except:
            with open(image_path + '.txt', 'r+', encoding="utf-8") as f:
                data = f.read()
                f.seek(0)
                f.write(result)
                f.truncate()
    except:
        print(traceback.format_exc())