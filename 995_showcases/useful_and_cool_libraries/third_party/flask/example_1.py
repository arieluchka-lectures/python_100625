
from flask import Flask, render_template_string, request, jsonify, url_for, redirect

# Create Flask application instance
app = Flask(__name__)

# Set a secret key for session management
app.config['SECRET_KEY'] = 'your-secret-key-here'


# 1. BASIC ROUTING - Simple homepage
@app.route('/')
def home():
    return '''
    <h1>Welcome to Flask!</h1>
    <p>Check out these examples:</p>
    <ul>
        <li><a href="/hello">Simple Hello</a></li>
        <li><a href="/hello/John">Hello with Name</a></li>
        <li><a href="/api/data">JSON API Example</a></li>
        <li><a href="/form">Form Example</a></li>
        <li><a href="/about">About Page</a></li>
    </ul>
    '''


# 2. ROUTE WITH URL PARAMETERS
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        return f'<h1>Hello, {name}!</h1><a href="/">Back to Home</a>'
    return '<h1>Hello, Guest!</h1><a href="/">Back to Home</a>'


# 3. MULTIPLE URL PARAMETERS WITH TYPE CONVERSION
@app.route('/user/<string:username>/posts/<int:post_id>')
def user_post(username, post_id):
    return f'''
    <h2>User: {username}</h2>
    <p>Viewing post #{post_id}</p>
    <a href="/">Back to Home</a>
    '''


# 4. JSON API ENDPOINT
@app.route('/api/data')
def get_data():
    data = {
        'status': 'success',
        'message': 'This is a JSON response',
        'items': ['item1', 'item2', 'item3'],
        'count': 3
    }
    return jsonify(data)


# 5. HANDLING GET AND POST METHODS
@app.route('/form', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        username = request.form.get('username', '')
        email = request.form.get('email', '')
        return f'''
        <h2>Form Submitted!</h2>
        <p>Username: {username}</p>
        <p>Email: {email}</p>
        <a href="/form">Back to Form</a>
        '''

    return '''
    <h2>Submit a Form</h2>
    <form method="POST">
        <label>Username: <input type="text" name="username" required></label><br><br>
        <label>Email: <input type="email" name="email" required></label><br><br>
        <button type="submit">Submit</button>
    </form>
    <br><a href="/">Back to Home</a>
    '''


# 6. TEMPLATE RENDERING WITH VARIABLES
@app.route('/about')
def about():
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>{{ heading }}</h1>
        <p>{{ description }}</p>
        <h3>Features:</h3>
        <ul>
        {% for feature in features %}
            <li>{{ feature }}</li>
        {% endfor %}
        </ul>
        <a href="/">Back to Home</a>
    </body>
    </html>
    '''
    return render_template_string(
        template,
        title='About Flask',
        heading='About This Application',
        description='Flask is a lightweight Python web framework.',
        features=['Routing', 'Templates', 'Forms', 'APIs', 'Extensions']
    )


# 7. URL BUILDING AND REDIRECTS
@app.route('/redirect-example')
def redirect_example():
    return redirect(url_for('home'))


# 8. CUSTOM ERROR HANDLERS
@app.errorhandler(404)
def page_not_found(error):
    return '''
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="/">Go to Home</a>
    ''', 404


@app.errorhandler(500)
def internal_error(error):
    return '''
    <h1>500 - Internal Server Error</h1>
    <p>Something went wrong on our end.</p>
    <a href="/">Go to Home</a>
    ''', 500


# 9. QUERY PARAMETERS
@app.route('/search')
def search():
    query = request.args.get('q', 'nothing')
    page = request.args.get('page', 1, type=int)
    return f'''
    <h2>Search Results</h2>
    <p>You searched for: <strong>{query}</strong></p>
    <p>Page: {page}</p>
    <p>Try: <a href="/search?q=flask&page=2">/search?q=flask&page=2</a></p>
    <a href="/">Back to Home</a>
    '''


if __name__ == '__main__':
    # Run the Flask development server
    # debug=True enables auto-reload and detailed error messages
    app.run(debug=True, host='0.0.0.0', port=5000)