from flask import Flask, render_template_string, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey123'

# In-memory data store (use database in production)
todos = []
next_id = 1


# HTML Template for the todo list
TODO_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Todo List App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
        }
        .todo-form {
            background: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .todo-item {
            background: white;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .todo-item.completed {
            opacity: 0.6;
            text-decoration: line-through;
        }
        .btn {
            padding: 8px 15px;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            margin: 0 5px;
        }
        .btn-primary {
            background-color: #007bff;
            color: white;
        }
        .btn-success {
            background-color: #28a745;
            color: white;
        }
        .btn-danger {
            background-color: #dc3545;
            color: white;
        }
        .btn-warning {
            background-color: #ffc107;
            color: black;
        }
        input[type="text"] {
            width: 70%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 3px;
        }
        .flash-messages {
            padding: 10px;
            margin-bottom: 20px;
            border-radius: 3px;
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        .priority {
            font-size: 12px;
            padding: 3px 8px;
            border-radius: 3px;
            margin-left: 10px;
        }
        .priority-high { background-color: #ffcccc; }
        .priority-medium { background-color: #fff4cc; }
        .priority-low { background-color: #ccffcc; }
    </style>
</head>
<body>
    <h1>📝 My Todo List</h1>

    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <div class="flash-messages">
                {% for message in messages %}
                    <p>{{ message }}</p>
                {% endfor %}
            </div>
        {% endif %}
    {% endwith %}

    <div class="todo-form">
        <h2>Add New Todo</h2>
        <form method="POST" action="{{ url_for('add_todo') }}">
            <input type="text" name="task" placeholder="Enter your task..." required>
            <select name="priority">
                <option value="low">Low Priority</option>
                <option value="medium" selected>Medium Priority</option>
                <option value="high">High Priority</option>
            </select>
            <button type="submit" class="btn btn-primary">Add Todo</button>
        </form>
    </div>

    <h2>Tasks ({{ todos|length }})</h2>

    {% if todos %}
        {% for todo in todos %}
        <div class="todo-item {% if todo.completed %}completed{% endif %}">
            <div>
                <strong>{{ todo.task }}</strong>
                <span class="priority priority-{{ todo.priority }}">{{ todo.priority|upper }}</span>
                <br>
                <small>Created: {{ todo.created_at }}</small>
            </div>
            <div>
                {% if not todo.completed %}
                    <a href="{{ url_for('complete_todo', todo_id=todo.id) }}" class="btn btn-success">✓ Complete</a>
                {% else %}
                    <a href="{{ url_for('uncomplete_todo', todo_id=todo.id) }}" class="btn btn-warning">↺ Undo</a>
                {% endif %}
                <a href="{{ url_for('delete_todo', todo_id=todo.id) }}" class="btn btn-danger">✗ Delete</a>
            </div>
        </div>
        {% endfor %}
    {% else %}
        <p>No todos yet! Add one above to get started.</p>
    {% endif %}

    <br>
    <div style="text-align: center; margin-top: 30px;">
        <a href="{{ url_for('clear_all') }}" class="btn btn-danger">Clear All Completed</a>
        <p style="margin-top: 20px; color: #666;">
            Total: {{ todos|length }} | 
            Completed: {{ todos|selectattr('completed')|list|length }} | 
            Pending: {{ todos|rejectattr('completed')|list|length }}
        </p>
    </div>
</body>
</html>
'''


@app.route('/')
def index():
    '''Display all todos'''
    return render_template_string(TODO_TEMPLATE, todos=todos)


@app.route('/add', methods=['POST'])
def add_todo():
    '''Add a new todo'''
    global next_id
    task = request.form.get('task', '').strip()
    priority = request.form.get('priority', 'medium')

    if task:
        new_todo = {
            'id': next_id,
            'task': task,
            'priority': priority,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
        }
        todos.append(new_todo)
        next_id += 1
        flash(f'Todo "{task}" added successfully!')
    else:
        flash('Task cannot be empty!')

    return redirect(url_for('index'))


@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    '''Mark a todo as completed'''
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = True
            flash(f'Todo "{todo["task"]}" marked as completed!')
            break
    return redirect(url_for('index'))


@app.route('/uncomplete/<int:todo_id>')
def uncomplete_todo(todo_id):
    '''Mark a todo as not completed'''
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = False
            flash(f'Todo "{todo["task"]}" marked as pending!')
            break
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    '''Delete a specific todo'''
    global todos
    for i, todo in enumerate(todos):
        if todo['id'] == todo_id:
            task_name = todo['task']
            todos.pop(i)
            flash(f'Todo "{task_name}" deleted!')
            break
    return redirect(url_for('index'))


@app.route('/clear')
def clear_all():
    '''Delete all completed todos'''
    global todos
    completed_count = len([t for t in todos if t['completed']])
    todos = [t for t in todos if not t['completed']]
    flash(f'{completed_count} completed todo(s) cleared!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    # Add some sample data
    todos = [
        {'id': 1, 'task': 'Learn Flask basics', 'priority': 'high', 'completed': True, 'created_at': '2025-11-10 10:00'},
        {'id': 2, 'task': 'Build a todo app', 'priority': 'medium', 'completed': False, 'created_at': '2025-11-11 09:30'},
        {'id': 3, 'task': 'Deploy to production', 'priority': 'low', 'completed': False, 'created_at': '2025-11-11 14:00'}
    ]
    next_id = 4

    app.run(debug=True, host='0.0.0.0', port=5001)