from flask import *  
import sqlite3
import pandas as pd
import os
import time
import requests 
import array
import datetime
#from operator import itemgetter, attrgetter

weather_key = "243bcb47bdea9ca83bca929eddc3aeb4"
weather_url = "https://api.openweathermap.org/"
geo_url = "geo/1.0/direct?"
weather_req = "data/2.5/forecast?"




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random
import math 
import time

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
#from sklearn.svm import LinearSVR 
from sklearn.metrics import mean_squared_error, mean_absolute_error


from sklearn import preprocessing
from sklearn import utils
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


from sklearn import preprocessing
from sklearn import utils


import pickle






__STATES = ['Andaman and Nicobar Islands', 'Andhra Pradesh',
       'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
       'Chhattisgarh', 'Dadra and Nagar Haveli', 'Goa', 'Gujarat',
       'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir ', 'Jharkhand',
       'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
       'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry',
       'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana ',
       'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']

__DISTRICTS = ['NICOBARS', 'NORTH AND MIDDLE ANDAMAN', 'SOUTH ANDAMANS',
       'ANANTAPUR', 'CHITTOOR', 'EAST GODAVARI', 'GUNTUR', 'KADAPA',
       'KRISHNA', 'KURNOOL', 'PRAKASAM', 'SPSR NELLORE', 'SRIKAKULAM',
       'VISAKHAPATANAM', 'VIZIANAGARAM', 'WEST GODAVARI', 'ANJAW',
       'CHANGLANG', 'DIBANG VALLEY', 'EAST KAMENG', 'EAST SIANG',
       'KURUNG KUMEY', 'LOHIT', 'LONGDING', 'LOWER DIBANG VALLEY',
       'LOWER SUBANSIRI', 'NAMSAI', 'PAPUM PARE', 'TAWANG', 'TIRAP',
       'UPPER SIANG', 'UPPER SUBANSIRI', 'WEST KAMENG', 'WEST SIANG',
       'BAKSA', 'BARPETA', 'BONGAIGAON', 'CACHAR', 'CHIRANG', 'DARRANG',
       'DHEMAJI', 'DHUBRI', 'DIBRUGARH', 'DIMA HASAO', 'GOALPARA',
       'GOLAGHAT', 'HAILAKANDI', 'JORHAT', 'KAMRUP', 'KAMRUP METRO',
       'KARBI ANGLONG', 'KARIMGANJ', 'KOKRAJHAR', 'LAKHIMPUR', 'MARIGAON',
       'NAGAON', 'NALBARI', 'SIVASAGAR', 'SONITPUR', 'TINSUKIA',
       'UDALGURI', 'ARARIA', 'ARWAL', 'AURANGABAD', 'BANKA', 'BEGUSARAI',
       'BHAGALPUR', 'BHOJPUR', 'BUXAR', 'DARBHANGA', 'GAYA', 'GOPALGANJ',
       'JAMUI', 'JEHANABAD', 'KAIMUR (BHABUA)', 'KATIHAR', 'KHAGARIA',
       'KISHANGANJ', 'LAKHISARAI', 'MADHEPURA', 'MADHUBANI', 'MUNGER',
       'MUZAFFARPUR', 'NALANDA', 'NAWADA', 'PASHCHIM CHAMPARAN', 'PATNA',
       'PURBI CHAMPARAN', 'PURNIA', 'ROHTAS', 'SAHARSA', 'SAMASTIPUR',
       'SARAN', 'SHEIKHPURA', 'SHEOHAR', 'SITAMARHI', 'SIWAN', 'SUPAUL',
       'VAISHALI', 'CHANDIGARH', 'BALOD', 'BALODA BAZAR', 'BALRAMPUR',
       'BASTAR', 'BEMETARA', 'BIJAPUR', 'BILASPUR', 'DANTEWADA',
       'DHAMTARI', 'DURG', 'GARIYABAND', 'JANJGIR-CHAMPA', 'JASHPUR',
       'KABIRDHAM', 'KANKER', 'KONDAGAON', 'KORBA', 'KOREA', 'MAHASAMUND',
       'MUNGELI', 'NARAYANPUR', 'RAIGARH', 'RAIPUR', 'RAJNANDGAON',
       'SUKMA', 'SURAJPUR', 'SURGUJA', 'DADRA AND NAGAR HAVELI',
       'NORTH GOA', 'SOUTH GOA', 'AHMADABAD', 'AMRELI', 'ANAND',
       'BANAS KANTHA', 'BHARUCH', 'BHAVNAGAR', 'DANG', 'DOHAD',
       'GANDHINAGAR', 'JAMNAGAR', 'JUNAGADH', 'KACHCHH', 'KHEDA',
       'MAHESANA', 'NARMADA', 'NAVSARI', 'PANCH MAHALS', 'PATAN',
       'PORBANDAR', 'RAJKOT', 'SABAR KANTHA', 'SURAT', 'SURENDRANAGAR',
       'TAPI', 'VADODARA', 'VALSAD', 'AMBALA', 'BHIWANI', 'FARIDABAD',
       'FATEHABAD', 'GURGAON', 'HISAR', 'JHAJJAR', 'JIND', 'KAITHAL',
       'KARNAL', 'KURUKSHETRA', 'MAHENDRAGARH', 'MEWAT', 'PALWAL',
       'PANCHKULA', 'PANIPAT', 'REWARI', 'ROHTAK', 'SIRSA', 'SONIPAT',
       'YAMUNANAGAR', 'CHAMBA', 'HAMIRPUR', 'KANGRA', 'KINNAUR', 'KULLU',
       'LAHUL AND SPITI', 'MANDI', 'SHIMLA', 'SIRMAUR', 'SOLAN', 'UNA',
       'ANANTNAG', 'BADGAM', 'BANDIPORA', 'BARAMULLA', 'DODA',
       'GANDERBAL', 'JAMMU', 'KARGIL', 'KATHUA', 'KISHTWAR', 'KULGAM',
       'KUPWARA', 'LEH LADAKH', 'POONCH', 'PULWAMA', 'RAJAURI', 'RAMBAN',
       'REASI', 'SAMBA', 'SHOPIAN', 'SRINAGAR', 'UDHAMPUR', 'BOKARO',
       'CHATRA', 'DEOGHAR', 'DHANBAD', 'DUMKA', 'EAST SINGHBUM', 'GARHWA',
       'GIRIDIH', 'GODDA', 'GUMLA', 'HAZARIBAGH', 'JAMTARA', 'KHUNTI',
       'KODERMA', 'LATEHAR', 'LOHARDAGA', 'PAKUR', 'PALAMU', 'RAMGARH',
       'RANCHI', 'SAHEBGANJ', 'SARAIKELA KHARSAWAN', 'SIMDEGA',
       'WEST SINGHBHUM', 'BAGALKOT', 'BANGALORE RURAL', 'BELGAUM',
       'BELLARY', 'BENGALURU URBAN', 'BIDAR', 'CHAMARAJANAGAR',
       'CHIKBALLAPUR', 'CHIKMAGALUR', 'CHITRADURGA', 'DAKSHIN KANNAD',
       'DAVANGERE', 'DHARWAD', 'GADAG', 'GULBARGA', 'HASSAN', 'HAVERI',
       'KODAGU', 'KOLAR', 'KOPPAL', 'MANDYA', 'MYSORE', 'RAICHUR',
       'RAMANAGARA', 'SHIMOGA', 'TUMKUR', 'UDUPI', 'UTTAR KANNAD',
       'YADGIR', 'ALAPPUZHA', 'ERNAKULAM', 'IDUKKI', 'KANNUR',
       'KASARAGOD', 'KOLLAM', 'KOTTAYAM', 'KOZHIKODE', 'MALAPPURAM',
       'PALAKKAD', 'PATHANAMTHITTA', 'THIRUVANANTHAPURAM', 'THRISSUR',
       'WAYANAD', 'AGAR MALWA', 'ALIRAJPUR', 'ANUPPUR', 'ASHOKNAGAR',
       'BALAGHAT', 'BARWANI', 'BETUL', 'BHIND', 'BHOPAL', 'BURHANPUR',
       'CHHATARPUR', 'CHHINDWARA', 'DAMOH', 'DATIA', 'DEWAS', 'DHAR',
       'DINDORI', 'GUNA', 'GWALIOR', 'HARDA', 'HOSHANGABAD', 'INDORE',
       'JABALPUR', 'JHABUA', 'KATNI', 'KHANDWA', 'KHARGONE', 'MANDLA',
       'MANDSAUR', 'MORENA', 'NARSINGHPUR', 'NEEMUCH', 'PANNA', 'RAISEN',
       'RAJGARH', 'RATLAM', 'REWA', 'SAGAR', 'SATNA', 'SEHORE', 'SEONI',
       'SHAHDOL', 'SHAJAPUR', 'SHEOPUR', 'SHIVPURI', 'SIDHI', 'SINGRAULI',
       'TIKAMGARH', 'UJJAIN', 'UMARIA', 'VIDISHA', 'AHMEDNAGAR', 'AKOLA',
       'AMRAVATI', 'BEED', 'BHANDARA', 'BULDHANA', 'CHANDRAPUR', 'DHULE',
       'GADCHIROLI', 'GONDIA', 'HINGOLI', 'JALGAON', 'JALNA', 'KOLHAPUR',
       'LATUR', 'MUMBAI', 'NAGPUR', 'NANDED', 'NANDURBAR', 'NASHIK',
       'OSMANABAD', 'PALGHAR', 'PARBHANI', 'PUNE', 'RAIGAD', 'RATNAGIRI',
       'SANGLI', 'SATARA', 'SINDHUDURG', 'SOLAPUR', 'THANE', 'WARDHA',
       'WASHIM', 'YAVATMAL', 'BISHNUPUR', 'CHANDEL', 'CHURACHANDPUR',
       'IMPHAL EAST', 'IMPHAL WEST', 'SENAPATI', 'TAMENGLONG', 'THOUBAL',
       'UKHRUL', 'EAST GARO HILLS', 'EAST JAINTIA HILLS',
       'EAST KHASI HILLS', 'NORTH GARO HILLS', 'RI BHOI',
       'SOUTH GARO HILLS', 'SOUTH WEST GARO HILLS',
       'SOUTH WEST KHASI HILLS', 'WEST GARO HILLS', 'WEST JAINTIA HILLS',
       'WEST KHASI HILLS', 'AIZAWL', 'CHAMPHAI', 'KOLASIB', 'LAWNGTLAI',
       'LUNGLEI', 'MAMIT', 'SAIHA', 'SERCHHIP', 'DIMAPUR', 'KIPHIRE',
       'KOHIMA', 'LONGLENG', 'MOKOKCHUNG', 'MON', 'PEREN', 'PHEK',
       'TUENSANG', 'WOKHA', 'ZUNHEBOTO', 'ANUGUL', 'BALANGIR',
       'BALESHWAR', 'BARGARH', 'BHADRAK', 'BOUDH', 'CUTTACK', 'DEOGARH',
       'DHENKANAL', 'GAJAPATI', 'GANJAM', 'JAGATSINGHAPUR', 'JAJAPUR',
       'JHARSUGUDA', 'KALAHANDI', 'KANDHAMAL', 'KENDRAPARA', 'KENDUJHAR',
       'KHORDHA', 'KORAPUT', 'MALKANGIRI', 'MAYURBHANJ', 'NABARANGPUR',
       'NAYAGARH', 'NUAPADA', 'PURI', 'RAYAGADA', 'SAMBALPUR', 'SONEPUR',
       'SUNDARGARH', 'KARAIKAL', 'MAHE', 'PONDICHERRY', 'YANAM',
       'AMRITSAR', 'BARNALA', 'BATHINDA', 'FARIDKOT', 'FATEHGARH SAHIB',
       'FAZILKA', 'FIROZEPUR', 'GURDASPUR', 'HOSHIARPUR', 'JALANDHAR',
       'KAPURTHALA', 'LUDHIANA', 'MANSA', 'MOGA', 'MUKTSAR', 'NAWANSHAHR',
       'PATHANKOT', 'PATIALA', 'RUPNAGAR', 'S.A.S NAGAR', 'SANGRUR',
       'TARN TARAN', 'AJMER', 'ALWAR', 'BANSWARA', 'BARAN', 'BARMER',
       'BHARATPUR', 'BHILWARA', 'BIKANER', 'BUNDI', 'CHITTORGARH',
       'CHURU', 'DAUSA', 'DHOLPUR', 'DUNGARPUR', 'GANGANAGAR',
       'HANUMANGARH', 'JAIPUR', 'JAISALMER', 'JALORE', 'JHALAWAR',
       'JHUNJHUNU', 'JODHPUR', 'KARAULI', 'KOTA', 'NAGAUR', 'PALI',
       'PRATAPGARH', 'RAJSAMAND', 'SAWAI MADHOPUR', 'SIKAR', 'SIROHI',
       'TONK', 'UDAIPUR', 'EAST DISTRICT', 'NORTH DISTRICT',
       'SOUTH DISTRICT', 'WEST DISTRICT', 'ARIYALUR', 'COIMBATORE',
       'CUDDALORE', 'DHARMAPURI', 'DINDIGUL', 'ERODE', 'KANCHIPURAM',
       'KANNIYAKUMARI', 'KARUR', 'KRISHNAGIRI', 'MADURAI', 'NAGAPATTINAM',
       'NAMAKKAL', 'PERAMBALUR', 'PUDUKKOTTAI', 'RAMANATHAPURAM', 'SALEM',
       'SIVAGANGA', 'THANJAVUR', 'THE NILGIRIS', 'THENI', 'THIRUVALLUR',
       'THIRUVARUR', 'TIRUCHIRAPPALLI', 'TIRUNELVELI', 'TIRUPPUR',
       'TIRUVANNAMALAI', 'TUTICORIN', 'VELLORE', 'VILLUPURAM',
       'VIRUDHUNAGAR', 'ADILABAD', 'HYDERABAD', 'KARIMNAGAR', 'KHAMMAM',
       'MAHBUBNAGAR', 'MEDAK', 'NALGONDA', 'NIZAMABAD', 'RANGAREDDI',
       'WARANGAL', 'DHALAI', 'GOMATI', 'KHOWAI', 'NORTH TRIPURA',
       'SEPAHIJALA', 'SOUTH TRIPURA', 'UNAKOTI', 'WEST TRIPURA', 'AGRA',
       'ALIGARH', 'ALLAHABAD', 'AMBEDKAR NAGAR', 'AMETHI', 'AMROHA',
       'AURAIYA', 'AZAMGARH', 'BAGHPAT', 'BAHRAICH', 'BALLIA', 'BANDA',
       'BARABANKI', 'BAREILLY', 'BASTI', 'BIJNOR', 'BUDAUN',
       'BULANDSHAHR', 'CHANDAULI', 'CHITRAKOOT', 'DEORIA', 'ETAH',
       'ETAWAH', 'FAIZABAD', 'FARRUKHABAD', 'FATEHPUR', 'FIROZABAD',
       'GAUTAM BUDDHA NAGAR', 'GHAZIABAD', 'GHAZIPUR', 'GONDA',
       'GORAKHPUR', 'HAPUR', 'HARDOI', 'HATHRAS', 'JALAUN', 'JAUNPUR',
       'JHANSI', 'KANNAUJ', 'KANPUR DEHAT', 'KANPUR NAGAR', 'KASGANJ',
       'KAUSHAMBI', 'KHERI', 'KUSHI NAGAR', 'LALITPUR', 'LUCKNOW',
       'MAHARAJGANJ', 'MAHOBA', 'MAINPURI', 'MATHURA', 'MAU', 'MEERUT',
       'MIRZAPUR', 'MORADABAD', 'MUZAFFARNAGAR', 'PILIBHIT', 'RAE BARELI',
       'RAMPUR', 'SAHARANPUR', 'SAMBHAL', 'SANT KABEER NAGAR',
       'SANT RAVIDAS NAGAR', 'SHAHJAHANPUR', 'SHAMLI', 'SHRAVASTI',
       'SIDDHARTH NAGAR', 'SITAPUR', 'SONBHADRA', 'SULTANPUR', 'UNNAO',
       'VARANASI', 'ALMORA', 'BAGESHWAR', 'CHAMOLI', 'CHAMPAWAT',
       'DEHRADUN', 'HARIDWAR', 'NAINITAL', 'PAURI GARHWAL', 'PITHORAGARH',
       'RUDRA PRAYAG', 'TEHRI GARHWAL', 'UDAM SINGH NAGAR', 'UTTAR KASHI',
       '24 PARAGANAS NORTH', '24 PARAGANAS SOUTH', 'BANKURA', 'BARDHAMAN',
       'BIRBHUM', 'COOCHBEHAR', 'DARJEELING', 'DINAJPUR DAKSHIN',
       'DINAJPUR UTTAR', 'HOOGHLY', 'HOWRAH', 'JALPAIGURI', 'MALDAH',
       'MEDINIPUR EAST', 'MEDINIPUR WEST', 'MURSHIDABAD', 'NADIA',
       'PURULIA']


__SESSIONS  = ['Kharif', 'Whole Year', 'Autumn', 'Rabi',
       'Summer', 'Winter']


__CROPS = ['Arecanut', 'Other Kharif pulses', 'Rice', 'Banana', 'Cashewnut',
       'Coconut ', 'Dry ginger', 'Sugarcane', 'Sweet potato', 'Tapioca',
       'Black pepper', 'Dry chillies', 'other oilseeds', 'Turmeric',
       'Maize', 'Moong(Green Gram)', 'Urad', 'Arhar/Tur', 'Groundnut',
       'Sunflower', 'Bajra', 'Castor seed', 'Cotton(lint)', 'Horse-gram',
       'Jowar', 'Korra', 'Ragi', 'Tobacco', 'Gram', 'Wheat', 'Masoor',
       'Sesamum', 'Linseed', 'Safflower', 'Onion', 'other misc. pulses',
       'Samai', 'Small millets', 'Coriander', 'Potato',
       'Other  Rabi pulses', 'Soyabean', 'Beans & Mutter(Vegetable)',
       'Bhindi', 'Brinjal', 'Citrus Fruit', 'Cucumber', 'Grapes', 'Mango',
       'Orange', 'other fibres', 'Other Fresh Fruits', 'Other Vegetables',
       'Papaya', 'Pome Fruit', 'Tomato', 'Mesta', 'Cowpea(Lobia)',
       'Lemon', 'Pome Granet', 'Sapota', 'Cabbage', 'Rapeseed &Mustard',
       'Peas  (vegetable)', 'Niger seed', 'Bottle Gourd', 'Varagu',
       'Garlic', 'Ginger', 'Oilseeds total', 'Pulses total', 'Jute',
       'Peas & beans (Pulses)', 'Blackgram', 'Paddy', 'Pineapple',
       'Barley', 'Sannhamp', 'Khesari', 'Guar seed', 'Moth',
       'Other Cereals & Millets', 'Cond-spcs other', 'Turnip', 'Carrot',
       'Redish', 'Arcanut (Processed)', 'Atcanut (Raw)',
       'Cashewnut Processed', 'Cashewnut Raw', 'Cardamom', 'Rubber',
       'Bitter Gourd', 'Drum Stick', 'Jack Fruit', 'Snak Guard', 'Tea',
       'Coffee', 'Cauliflower', 'Other Citrus Fruit', 'Water Melon',
       'Total foodgrain', 'Kapas', 'Colocosia', 'Lentil', 'Bean',
       'Jobster', 'Perilla', 'Rajmash Kholar', 'Ricebean (nagadal)',
       'Ash Gourd', 'Beet Root', 'Lab-Lab', 'Ribed Guard', 'Yam',
       'Pump Kin', 'Apple', 'Peach', 'Pear', 'Plums', 'Litchi', 'Ber',
       'Other Dry Fruit', 'Jute & mesta']



_crop_perdiction_crop_map  = {'rice': 0, 'maize': 1, 'chickpea': 2, 'kidneybeans': 3, 'pigeonpeas': 4, 'mothbeans': 5, 'mungbean': 6, 'blackgram': 7,
 'lentil': 8, 'pomegranate': 9, 'banana': 10, 'mango': 11, 'grapes': 12, 'watermelon': 13, 'muskmelon': 14,
 'apple': 15, 'orange': 16, 'papaya': 17, 'coconut': 18, 'cotton': 19, 'jute': 20, 'coffee': 21}



ferti_liser_crop_list = []

for crop in _crop_perdiction_crop_map:
    #print(crop)
    ferti_liser_crop_list.append(crop)


def get_crop_numerical_value(crop_name):
    return _crop_perdiction_crop_map.get(crop_name.lower(), -1)






app = Flask(__name__)
app.secret_key = '67tyrteytertwiruih67456bcagd'



    

def checkLogin(username, password):
    if username == "admin" and password == "admin":
        return True

    return False
    


     
    


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', login=True, active="home")
    return render_template('index.html', login=False, active="home")



@app.route('/preview')
def preview():
    if 'username' in session:
        data = None
        with open("templates/data.html", "r") as file:
            data = str(file.read())
        return render_template('preview.html', login=True, active="preview", data=data)

    return redirect("/", code=302)


@app.route('/upload', methods = ['POST','GET'])
def upload():
    if 'username' in session:
        if request.method == 'POST':
            f = request.files['file']
            fileName  = os.path.join(os.getcwd()+'\\uploads\\', ("data_set.csv"))
            print(fileName)
            f.save(fileName)
            df = pd.read_csv(fileName, nrows=1000)
            df.to_html('templates/data.html')
            return "<script>alert('File upload successful.'); window.open('/preview','_self')</script>"
        else:
            return render_template('upload.html', login=True, active="upload")

    return redirect("/", code=302)
        
    
 

@app.route('/login',methods = ['POST','GET'])
def login():
    print(request.method)
    if request.method  == "POST":
        username=request.form['username']  
        password=request.form['password'] 
        login =checkLogin(username, password)
        if not login :
            return  "<script>alert('username or password did not match.'); window.open('/','_self')</script>"
        else:
            session['username'] = username
            session['userphone'] = username
            return redirect("/", code=302)
    else:
        return render_template('login.html', active="login")
    



@app.route('/forcast',methods = ['POST','GET'])
def forcast():
    print(request.method)
    if 'username' in session:
        if request.method  == "POST":
            location=request.form['location']  
            finalurl = weather_url + geo_url +"q="+location+"&limit=5&appid="+weather_key
            print(finalurl)
            resp = requests.get(finalurl)
            print(resp)
            print(resp.text)
            data = json.loads(resp.text)
            if len(data) > 0:
                location = data[0]['name']
                country = data[0]['country']
                state = data[0]['state']
                lat = str(data[0]['lat'])
                lon = str(data[0]['lon'])
                print(data[0]['name'])
                print(data[0]['lat'])
                print(data[0]['lon'])
                print(data[0]['country'])
                print(data[0]['state'])
                
                finalurl = weather_url + weather_req +"lat="+lat+"&lon="+lon+"&appid="+weather_key
                print(finalurl)
                resp = requests.get(finalurl)
                print(resp)
                #print(resp.text)
                data = json.loads(resp.text)
                forcast = data['list']
                print(forcast)
            else:
                location = "Not found!"
        
            return render_template('forcast.html', login=True, active="forcast", location=location, country=country, state=state, forcast=forcast, round=round)
        else:
            return render_template('forcast.html', login=True, active="forcast", location="")
    
    return redirect("/", code=302)
   
      

        




        
        
@app.route('/file_upload', methods = ['GET', 'POST'])
def file_upload():
   if request.method == 'POST':
      f = request.files['file']
      fileName  = os.path.join(os.getcwd()+'\\uploads\\', ("data_set.csv"))
      print(fileName)
      f.save(fileName)
      return "<script>alert('File upload successful.'); window.open('/user_view?','_self')</script>"
      

@app.route('/logout',methods=['GET'])
def logout():
    session.pop('username', None)
    session.pop('userphone', None)
    return  "<script>alert('Logout complete.'); window.open('/','_self')</script>" 


@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html')
    












@app.route('/train',methods=['GET'])
def train():
    crop_df = pd.read_csv("uploads//data_set.csv")
    crop_df=crop_df.dropna().reset_index(drop=True)
    cols = crop_df.keys()
    states = crop_df["State_Name"].unique()
    districts = crop_df["District_Name"].unique()
    sessions = crop_df["Season"].unique()
    crops = crop_df["Crop"].unique()
    pre_crop_df = crop_df.copy(deep=True)
    pre_crop_df.head()


    index = 1
    for crop in crops:
        pre_crop_df.loc[pre_crop_df["Crop"] == crop, "Crop"] = index
        index+=1

    index = 1
    for session in sessions:
        pre_crop_df.loc[pre_crop_df["Season"] == session, "Season"] = index
        index+=1


    index = 1
    for district in districts:
        pre_crop_df.loc[pre_crop_df["District_Name"] == district, "District_Name"] = index
        index+=1

    index = 1
    for state in states:
        pre_crop_df.loc[pre_crop_df["State_Name"] == state, "State_Name"] = index
        index+=1

    
    #pre_crop_df['Production']

    pre_crop_df.to_csv (r'pren_crop_df.csv', index = False, header=True)
    X=pre_crop_df[ ['State_Name', 'District_Name', 'Crop_Year', 'Season', 'Crop', 'Area']]
    y=pre_crop_df['Production']



    #convert y values to categorical values
    lab = preprocessing.LabelEncoder()
    y_transformed = lab.fit_transform(y)

    #view transformed values
    y = y_transformed

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=22)    

    model=KNeighborsClassifier()

    model.fit(X_train,y_train)

    pickle.dump(model, open("trained-model.pickle", "wb"))

    y_predict=model.predict(X_test)


    ###################
    ###################
    ###################
    #tranin crop model
    X=pre_crop_df[ ['State_Name', 'District_Name', 'Crop_Year', 'Season', 'Area']]
    y=pre_crop_df['Crop']

    lab = preprocessing.LabelEncoder()
    y_transformed = lab.fit_transform(y)

    y = y_transformed

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=22)


    model.fit(X_train,y_train)

    pickle.dump(model, open("trained-model-crop.pickle", "wb"))


    return "Trainign Done"






def getStateCode(state_get):
    index = 1
    for state in __STATES:
        if state.strip() == state_get.strip():
            return index
    return -1


def getDistrictCode(district_get):
    index = 1
    for district in __DISTRICTS:
        if district.strip() == district_get.strip():
            return index
    return -1



def getSessionCode(session_get):
    index = 1
    for session in __SESSIONS:
        if session.strip() == session_get.strip():
            return index
    return -1


def getCropCode(crop_get):
    index = 1
    for crop in __CROPS:
        if crop.strip() == crop_get.strip():
            return index
    return -1



def cropFromCode(crop_code):
    index = 1
    for crop in __CROPS:
        if crop_code == index:
            return crop
        
        index+=1
        
    return "error!"








@app.route('/predictproduction',methods = ['POST','GET'])
def predictproduction():
    print(request.method)
    if 'username' in session:
        if request.method  == "POST":
            state=request.form['state']
            district=request.form['district']
            session_crop=request.form['session']
            crop=request.form['crop']
            year = request.form['year']
            area=request.form['area']

            state_code = getStateCode(state)
            district_code = getDistrictCode(district)
            crop_year = int(year)
            season_code = getSessionCode(session_crop)
            crop_code = getCropCode(crop)
            crop_area = int(area)

            model = pickle.load(open("trained-model.pickle", "rb"))

            result=model.predict([[state_code, district_code, crop_year,season_code, crop_code,crop_area]])
            print('Production: ',result[0],'\n\n\n\n\n\n\n')

            return render_template('predictproduction.html',login=True, active="predictproduction", states=__STATES,
                                                                     districts=__DISTRICTS, sessions=__SESSIONS,
                                                                     crops=__CROPS, production=result[0], selstate=state,
                                                                     seldistrict=district,selsession=session,selcrop=crop,year=year,area=area ) 




    return render_template('predictproduction.html',login=True, active="predictproduction", states=__STATES,
                                                                     districts=__DISTRICTS, sessions=__SESSIONS,
                                                                     crops=__CROPS) 




@app.route('/cropproduction',methods = ['POST','GET'])
def cropproduction():
    print(request.method)
    if 'username' in session:
        if request.method  == "POST":
            state=request.form['state']
            district=request.form['district']
            session_crop=request.form['session']
            year = request.form['year']
            area=request.form['area']

            state_code = getStateCode(state)
            district_code = getDistrictCode(district)
            crop_year = int(year)
            season_code = getSessionCode(session_crop)
            crop_area = int(area)

            model = pickle.load(open("trained-model-crop.pickle", "rb"))

            result=model.predict([[state_code, district_code, crop_year,season_code,crop_area]])
            crop_name = cropFromCode(result[0])
            print('crop_code: ',crop_name)

            return render_template('predictcrop.html',login=True, active="predictproduction", states=__STATES,
                                                                     districts=__DISTRICTS, sessions=__SESSIONS,
                                                                     crop_name=crop_name, selstate=state,
                                                                     seldistrict=district,selsession=session,year=year,area=area) 




    return render_template('predictcrop.html',login=True, active="predictproduction", states=__STATES,
                                                                     districts=__DISTRICTS, sessions=__SESSIONS) 


     
     



@app.route('/predict_fertilizer',methods = ['POST','GET'])
def predict_fertilizer():
    print(request.method)
    if 'username' in session:
        if request.method  == "POST":
            #temperature, humidity, ph, rainfall, label
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])
            crop = request.form['crop']

            label= get_crop_numerical_value(crop)

            n_model = pickle.load(open("trained-model-n.pickle", "rb"))
            p_model = pickle.load(open("trained-model-p.pickle", "rb"))
            k_model = pickle.load(open("trained-model-k.pickle", "rb"))

            n_result = n_model.predict([[temperature, humidity, ph, rainfall, label]])[0]
            p_result = p_model.predict([[temperature, humidity, ph, rainfall, label]])[0]
            k_result = k_model.predict([[temperature, humidity, ph, rainfall, label]])[0]


           

            return render_template('predictferti.html',login=True, active="predictferti", selcrop=crop, temperature=temperature, humidity=humidity, 
                                    ph=ph, rainfall=rainfall,  ferti_liser_crop_list = ferti_liser_crop_list, n_result=n_result, p_result=p_result, k_result=k_result, show_result=True) 




    return render_template('predictferti.html',login=True, active="predictferti", ferti_liser_crop_list = ferti_liser_crop_list , show_result=False) 

    
    




  

        





    
    
   
if __name__ == '__main__':  
   app.run(debug = True)  
   