from flask import Flask
from flask import render_template
import os
import glob

app = Flask(__name__)


''' images_folder must be located inside the static folder in a folder name "images" '''
images_folder =  os.getcwd()
for_later = images_folder + "/static/"
images_folder = images_folder + "/static/images/"


photos = glob.glob(images_folder + "*")
list_of_images = []

for every in photos:
    every = every.replace(for_later, '')
    list_of_images.append(every)

@app.route('/')
def create_image_gallery():
    return render_template('index.html', data=list_of_images)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)