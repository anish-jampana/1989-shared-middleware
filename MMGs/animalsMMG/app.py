import sys
sys.path.insert(1, '/Users/anishjampana/Downloads/mosaic/1989-shared-middleware/')
import mosaic
from flask import Flask, request, jsonify
from PIL import Image as im
from io import BytesIO
import base64
import requests
import psutil
import os



app = Flask(__name__)

url = 'http://127.0.0.1:5000/addMMG'
data = {"name": "animalsMMG", "url": "http://127.0.0.1:7001/", "author": "Anish Jampana"}

response = requests.put(url, data=data)

@app.route('/', methods=["POST"])
def createMosaic():
    f = request.files["image"]
    image = im.open(BytesIO(f.read()))
    jpg_image = image.convert('RGB')
    tilesAcross = int(request.args.get("tilesAcross"))
    renderedTileSize = int(request.args.get("renderedTileSize"))
    
    mosaic.genMosaic(jpg_image, "animals", tilesAcross, renderedTileSize)

    with open("output.png", "rb") as f:
        buffer = f.read()
    b64 = base64.b64encode(buffer)
    response = {"image": "data:image/png;base64," + b64.decode("utf-8")}

    return [response]


    
