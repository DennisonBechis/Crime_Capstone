from PIL import Image
import glob


frames = []
imgs = glob.glob("/Users/bechis/DSI/repo/Crime_Capstone/images/HeatMapGif/*.png")
print(imgs)

for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

frames[0].save('png_to_gif.gif', format='GIF', append_images=frames[1:], save_all=True, duration=300, loop=0)
