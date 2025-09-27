# Image Gallery Website

A beautiful, responsive image gallery built with Flask and Python.

## Features

- 🖼️ Display images in a responsive grid layout
- 📱 Mobile-friendly design
- 🎨 Modern, beautiful UI with hover effects
- ⚡ Fast loading and optimized performance
- 🔍 Click images to view full size

## Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd website
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your images**
   - Place your JPG/PNG files in `static/images/` folder
   - Supported formats: JPG, JPEG, PNG, GIF, BMP

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   - Go to `http://localhost:5000`

## Deployment

This app is ready for deployment on:
- Railway
- Render
- Heroku
- PythonAnywhere

## Project Structure

```
website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # For Heroku deployment
├── templates/
│   └── index.html        # Gallery template
├── static/
│   └── images/           # Your image files
└── venv/                 # Virtual environment
```

## Adding Images

Simply copy your image files into the `static/images/` directory and refresh the page. The gallery will automatically display all supported image formats.
