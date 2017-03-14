import urllib.request
import random

# The image is stored under your project folder.
# You need to refresh your eclipse project before you see the image in your class path.
def downloadImage(url):
    urllib.request.urlretrieve(url, str(random.randrange(1, 1000)) + '.jpg')
downloadImage('https://images-na.ssl-images-amazon.com/images/G/01/img15/pet-products/small-tiles/23695_pets_vertical_store_dogs_small_tile_8._CB312176604_.jpg')


