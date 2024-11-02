from flask import *
from apis import product_data,image
from points import suggestion
from databases import login_data,upload_data
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
                email = request.form.get('email')
                password = request.form['password']
                value = login_data(email, password)
                if value == True:
                        return render_template("mainpage.html")
                else:
                        return render_template('login.html',error="Invalid Details!")
        return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
        if request.method == 'POST':
                try:
                        gmail = request.form.get('email')
                        passwd = request.form['password']
                        username = request.form.get('username')
                        upload_data(username,gmail, passwd)
                        return render_template('success.html')
                except:
                        return render_template('signup.html',error="User Already Exist!")
        return render_template("signup.html")

@app.route('/compare', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
                search_query1,search_query2 = request.form.get('search_query1'),request.form.get('search_query2')
                data1=product_data(search_query1)
                data2=product_data(search_query2)
                maincamera1,maincamera2 = "",""
                for index, (key, val) in enumerate(data1['gsmMainCameraDetails'].items()):
                        if index == 1:
                                maincam1 = maincamera1.replace("",val)
                for index, (key, val) in enumerate(data2['gsmMainCameraDetails'].items()):
                        if index == 1:
                                maincam2 = maincamera2.replace("",val)
                suggest = suggestion(data1,data2)
                img1 = image(data1['phoneDetails']['customId'])
                img2 = image(data2['phoneDetails']['customId'])
                return render_template('mainpage.html',data1=data1,data2=data2,maincam1=maincam1,maincam2=maincam2,suggest=suggest,img1=img1,img2=img2)
        return render_template('mainpage.html')

if __name__=='__main__':
        app.run(debug=True,host='0.0.0.0')
