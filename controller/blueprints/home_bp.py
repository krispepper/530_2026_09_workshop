#Purpose: Return the home page for our workshop app
from flask import Blueprint, render_template, redirect, abort
from jinja2.exceptions import TemplateNotFound
from model.model import model
from model import user, enroll
import time # Added to track our 30-minute timer

home_bp = Blueprint('home', __name__, template_folder='templates')

# Cache variables to hold our data and timer
cached_top_workshops = None
last_fetched_time = 0
CACHE_LIMIT = 30 * 60 # 30 minutes (in seconds)

# Route for the home dashboard displaying system messages and top workshops
@home_bp.route('/')
@home_bp.route('/home')
def home():
    global cached_top_workshops, last_fetched_time
    
    try:
        current_time = time.time()
        
        # Check if we have no data yet, OR if 30 minutes have passed
        if cached_top_workshops is None or (current_time - last_fetched_time) > CACHE_LIMIT:
            # Time is up! Fetch fresh data from the database
            cached_top_workshops = enroll.get_top_subscribed_workshops(limit=5)
            last_fetched_time = current_time
            print("Fetching fresh workshop list from database...") # Helpful for testing
            
        # Pass our (cached or newly fetched) data to the HTML template
        return render_template('home.html', top_workshops=cached_top_workshops)
        
    except TemplateNotFound:
        # if we can't render the home page, return a 404 error
        abort(404)