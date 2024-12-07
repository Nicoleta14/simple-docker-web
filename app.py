from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple Web App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                margin: 0;
                background: #f5f5f5;
                color: #333;
                text-align: center;
            }
            h1 {
                font-size: 2.5rem;
                color: #4CAF50;
            }
            p {
                font-size: 1.2rem;
                margin: 10px 0;
            }
            button {
                background: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 1rem;
                border-radius: 5px;
                cursor: pointer;
                transition: background 0.3s ease;
            }
            button:hover {
                background: #45a049;
            }
        </style>
    </head>
    <body>
        <h1>Welcome!</h1>
        <p>Explore your simple web app.</p>
        <button>Get Started</button>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
