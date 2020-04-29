from flask import Flask, request, render_template

app = Flask( __name__ )
app.config['DEBUG'] = True

@app.route( '/' )
def home():
    return render_template( "index.html" )

@app.route( '/about' )
def aboutMe():
    return render_template( "about.html" )

@app.route( '/greet/<username>/<job>' )
def greeting( username, job ):
    return "<h1> Hello " + username + ", you are a " + job + " </h1>"

@app.route( '/add' )
def addition():
    a = int( request.args.get( 'first_num' ) )
    b = int( request.args.get( 'second_num' ) )
    result = a + b
    return render_template( "addition.html", theResult = result )


app.run()