from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_image_files():
    """Get list of image files from the static/images directory"""
    image_files = []
    if os.path.exists(UPLOAD_FOLDER):
        for filename in os.listdir(UPLOAD_FOLDER):
            if allowed_file(filename):
                image_files.append(filename)
    return sorted(image_files)

@app.route('/')
def index():
    """Main page showing the image gallery"""
    images = get_image_files()
    return render_template('index.html', images=images)

@app.route('/images/<filename>')
def uploaded_file(filename):
    """Serve uploaded images"""
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    # Create the images directory if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    # Run the app in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)
