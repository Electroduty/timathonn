from os import stat_result
from flask import Flask, render_template, request
from geopy import *
import requests
from pprint import pprint
from selenium import webdriver
from werkzeug.utils import redirect
import os
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from werkzeug.utils import secure_filename
import sqlite3


#Flask Init
app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.mp3', '.mp4']
app.config['UPLOAD_PATH'] = 'uploads'

#SQLite3 Init
#none

#Connect to database
con = sqlite3.connect('Videofilelink.db')

#hashtag

#Define cursor for database
cur = con.cursor()

#home route
@app.route('/home')
def home():
    # return render_template('home.html')
    return render_template('real_home.html')

#Rating route
@app.route('/rating')
def rating():
    return render_template('rating.html')



#route to get maps
@app.route('/data', methods = ['POST', 'GET'])
def index():
    global lat
    global log
    global Locality
    if request.method == "POST":
        Country = request.form['Country']
        State = request.form['State']
        Locality = request.form['Locality']
        locator = Nominatim(user_agent='app')
        location = locator.geocode('{}, {}, {}'.format(Locality,State,Country))
        lat = location.latitude
        log = location.longitude

        geocode = str(lat)+','+str(log)
        return render_template('bing_maps.html', geocode=geocode)
    elif request.method == "GET":
        return render_template('data.html')


#route to get all nearby places by selection
@app.route('/maps', methods = ['POST', 'GET'])
def maps():
    if request.method == "POST":



        #Get suggestions\
        typ = request.form['Type']
        # print(typ)
        URL = "https://discover.search.hereapi.com/v1/discover"

        latitude = lat
        longitude = log


        api_key = 'id9PFVL6rOpgypwTb_FG10ZMRMaHKScQwP01khV1Y0U' # Acquire from developer.here.com
        query = typ
        limit = 5

        PARAMS = {
                    'apikey':api_key,
                    'q':query,
                    'limit': limit,
                    'at':'{},{}'.format(latitude,longitude)
                }

        # sending get request and saving the response as response object
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()
        # print(data)
        pprint(data)


        hospitalOne = data['items'][0]['title']
        hospitalOne_address =  data['items'][0]['address']['label']
        hospitalOne_latitude = data['items'][0]['position']['lat']
        hospitalOne_longitude = data['items'][0]['position']['lng']
        # if  data['items'][0]['contacts'][0]['phone'][0]['value']:
        #     hospitalOnephone = data['items'][0]['contacts'][0]['phone'][0]['value']

        # else:
        #     hospitalOnephone = data['items'][3]['contacts'][0]['mobile'][0]['value']


        hospitalTwo = data['items'][1]['title']
        hospitalTwo_address =  data['items'][1]['address']['label']
        hospitalTwo_latitude = data['items'][1]['position']['lat']
        hospitalTwo_longitude = data['items'][1]['position']['lng']
        # hospitalTwophone = data['items'][1]['contacts'][0]['mobile'][0]['value']
        # if  data['items'][3]['contacts'][0]['phone'][0]['value']:
        #     hospitalTwophone = data['items'][1]['contacts'][0]['phone'][0]['value']

        # else:
        #     hospitalTwophone = data['items'][1]['contacts'][0]['mobile'][0]['value']

        hospitalThree = data['items'][2]['title']
        hospitalThree_address =  data['items'][2]['address']['label']
        hospitalThree_latitude = data['items'][2]['position']['lat']
        hospitalThree_longitude = data['items'][2]['position']['lng']
        # hospitalThreephone = data['items'][2]['contacts'][0]['phone'][0]['value']

        # if  data['items'][2]['contacts'][0]['phone'][0]['value']:
        #     hospitalThreephone = data['items'][2]['contacts'][0]['phone'][0]['value']

        # else:
        #     hospitalThreephone = data['items'][2]['contacts'][0]['mobile'][0]['value']


        hospitalFour = data['items'][3]['title']
        hospitalFour_address =  data['items'][3]['address']['label']
        hospitalFour_latitude = data['items'][3]['position']['lat']
        hospitalFour_longitude = data['items'][3]['position']['lng']
        # if  data['items'][3]['contacts'][0]['phone'][0]['value']:
        #     hospitalFourphone = data['items'][3]['contacts'][0]['phone'][0]['value']

        # else:
        #     hospitalFourphone = data['items'][3]['contacts'][0]['mobile'][0]['value']




        hospitalFive = data['items'][4]['title']
        hospitalFive_address =  data['items'][4]['address']['label']
        hospitalFive_latitude = data['items'][4]['position']['lat']
        hospitalFive_longitude = data['items'][4]['position']['lng']
        # hospitalFivephone = data['items'][4]['contacts'][0]['phone'][0]['value']

        # if  data['items'][4]['contacts'][0]['phone'][0]['value']:
        #     hospitalFivephone = data['items'][4]['contacts'][0]['phone'][0]['value']

        # else:
        #     hospitalFivephone = data['items'][4]['contacts'][0]['mobile'][0]['value']
        print('   ')
        # print(hospitalphone)

        # hospitalSix = data['items'][5]['title']
        # hospitalSix_address =  data['items'][5]['address']['label']
        # hospitalSix_latitude = data['items'][5]['position']['lat']
        # hospitalSix_longitude = data['items'][5]['position']['lng']
        # hospitalphone = data['items'][5]['phone']['value']
        # print(hospitalFive_address)

        #DEBBUGGING PURPOSES ONLY
        # print(hospitalOne)
        # print(hospitalTwo)
        # print(hospitalThree)
        # print(hospitalFour)
        # print(hospitalFive)
        # print(hospitalFive_latitude, hospitalFive_longitude)

        geocode = str(hospitalFive_latitude)+','+str(hospitalFive_longitude)
        # search_string = "https://justdial.com"
        # browser = webdriver.Chrome('/home/gaurav/Downloads/chromedriver')
        # browser.get(search_string)

        return render_template('location.html' , geocode=geocode, hospitalFive=hospitalFive, hospitalFive_longitude=hospitalFive_longitude, hospitalFive_latitude=hospitalFive_latitude,hospitalFive_address=hospitalFive_address, hospitalFour_latitude=hospitalFour_latitude,hospitalFour_longitude=hospitalFour_longitude, hospitalFour=hospitalFour,hospitalFour_address=hospitalFour_address, typ=typ, Locality=Locality, hospitalThree=hospitalThree, hospitalThree_latitude=hospitalThree_latitude, hospitalThree_longitude=hospitalThree_longitude,hospitalThree_address=hospitalThree_address, hospitalTwo_longitude=hospitalTwo_longitude, hospitalTwo_latitude=hospitalTwo_latitude, hospitalTwo=hospitalTwo,hospitalTwo_address=hospitalTwo_address, hospitalOne=hospitalOne, hospitalOne_longitude=hospitalOne_longitude, hospitalOne_latitude=hospitalOne_latitude, hospitalOne_address=hospitalOne_address)

#route to return



        #Get suggestions\
        # print(typ)
        URL = "http://dev.virtualearth.net/REST/v1/Routes?wayPoint.1=Benfaluru&viaWaypoint.2=Mysur&heading={heading}&optimize={optimize}&avoid={avoid}&distanceBeforeFirstTurn={distanceBeforeFirstTurn}&routeAttributes={routeAttributes}&timeType={timeType}&dateTime={dateTime}&maxSolutions={maxSolutions}&tolerances={tolerances}&distanceUnit={distanceUnit}&key=ApoSfk2tKg5S1J5L3DFAMjfwreSS62XGMtLE9NsAmGcNWQJ21lAeRJs3w1LML19X"

@app.route('/Estreams')
def home_page():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('home_estreams.html', files=files)

@app.route('/uploads')
def index2():
    files = os.listdir(app.config['UPLOAD_PATH'])
    filearr = files[0:1]
    #Insert vidlinks into database
    return render_template('upload.html', files=files)


#Upload route to process files
@app.route('/uploads', methods=['POST'])
def upload_files():
    #SQLite3 Init

    #Connect to database
    con = sqlite3.connect('Videofilelink.db')

    #Define cursor for database
    cur = con.cursor()

    #request files from html
    uploaded_file = request.files['file']
    
    #request title from html
    title = request.form['title']
    print(title)

    #Init filename
    filename = secure_filename(uploaded_file.filename)
    print(filename)

    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))

    #File array
    files = os.listdir(app.config['UPLOAD_PATH'])

    #Send each filename in file list to database
    for file in files:
        cur.execute("INSERT INTO Videolinks (vlink) VALUES('"+file+"')")
        cur.execute("INSERT INTO Videolinks (vtitle) VALUES('"+title+"')")
        con.commit()

    #Request search
    search = request.form['search']
    print(search)
    search_sql = cur.execute('SELECT * FROM Videolinks WHERE vlink LIKE"%'+search+'%"')
    global search_url
    if search != '':
        search_url = search_sql.fetchone()
        con.commit()
        srch_url = search_url[0]
        return redirect('/'+str(srch_url))
    else:
        return render_template('upload.html')
@app.route('/<srch_url>')
def home2(srch_url):
    new_srch_url = '/uploads/'+srch_url
    return render_template('search.html', srch_url=srch_url, new_srch_url=new_srch_url);


#Upload route init
@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)










if __name__ == '__main__':
    app.run(debug=True)














# locator = Nominatim(user_agent='app')
# location = locator.geocode("Champ de Mars, Paris, France", Locality, State, Country)

# print('Latitude = {}, Longitude = {}'.format(location.latitude, location.longitude))

#+918792066194
