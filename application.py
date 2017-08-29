from flask import Flask, flash, redirect, render_template, request, session, url_for
import twitter
import string
import cfg

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        username = request.form.get("username")
        try:
            words = get_tweets(username)
            return render_template("compose.html", words=words, username=username)
        except twitter.error.TwitterError:
            flash("That username was not found. Please try again.", category="warning")
            return redirect(url_for("index"))


@app.route('/compose/', methods=["GET", "POST"])
def compose():
    if request.method == "GET":
        words = get_tweets()
        return render_template("compose.html", words=words)
    if request.method == "POST":
        return render_template("tweet.html", submitted_tweet=request.form.get("message"))


@app.route('/tweet/', methods=["GET", "POST"])
def tweet():
    return render_template("tweet.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


def get_tweets(username):
    api = twitter.Api(consumer_key=cfg.consumer_key,
                    consumer_secret=cfg.consumer_secret,
                    access_token_key=cfg.access_token_key,
                    access_token_secret=cfg.access_token_secret)
    statuses = api.GetUserTimeline(screen_name=username, include_rts=False, count=150)

    words = []

    for status in statuses:
        for word in status.text.split(' '): # separate words by spaces
            if word != "&amp;" and word != "" and word[0] != "@":
                word = word.strip(string.punctuation).lower()
                if word != "" and word[0] != "#" and word[0] != "@" and word[0:2] != ".@" and \
                   word[0:4] != "http" and "\n" not in word and word not in words:
                    words.append(word)
    words.sort()  # sort words alphabetically
    return words


if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'

    session.init_app(app)

    app.run(host='0.0.0.0',  debug=True)
