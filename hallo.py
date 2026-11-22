from flask import Flask

app = Flask(__name__)


# Когда браузер открывает главную страницу, Flask вызывает эту функцию.
@app.get("/")
def home():
    return """
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Ai Survey</title>
</head>
<body>
    <h1>опросник</h1>
    <h2>очень ОЧЕНЬ важные слова</h2>
    <p>крутой оч</p>
    <p>крутой оч67</p>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(port=5001)