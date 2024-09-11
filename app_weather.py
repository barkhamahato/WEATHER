from flask import Flask,render_template,flash,request
import voice_search
import weather

app = Flask(__name__)    #create object of Flask class
app.secret_key="jhjd67hut67euwhgyut7ew"


@app.route('/')
def index():
    return render_template("index_weather.html")

@app.route('/search')
def search():
    try:
        city=voice_search.search()
    except:
        flash("voice is not audible!!")
        return render_template("index_weather.html")

    weather.forecast(city)
    return render_template("index_weather.html",cityname=city)

@app.route('/search_text',methods=['GET','POST'])
def search_text():
    if request.method=='POST':
        city=request.form['city']
        weather.forecast(city)
        return render_template("index_weather.html",cityname=city)

if __name__=='__main__':
    app.run(debug=True)   # activate flask server
