from flask import Flask, render_template
import datetime

app = Flask(__name__)

# List of quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Get busy living or get busy dying. - Stephen King",
    "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy",
    "Believe you can and you're halfway there. - Theodore Roosevelt"
]

def get_todays_quote():
    # Get today's date
    today = datetime.datetime.now().date()
    # Use the day of the year to select a quote
    index = today.timetuple().tm_yday % len(quotes)
    return quotes[index]

@app.route('/')
def home():
    quote = get_todays_quote()
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
