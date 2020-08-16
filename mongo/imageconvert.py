
import time
from PIL import Image
import os

for f in os.listdir('images/'):
    print(f)
sizes=(300, 300)
p=Image.open('C:\\Users\\NITESH\\Desktop\\python\\images\\lol.png')

print("creating a thumbnail ....")
time.sleep(5)
p.thumbnail(sizes)

saved_path="lenna.jpg"
p.save(saved_path)
print("done ... ")