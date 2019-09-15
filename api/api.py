import flask
from flask import request, jsonify
import os
app = flask.Flask(__name__) #create flask app
app.config["DEBUG"] = True


@app.route('/', methods=['GET']) #Set route to / and method to get. 
def home():
    return "<h1>Test API</h1><p>This is meant to test the feasibility of creating an api for the capstone project</p>"

@app.route('/echo', methods=['GET'])
def test():
    return request.args['string']

@app.route("/website", methods=["GET"])
def website():
    file = open("templates/index.html")
    return file.read()

@app.route('/runScript', methods=['GET'])
def runScript():
    os.system('python discover_topics_UMAP_Kmeans.py -i filelist.txt -c 2019.03.12_SEED_TOPICS_AMY\FILELIST.txt -g testCorpus.txt -o ./results --include_input_in_tfidf -v svd -w 6 -p TODAY2_UMAP_TESTING_LocalTFIDF_SVD_w6_d10 -t 8 -d 10 -u 15 -m cosine')
    file = open("results/TODAY2_UMAP_TESTING_LocalTFIDF_SVD_w6_d10_UMAP_svd.png.html", "r")
    text = file.read()
    return text

@app.route("/NoQString/<num>", methods=["GET"])
def add(num):
    return "The answer to " + str(num) + " + 1 is " + str(int(num)+1)

app.run()