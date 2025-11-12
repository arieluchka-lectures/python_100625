
from flask import Flask, jsonify, request, render_template_string
from datetime import datetime

app = Flask(__name__)

# In-memory data store
posts = []
next_id = 1


# Homepage with API documentation
HOME_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Blog API</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1000px;
            margin: 40px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        h1 {
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }
        h2 {
            color: #764ba2;
            margin-top: 30px;
        }
        .endpoint {
            background: #f8f9fa;
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid #667eea;
            border-radius: 5px;
        }
        .method {
            display: inline-block;
            padding: 3px 10px;
            border-radius: 3px;
            font-weight: bold;
            margin-right: 10px;
            color: white;
        }
        .get { background-color: #28a745; }
        .post { background-color: #007bff; }
        .put { background-color: #ffc107; color: #333; }
        .delete { background-color: #dc3545; }
        code {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 15px;
            display: block;
            border-radius: 5px;
            overflow-x: auto;
            margin: 10px 0;
        }
        .test-button {
            background: #667eea;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin: 5px;
        }
        .test-button:hover {
            background: #764ba2;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📝 Blog API Documentation</h1>
        <p>A RESTful API for managing blog posts. Use tools like curl, Postman, or your browser to test these endpoints.</p>

        <h2>Available Endpoints</h2>

        <div class="endpoint">
            <span class="method get">GET</span>
            <strong>/api/posts</strong>
            <p>Get all blog posts</p>
            <button class="test-button" onclick="testGetAll()">Test</button>
            <div id="result-all" style="margin-top: 10px;"></div>
        </div>

        <div class="endpoint">
            <span class="method get">GET</span>
            <strong>/api/posts/&lt;id&gt;</strong>
            <p>Get a single blog post by ID</p>
            <button class="test-button" onclick="testGetOne()">Test (ID: 1)</button>
            <div id="result-one" style="margin-top: 10px;"></div>
        </div>

        <div class="endpoint">
            <span class="method post">POST</span>
            <strong>/api/posts</strong>
            <p>Create a new blog post</p>
            <p><strong>Request Body:</strong></p>
            <code>{
    "title": "Post Title",
    "content": "Post content goes here",
    "author": "Author Name"
}</code>
        </div>

        <div class="endpoint">
            <span class="method put">PUT</span>
            <strong>/api/posts/&lt;id&gt;</strong>
            <p>Update an existing blog post</p>
            <p><strong>Request Body:</strong></p>
            <code>{
    "title": "Updated Title",
    "content": "Updated content",
    "author": "Updated Author"
}</code>
        </div>

        <div class="endpoint">
            <span class="method delete">DELETE</span>
            <strong>/api/posts/&lt;id&gt;</strong>
            <p>Delete a blog post by ID</p>
        </div>

        <h2>Example Usage with curl</h2>
        <code># Get all posts
curl http://localhost:5002/api/posts

# Get single post
curl http://localhost:5002/api/posts/1

# Create new post
curl -X POST http://localhost:5002/api/posts \
  -H "Content-Type: application/json" \
  -d '{"title":"My Post","content":"Hello World","author":"John"}'

# Update post
curl -X PUT http://localhost:5002/api/posts/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated Title","content":"New content","author":"Jane"}'

# Delete post
curl -X DELETE http://localhost:5002/api/posts/1</code>

        <h2>Current Stats</h2>
        <p>Total Posts: <strong>{{ total_posts }}</strong></p>
    </div>

    <script>
        function testGetAll() {
            fetch('/api/posts')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('result-all').innerHTML = 
                        '<code>' + JSON.stringify(data, null, 2) + '</code>';
                });
        }

        function testGetOne() {
            fetch('/api/posts/1')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('result-one').innerHTML = 
                        '<code>' + JSON.stringify(data, null, 2) + '</code>';
                });
        }
    </script>
</body>
</html>
'''


@app.route('/')
def home():
    '''API documentation homepage'''
    return render_template_string(HOME_TEMPLATE, total_posts=len(posts))


@app.route('/api/posts', methods=['GET'])
def get_posts():
    '''Get all blog posts'''
    return jsonify({
        'success': True,
        'count': len(posts),
        'data': posts
    }), 200


@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    '''Get a single blog post by ID'''
    post = next((p for p in posts if p['id'] == post_id), None)

    if post:
        return jsonify({
            'success': True,
            'data': post
        }), 200
    else:
        return jsonify({
            'success': False,
            'error': 'Post not found'
        }), 404


@app.route('/api/posts', methods=['POST'])
def create_post():
    '''Create a new blog post'''
    global next_id

    # Validate request has JSON data
    if not request.is_json:
        return jsonify({
            'success': False,
            'error': 'Content-Type must be application/json'
        }), 400

    data = request.get_json()

    # Validate required fields
    required_fields = ['title', 'content', 'author']
    for field in required_fields:
        if field not in data or not data[field].strip():
            return jsonify({
                'success': False,
                'error': f'Missing or empty required field: {field}'
            }), 400

    # Create new post
    new_post = {
        'id': next_id,
        'title': data['title'].strip(),
        'content': data['content'].strip(),
        'author': data['author'].strip(),
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }

    posts.append(new_post)
    next_id += 1

    return jsonify({
        'success': True,
        'message': 'Post created successfully',
        'data': new_post
    }), 201


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    '''Update an existing blog post'''
    post = next((p for p in posts if p['id'] == post_id), None)

    if not post:
        return jsonify({
            'success': False,
            'error': 'Post not found'
        }), 404

    if not request.is_json:
        return jsonify({
            'success': False,
            'error': 'Content-Type must be application/json'
        }), 400

    data = request.get_json()

    # Update fields if provided
    if 'title' in data and data['title'].strip():
        post['title'] = data['title'].strip()
    if 'content' in data and data['content'].strip():
        post['content'] = data['content'].strip()
    if 'author' in data and data['author'].strip():
        post['author'] = data['author'].strip()

    post['updated_at'] = datetime.now().isoformat()

    return jsonify({
        'success': True,
        'message': 'Post updated successfully',
        'data': post
    }), 200


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    '''Delete a blog post'''
    global posts

    post = next((p for p in posts if p['id'] == post_id), None)

    if not post:
        return jsonify({
            'success': False,
            'error': 'Post not found'
        }), 404

    posts = [p for p in posts if p['id'] != post_id]

    return jsonify({
        'success': True,
        'message': 'Post deleted successfully'
    }), 200


@app.errorhandler(404)
def not_found(error):
    '''Handle 404 errors'''
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    '''Handle 500 errors'''
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500


if __name__ == '__main__':
    # Add sample blog posts
    posts = [
        {
            'id': 1,
            'title': 'Getting Started with Flask',
            'content': 'Flask is a lightweight Python web framework that makes it easy to build web applications. In this post, we will explore the basics of Flask and how to create your first web application.',
            'author': 'John Doe',
            'created_at': '2025-11-10T10:00:00',
            'updated_at': '2025-11-10T10:00:00'
        },
        {
            'id': 2,
            'title': 'Building RESTful APIs with Flask',
            'content': 'RESTful APIs are a crucial part of modern web development. This post demonstrates how to build a complete REST API using Flask, including all CRUD operations.',
            'author': 'Jane Smith',
            'created_at': '2025-11-11T09:30:00',
            'updated_at': '2025-11-11T09:30:00'
        },
        {
            'id': 3,
            'title': 'Flask Best Practices',
            'content': 'Learn about best practices when developing Flask applications, including project structure, error handling, and security considerations.',
            'author': 'Bob Johnson',
            'created_at': '2025-11-11T14:00:00',
            'updated_at': '2025-11-11T14:00:00'
        }
    ]
    next_id = 4

    print("\n🚀 Blog API Server Starting...")
    print("📖 Visit http://localhost:5002/ for API documentation")
    print("🔧 API endpoints available at http://localhost:5002/api/posts\n")

    app.run(debug=True, host='0.0.0.0', port=5002)