from flask import Flask, render_template, request
import os
from hdbcli import dbapi

conn = dbapi.connect(
    address="zeus.hana.canary.eu-central-1.whitney.dbaas.ondemand.com", 
    port= 21761, 
    user="SYSTEM", 
    password="Abcd1234",
    encrypt="true",
    sslValidateCertificate="false"

)
cursor = conn.cursor()
cursor.execute("set schema EXOPLANETS")


IMAGE_PATH = "https://upload.wikimedia.org/wikipedia/commons/2/2f/Hubble_ultra_deep_field.jpg"
# "/Users/d022166/SAP/GitRepos/Exoplanets/app/static/images/DeepSpace.jpg"
IMAGE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['IMAGE_FOLDER'] = IMAGE_PATH

@app.route('/',  methods=['GET', 'POST'])
def show_image():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('submit') == 'submit':
            # pass
            sql = 'SELECT TOP 5 "ID", "LABEL" from EXOTEST;'
            cursor.execute(sql)
            data = cursor.fetchall()
            conn.close()
            print (data)	
            #for row in cursor:
            #    print(row)	
            newarray = []
            newtuple = ()
            for i in data:
                if i[1] == 2:
                    newtuple = (i[0], i[1], "planet")
                if i[1] == 1:
                    newtuple = (i[0], i[1], "star")        
                newarray.append(newtuple)       


            return render_template("index.html", image = IMAGE_PATH, text = "Hello World", data = newarray )	
    return render_template("index.html", image = IMAGE_PATH)

if __name__ == "__main__":
    app.run()
