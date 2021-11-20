# Make By Nattawatt Hongthong (Oreo Young Man)
import instaloader
from PIL import Image, ImageTk
import os


#create instance
loader = instaloader.Instaloader()
#get username (publiic)
user = input('Enter username on public instagram account: ')
#download proflie
loader.download_profile(user, profile_pic= True)
#get list of image from folder
img = [x for x in os.listdir(f'{os.getcwd()}/{user}') if x.endswith('jpg')]
#read Image from list
img = Image.open(f'{os.getcwd()}/{user}/{img[0]}')
#display Image
img.show()