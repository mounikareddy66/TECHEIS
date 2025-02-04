from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    return "Hello, Flask!"  # This message will be displayed in the browser

# Check if the script is run directly (not imported)
if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode 
