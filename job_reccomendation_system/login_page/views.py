from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import pyrebase
 
 
# For Firebase JS SDK v7.20.0 and later, measurementId is optional
config = {
  "apiKey": "AIzaSyCymQui1BmSZlUQcbz5EJzMzFVZB0CtUtk",
  "authDomain": "job-recommender-d701e.firebaseapp.com",
  "projectId": "job-recommender-d701e",
  "storageBucket": "job-recommender-d701e.appspot.com",
  "messagingSenderId": "836570295145",
  "appId": "1:836570295145:web:2595205b74a38dd405ebf8",
  "measurementId": "G-7JC5V4D8YD",
  "databaseURL": "https://job-recommender-d701e-default-rtdb.firebaseio.com",
}
# Initialising database,auth and firebase for further use
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
 
def signIn(request):
    return render(request,"index.html")
def home(request):
    return render(request,"Home.html")   
 
def postsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
        
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"Login.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"Home.html",{"email":email})
 
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"index.html")
 
def postsignUp(request):
     email = request.POST.get('email')
     passs = request.POST.get('pass')
     name = request.POST.get('name')
     try:
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
     except:
        return render(request, "index.html")
     return render(request,"index.html")

def reset(request):
    return render(request, "Reset.html")
 
def postReset(request):
    email = request.POST.get('email')
    try:
        authe.send_password_reset_email(email)
        message  = "A email to reset password is successfully sent"
        return render(request, "Reset.html", {"msg":message})
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        return render(request, "Reset.html", {"msg":message})
