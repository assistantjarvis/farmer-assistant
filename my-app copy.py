from flask import *  
import sqlite3
import pandas as pd
import os
import time
import requests 
from bs4 import BeautifulSoup 
from fuzzywuzzy import fuzz 
#from fuzzywuzzy import process 
import html2text
import array
#from operator import itemgetter, attrgetter





app = Flask(__name__)
app.secret_key = '67tyrteytertwiruih67456bcagd'
DATABASE = 'userdatabase.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def insert_user(name, phone, password, gender):
    con = get_db()
    status = False
    try:
        cur = con.cursor()  
        cur.execute("INSERT INTO users(name,phone,pass,gender)VALUES(?,?,?,?)",(name, phone, password,gender))  
        con.commit()
        status = True
    except:  
        con.rollback()
        status = False
    finally:  
        return status
        
        

         
    

def checkLogin(phone, password):
    conn = get_db()
    user = query_db('select * from users where phone = ? AND pass = ?',
                (phone,password), one=True)
    return user
    



def loginAdmin(phone, password):
    conn = get_db()
    admin = query_db('select * from administrator where phone = ? AND pass = ?',
                (phone,password), one=True)
    return admin
    
def updatePassword(userphone,password):
    status = False
    try:
        conn = get_db()
        sql = "UPDATE administrator SET pass = ?  WHERE phone = ?"
        cur = conn.cursor()
        cur.execute(sql, (password,userphone))
        conn.commit()
        status = True
    except:  
        con.rollback()
        status = False
    finally:  
        return status
    
    
def keywordExists(word):
    conn = get_db()

    exist = query_db('select * from keywords where keyword = ? ',
                (word,), one=True)
    return exist
    
def insert_keyword(keyword):
    con = get_db()
    status = False
    try:
        cur = con.cursor()  
        cur.execute("INSERT INTO keywords(keyword)VALUES(?)",(keyword,))  
        con.commit()
        status = True
    except:  
        con.rollback()
        status = False
    finally:  
        return status
        
def delete_keyword(index_no):
    conn = get_db()
    sql = 'DELETE FROM keywords WHERE id_no=?'
    cur = conn.cursor()
    cur.execute(sql, (index_no,))
    conn.commit()



         

def getAllKeyWords():
    conn = get_db()
    data = query_db('select * from keywords')
    keyWords = [KeyWord] * len(data)
    index = 0;
    for mKeyword in data:
        keyword = KeyWord(mKeyword[0], mKeyword[1])
        keyWords[index] = keyword;
        index += 1
    return keyWords    
    


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/register')
def register():
    return render_template('register.html') 
    
@app.route('/registeruser',methods = ['POST'])
def registeruser():
    name=request.form['name']    
    phone=request.form['phone']  
    password=request.form['pass'] 
    gender=request.form['gender']
    result = insert_user(name,phone,password,gender)
    if result == True:
        return  "<script>alert('user registration successfull.'); window.open('/home','_self')</script>"
    else:
        return  "<script>alert('user registration Fail.'); window.open('/register','_self')</script>"







@app.route('/admin_login',methods = ['POST'])
def admin_login():
    phone=request.form['phone']  
    password=request.form['pass'] 
    user=loginAdmin(phone, password)
    if user is None:
       return  "<script>alert('Phone or password did not match.'); window.open('/','_self')</script>"
    else:
        session['username'] = 'admin'
        session['userphone'] = phone
        return redirect("/admin_account", code=302)
      
        
        
        
@app.route('/admin_account',methods = ['POST','GET'])
def admin_account():
     if 'username' in session:
        if 'admin' == session['username']:
              if request.args.get('opt') == None or request.args.get('opt') == 'add_keyword' or request.args.get('opt') == 'Add Keyword':
                if request.args.get('keyword') == None:
                    return render_template('admin-account.html',active = "Add keyword")
                else:
                    word = request.args.get('keyword')
                    
                    if keywordExists(word):
                        return  "<script>alert('Keyword: "+word+" already exists.'); window.open('/admin_account?opt=add_keyword','_self')</script>"
                    
                    result = insert_keyword(word)
                    if result == True:
                        return  "<script>alert('Keyword added successful.'); window.open('/admin_account?opt=add_keyword','_self')</script>"
                    else:
                        return  "<script>alert('Fail to add Keyword.'); window.open('/admin_account?opt=add_keyword','_self')</script>"
                    
              elif request.args.get('opt') == 'upload_file':
                return render_template('admin-account.html',active = "Check Website")
              elif request.args.get('opt') == 'check_all_websites':
                #return render_template('admin-account.html',active = "Check All Websites")
                #return redirect("/check_all_websites", code=302)
                return check_all_websites()
              elif request.args.get('opt') == 'update_password':
                return render_template('admin-account.html',active = "Update Password")
              elif request.args.get('opt') == 'view_keywords':
                if request.args.get('del_id') == None:
                    return render_template('admin-account.html',active = "View Keywords", allKeywords = getAllKeyWords())
                else:
                    
                    index_no = request.args.get('del_id')
                    print(index_no)
                    delete_keyword(str(index_no))
                    return render_template('admin-account.html',active = "View Keywords", allKeywords = getAllKeyWords())
                        
                        
                   
              
              
     return  "<script>alert('Please login!'); window.open('/','_self')</script>"
     


        
@app.route('/update_password',methods = ['POST','GET'])
def update_password():
     if 'username' in session:
        if 'admin' == session['username']:
              oldpassword = request.form['oldpassword']
              newPass1    = request.form['newpassword1']
              newPass2    = request.form['newpassword2']
              
              phone = session['userphone']
              
              user=loginAdmin(phone, oldpassword)
              
              if not newPass1 == newPass2:
                return  "<script>alert('new passwords are not same!'); window.open('/admin_account?opt=update_password','_self')</script>"
              
              elif user is None:
                return  "<script>alert('Old password did not match!'); window.open('/admin_account?opt=update_password','_self')</script>"
              
              res = updatePassword(phone,newPass1)
              
              if res :
                return  "<script>alert('Password update done!'); window.open('/admin_account?opt=add_keyword','_self')</script>"
              
              else:
                return  "<script>alert('Fail to update password!'); window.open('/admin_account?opt=update_password','_self')</script>"
              
              return render_template('admin-account.html',active = "Update Password")
                        
                        
                   
              
              
     return  "<script>alert('Please login!'); window.open('/','_self')</script>"
     
     
     
     
def check_all_websites():
    fileName  = getFileName()
    file1 = open(fileName, 'r')
    Lines = file1.readlines()
    
    strWrds = []
    for keyword in getAllKeyWords():
        strWrds.append(keyword.word)
    
    #print(strWrds)
    
    resultsFromUrl = dict()
    for urldata in Lines:
        linestr = urldata.strip()
        print("-"*10)
        print(linestr)
        resultSet = getPage(linestr,strWrds)
        resultsFromUrl[linestr] = resultSet
        print(resultSet.printString())
        print("-"*10)

    

    
    resultsWithTotal = dict()
    for res in resultsFromUrl:
        #print(res)
        if resultsFromUrl[res] != None:
            #print("="*50)
            #print(resultsFromUrl[res].printString())
            rwm = ResultWithSum(resultsFromUrl[res],res,resultsFromUrl[res].getTotal())
            resultsWithTotal[resultsFromUrl[res].getTotal()] = rwm
            #print("="*50)
           

    bestMatch = True
    for key in sorted(resultsWithTotal.keys(), reverse=True) :
        #print(key , " :: " , resultsWithTotal[key])
        print("**"*50)
        if bestMatch:
            print("-+^Best Match^+-")
            bestMatch = False
        print("URL>\n" + resultsWithTotal[key].url)
        print("Total: " + str(resultsWithTotal[key].total))
        print("ResultSet>")
        resultsWithTotal[key].resultSet.printString()
        print("**"*50)
    
    #return sorted(resultsWithTotal.keys(), reverse=True)
    sorted_keysT = sorted(resultsWithTotal.keys(), reverse=True)
    return render_template('admin-account.html',active = "Check All Websites",resultSets = resultsWithTotal, sorted_keys = sorted_keysT, allKeywords = getAllKeyWords())   
        

def getFileName():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    timestr ="asset"
    path = os.path.join(os.getcwd()+'\\uploads\\', (timestr+".txt"))
    return path
        
        
        
@app.route('/file_upload', methods = ['GET', 'POST'])
def file_upload():
   if request.method == 'POST':
      f = request.files['file']
      fileName  = getFileName()
      print(fileName)
      f.save(fileName)
      return "<script>alert('File upload successful.'); window.open('/admin_account?opt=upload_file','_self')</script>"
      

@app.route('/logout',methods=['GET'])
def logout():
    session.pop('username', None)
    session.pop('userphone', None)
    return  "<script>alert('Logout complete.'); window.open('/','_self')</script>" 


@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html')
    






class ResultSet:
  def __init__(self, Ratio, Partial_Ratio, Token_Sort_Ratio, Token_Set_Ratio):
    self.Ratio = Ratio
    self.Partial_Ratio = Partial_Ratio    
    self.Token_Sort_Ratio = Token_Sort_Ratio
    self.Token_Set_Ratio = Token_Set_Ratio
    
    
  
  def getTotal(self):
    return self.Partial_Ratio + self.Token_Set_Ratio
    
    
    
  def printString(self):
    print("Ratio: ",self.Ratio)
    print("Partial_Ratio: ",self.Partial_Ratio)
    print("Token_Sort_Ratio: ",self.Token_Sort_Ratio)
    print("Token_Set_Ratio: ",self.Token_Set_Ratio)
    #print("Sum: ", self.Partial_Ratio + self.Token_Set_Ratio)
    
    
 
 
class ResultWithSum:
    def __init__(self, resultSet, url, total):
        self.resultSet = resultSet
        self.url = url
        self.total = total
    
    
    
    
    
    


  
def getPage(url,query): 
    # the target we want to open     
    #url='http://www.hindustantimes.com/top-news'
      
    #open with GET method 
    resp=requests.get(url) 
      
    #http_respone 200 means OK status 
    if resp.status_code==200: 
        print("Successfully opened the web page") 
        #print("The news are as follow :-\n") 
        #print("*"*40);
        #print(resp.text);
        #print("*"*40);
        h = html2text.HTML2Text()
        # Ignore converting links from HTML
        h.ignore_links = True
        
        pageText  = h.handle(resp.text)
        #print(pageText)
        
        Ratio = fuzz.ratio(pageText,query)
        Partial_Ratio  = fuzz.partial_ratio(pageText,query)
        Token_Sort_Ratio = fuzz.token_sort_ratio(pageText,query)
        Token_Set_Ratio = fuzz.token_set_ratio(pageText,query)
               
        resultSet = ResultSet(Ratio, Partial_Ratio, Token_Sort_Ratio, Token_Set_Ratio)
        
        return resultSet
        #return None
    else: 
        print("Error") 
        return None
  
  

        








    

class KeyWord:
    def __init__(self, index, word):
        self.index  = index
        self.word  = word
       
    
    
   
if __name__ == '__main__':  
   app.run(debug = True)  
   