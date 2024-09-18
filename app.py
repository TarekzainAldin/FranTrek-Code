from flask import Flask, render_template, url_for

app = Flask(__name__)

lessons=[{
    
        'title':'request Libray course',
        'course':'python',
        'authour':'tarek'
   
},
{
    
        'title':'request html course',
        'course':'Html',
        'authour':'francia'
   
},

{
    
        'title':'request datatime course',
        'course':'python',
        'authour':'francia  '
   
},
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', lessons=lessons)
@app.route('/about')
def about():
    return render_template('about.html', title = "About")
if __name__ == '__main__':
    app.run(debug=True)
    