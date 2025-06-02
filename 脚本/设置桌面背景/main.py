from PIL import Image
import ctypes
import os

def save_image(image_path):
    image=Image.open(image_path) #打开图片
    rgb_image=image.convert("RGB")
    rgb_image.save("D:/piture/background.png")

def set_wallpaper(image_path):
    if not os.path.exists(image_path):
        print(f"{image_path}路径不存在")
        return
    
    ctypes.windll.user32.SystemParametersInfoW(20,0,image_path,0)
    print(f"桌面已改为{image_path}")


if __name__=='__main__':
    save_image("D:/updown/background.jpg")
    set_wallpaper("D:/piture/background.png")
