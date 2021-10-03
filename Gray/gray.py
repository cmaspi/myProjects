from PIL import Image

img=Image.open('img.png')
GrayImg= img.convert('L')
GrayImg.save('gray.png')
GrayImg.show()