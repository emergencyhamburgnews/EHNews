
from flask import Flask, render_template, request, redirect, jsonify, url_for
from werkzeug.utils import secure_filename
import os
import json
from datetime import datetime

app = Flask(__name__)

def load_posts():
    try:
        with open('posts.json', 'r') as f:
            return json.load(f)
    except:
        return []

def save_posts(posts):
    with open('posts.json', 'w') as f:
        json.dump(posts, f)

@app.route('/')
def home():
    posts = load_posts()
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['POST'])
def create_post():
    if request.headers.get('NewsHambu86122') != 'NewsHambu86122':  # Replace with your username
        return 'Unauthorized', 401
    
    content = request.form.get('content')
    posts = load_posts()
    posts.append({
        'content': content,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'comments': []
    })
    save_posts(posts)
    return redirect('/')

@app.route('/comment', methods=['POST'])
def add_comment():
    post_id = int(request.form.get('post_id'))
    comment = request.form.get('comment')
    username = request.headers.get('X-Replit-User-Name', 'Anonymous')
    
    posts = load_posts()
    posts[post_id]['comments'].append({
        'content': comment,
        'username': username,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_posts(posts)
    return redirect('/')

# EH page routes
@app.route('/eh')
def eh_page():
    posts = load_eh_posts()
    user_name = request.headers.get('X-Replit-User-Name', '')
    return render_template('EH.html', posts=posts, user_name=user_name)

def load_eh_posts():
    try:
        with open('eh_posts.json', 'r') as f:
            return json.load(f)
    except:
        return []

def save_eh_posts(posts):
    with open('eh_posts.json', 'w') as f:
        json.dump(posts, f)

@app.route('/eh/create_eh_post', methods=['POST'])
def create_eh_post():
    if request.headers.get('X-Replit-User-Name') != 'NewsHambu86122':
        return 'Unauthorized', 401
    
    content = request.form.get('content')
    media = request.files.get('media')
    media_url = None
    media_type = None
    
    if media and media.filename:
        filename = secure_filename(media.filename)
        media.save(os.path.join('static', filename))
        media_url = '/static/' + filename
        media_type = media.content_type

    posts = load_eh_posts()
    posts.append({
        'content': content,
        'media_url': media_url,
        'media_type': media_type,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'likes': []
    })
    save_eh_posts(posts)
    return redirect('/eh')

@app.route('/like_eh_post', methods=['POST'])
def like_eh_post():
    data = request.get_json()
    post_id = int(data.get('post_id'))
    username = request.headers.get('X-Replit-User-Name', '')
    
    posts = load_eh_posts()
    if username not in posts[post_id]['likes']:
        posts[post_id]['likes'].append(username)
    else:
        posts[post_id]['likes'].remove(username)
    
    save_eh_posts(posts)
    return jsonify({'likes': len(posts[post_id]['likes'])})

# Create static folder if it doesn't exist
if not os.path.exists('static'):
    os.makedirs('static')

app.run(host='0.0.0.0', port=8080)

from flask import Flask, render_template, request, redirect, jsonify, url_for
from werkzeug.utils import secure_filename
import os
import json
from datetime import datetime

app = Flask(__name__)

def load_posts():
    try:
        with open('posts.json', 'r') as f:
            posts = json.load(f)
            print(f"Loaded index posts: {posts}")  # Debugging
            return posts
    except Exception as e:
        print(f"Error loading posts.json: {e}")
        return []

def save_posts(posts):
    try:
        with open('posts.json', 'w') as f:
            json.dump(posts, f)
        print("Successfully saved posts to posts.json")  # Debugging
    except Exception as e:
        print(f"Error saving posts to posts.json: {e}")

@app.route('/')
def home():
    posts = load_posts()
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['POST'])
def create_post():
    if request.headers.get('X-Replit-User-Name') != 'NewsHambu86122':
        return 'Unauthorized', 401
    
    content = request.form.get('content')
    posts = load_posts()
    posts.append({
        'content': content,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'comments': []
    })
    save_posts(posts)
    return redirect('/')

@app.route('/comment', methods=['POST'])
def add_comment():
    post_id = int(request.form.get('post_id'))
    comment = request.form.get('comment')
    username = request.headers.get('X-Replit-User-Name', 'Anonymous')
    
    posts = load_posts()
    posts[post_id]['comments'].append({
        'content': comment,
        'username': username,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_posts(posts)
    return redirect('/')

# EH page routes
@app.route('/eh')
def eh_page():
    posts = load_eh_posts()
    user_name = request.headers.get('X-Replit-User-Name', '')
    response = render_template('EH.html', posts=posts, user_name=user_name)
    response = app.make_response(response)
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

def load_eh_posts():
    try:
        with open('eh_posts.json', 'r') as f:
            posts = json.load(f)
            print(f"Loaded EH posts: {posts}")  # Debugging
            return posts
    except Exception as e:
        print(f"Error loading eh_posts.json: {e}")
        return []

def save_eh_posts(posts):
    try:
        with open('eh_posts.json', 'w') as f:
            json.dump(posts, f)
        print("Successfully saved posts to eh_posts.json")  # Debugging
    except Exception as e:
        print(f"Error saving posts to eh_posts.json: {e}")

@app.route('/eh/create_eh_post', methods=['POST'])
def create_eh_post():
    if request.headers.get('X-Replit-User-Name') != 'NewsHambu86122':
        return 'Unauthorized', 401
    
    content = request.form.get('content')
    media = request.files.get('media')
    media_url = None
    media_type = None
    
    if media and media.filename:
        filename = secure_filename(media.filename)
        media_path = os.path.join('static', filename)
        media.save(media_path)
        media_url = '/static/' + filename
        media_type = media.content_type
        print(f"Saved media file to {media_path}")  # Debugging
    
    posts = load_eh_posts()
    new_post = {
        'content': content,
        'media_url': media_url,
        'media_type': media_type,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'likes': []
    }
    posts.append(new_post)
    print(f"New post created: {new_post}")  # Debugging
    save_eh_posts(posts)
    return redirect('/eh')

@app.route('/like_eh_post', methods=['POST'])
def like_eh_post():
    data = request.get_json()
    post_id = int(data.get('post_id'))
    username = request.headers.get('X-Replit-User-Name', '')
    
    posts = load_eh_posts()
    if username not in posts[post_id]['likes']:
        posts[post_id]['likes'].append(username)
    else:
        posts[post_id]['likes'].remove(username)
    
    save_eh_posts(posts)
    return jsonify({'likes': len(posts[post_id]['likes'])})

# Create static folder if it doesn't exist
if not os.path.exists('static'):
    os.makedirs('static')

app.run(host='0.0.0.0', port=8080)