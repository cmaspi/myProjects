from PIL import Image

img=Image.open('img.png')
GrayImg= img.convert('L')
GrayImg.save('BW_img.png')
GrayImg.show()