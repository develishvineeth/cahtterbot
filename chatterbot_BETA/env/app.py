#imports
from flask import Flask, render_template, request,redirect,url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
#create chatbot
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
englishBot.storage.drop()
#trainer = ChatterBotCorpusTrainer(englishBot)
#trainer.train("chatterbot.corpus.english.humor") #train the chatter bot for english

#englishBot=ChatBot("englishBot",logic_adapters=[{"import_path": "chatterbot.logic.BestMatch","statement_comparison_function":englishBot.comparisons.levenshtein_distance,"response_selection_method": englishBot.response_selection.get_first_response}])

trainer=ListTrainer(englishBot)
trainer.train([
    "hey",
    "hello there",
    "hi",
    "heya",
    "How are you?",
    "I am good.",
    "How are you?",
    "I am fine.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
    "i want software",
    "okk which one??",
    "photo editing",
    "i prefer pixart? should i place a request ?",
    "os for pc",
    "windows10 is the latest.should i placee the request?",
    "ok place it",
    "cool request placed",
    "that sounds cool",
    "cool request placed",
    "sure",
    "ok done",
    "bye",
    "ok bye see ya",

])
chatbot = ChatBot("englishBot",logic_adapters=["chatterbot.logic.BestMatch"])
#define app routes
@app.route("/sucess")
def index():
    return render_template("index.html")

@app.route('/login',methods=["GET","POST"])
def login():
     return render_template('log.html')
            
    

@app.route('/validation', methods=['POST'])
def validation():
    uname = request.form.get('uname')
    passw = request.form.get('pass')
    print(uname,passw)
    if uname == 'admin' and passw=="123456" :
            return render_template('index.html')
    return render_template('log.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))

if __name__ == "__main__":
    app.run()