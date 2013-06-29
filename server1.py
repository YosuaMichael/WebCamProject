from flask import Flask, jsonify, render_template, request ,\
send_file, make_response
from PIL import Image
import StringIO

app = Flask(__name__)

#global count
#count=0
#global img_1
#global img_2
#img_1 = Image.open('pictures/image_1.png')
#img_2 = Image.open('pictures/image_2.png')

def serve_pil_image(pil_img):
    img_io = StringIO.StringIO()
    pil_img.save(img_io, 'PNG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

def get_file():
    f = open("data/temp.txt","r")
    return str(f.read())

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a+b)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_get_pictures')
def get_pictures():
    print 'In_Get_Pictures'
    file_index = get_file()
    img_1 = Image.open('data/temp' + file_index + '.png')
    return serve_pil_image(img_1)
    '''if count%2 == 0:
        #return send_file(img_1, mimetype='image/png')
        return serve_pil_image(img_1)
    else:
        #return send_file(img_2, mimetype='image/png')
        return serve_pil_image(img_2)'''

if __name__ == "__main__":
    global count
    global img_1
    global img_2
    count = 0
    #img_1 = Image.open('pictures/image_1.png')
    #img_2 = Image.open('pictures/image_2.png')



    app.debug = True
    app.run()
