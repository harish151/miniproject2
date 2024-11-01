from flask import *
from demo import product_data
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
                search_query1,search_query2 = request.form.get('search_query1'),request.form.get('search_query2')
                data1=product_data(search_query1)
                data2=product_data(search_query2)
                maincamera1,maincamera2 = "",""
                for index, (key, val) in enumerate(data1['gsmMainCameraDetails'].items()):
                        if index == 1:  # Assuming 'c' is the second key
                                maincam1 = maincamera1.replace("",val)
                print(maincam1)
                for index, (key, val) in enumerate(data2['gsmMainCameraDetails'].items()):
                        if index == 1:  # Assuming 'c' is the second key
                                maincam2 = maincamera2.replace("",val)
                print(maincam2)
                return render_template('project.html',data1=data1,data2=data2,maincam1=maincam1,maincam2=maincam2)
        return render_template('project.html')

if __name__=='__main__':
        app.run(debug=True,host='0.0.0.0')