from PIL import Image
open_image = Image.open(r'C:\Users\Dell\Pictures\Camera Roll\WIN_20200506_10_59_59_Pro.jpg')
convert_to_bw = open_image.convert('L')
convert_to_bw.show()