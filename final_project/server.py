import json
from machinetranslation import translator
from flask import Flask, render_template, request
from machinetranslation.translator import englishToFrench as eng_fr
from machinetranslation.translator import frenchToEnglish as fr_eng

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return eng_fr(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return fr_eng(textToTranslate)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
