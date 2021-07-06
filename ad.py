import redis
from flask import Flask, render_template, make_response, url_for, request
from time import strftime
app = Flask(__name__)
r =  redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')

def cooockies():

    res = make_response(f"<h1>Вы уже были на сайте</h1>logged")
    res.set_cookie("logged", "yes")
    ret = request.cookies.get('logged')
    day=strftime("%Y-%m-%d")
    
    if ret:
        numb = str(r.get('page:index:counter:' + day))
        return f'Привет, ты уже был, твой номер на {day} = {numb}'
        
    else:
        day=strftime("%Y-%m-%d")
        r.incr('page:index:counter:' + day)
        return '42 - ' + str(r.get('page:index:counter:' + day))

    
    


