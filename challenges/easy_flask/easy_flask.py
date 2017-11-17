from flask import Flask,request,url_for,redirect,render_template,session
import hashlib,os,sys

# flag is in sandbox/4107/flag

app = Flask(__name__)
app.secret_key = "thisisfuckingsecretkey"
def getMd5(data):
    return hashlib.md5(data).hexdigest()

@app.route('/')
def index():
    userId = None
    if 'userId' in session:
        userId = session['userId']
    return render_template("index.html",userId=userId,fileList=os.listdir('.'))

@app.route('/login',methods = ['GET','POST'])
def login():
    error = "Login Page"
    if request.method == "POST" and 'userId' not in session:
        userId = request.form['userId']
        password = request.form['password']
        dirName = getMd5(userId + password)
        try:
            os.chdir(dirName)
            error = userId
            session['userId'] = userId
        except:
            error = "Login Failed"
    return render_template("login.html",error=error)

@app.route('/join',methods = ['GET','POST'])
def join():
    error = "Join Page"
    fileDict = \
            {'apple':'[NOUN] An apple is a round fruit with smooth green, yellow, or red skin and firm white flesh.',
            'banana':'[NOUN] Bananas are long curved fruit with yellow skins.',
            'carrot':'[NOUN] Carrots are long, thin, orange-coloured vegetables. They grow under the ground, and have green shoots above the ground.',
            'durian':'[NOUN] a SE Asian bombacaceous tree, Durio zibethinus, having very large oval fruits with a hard spiny rind containing seeds surrounded by edible evil-smelling aril',
            'eggplant':'[NOUN] An eggplant is a vegetable with a smooth, dark purple skin. in BRIT, use aubergine'}
    if request.method == 'POST' and 'userId' not in session:
        userId = request.form['userId']
        password = request.form['password']
        dirName = getMd5(userId + password)
        try:
            os.mkdir(dirName,0755)
            os.chdir(dirName)
            for key, value in fileDict.iteritems():
                with open(key,"wb") as f:
                    f.write(value)
                f.close()
            os.chdir("..")
            error = "Join Success"
        except:
            error = "Cannot join"

    return render_template("join.html",error=error)

@app.route('/logout')
def logout():
    if 'userId' in session:
        session.pop('userId',None)
        os.chdir("..")

    return redirect(url_for('index'))

@app.route('/read',methods=['GET'])
def read():
    rdata = "None"
    if 'file' in request.args:
        fileName = request.args['file']
        filePath = "./" + fileName
        try:
            with open(filePath,"rb") as f:
                rdata = f.read()
            f.close()
        except:
            rdata = "Read Error"
    return rdata


if __name__ == '__main__':
    try:
        #os.mkdir("sandbox",0755)
        os.chdir("sandbox")
    except:
        print "Holy shit, It's time to tell this shit to admin"
        sys.exit(-1)
    app.run("0.0.0.0",5555)
