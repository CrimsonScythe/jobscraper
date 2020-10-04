import flask
from flask.helpers import send_from_directory
from flask.json import jsonify
import psycopg2
import collections
import matplotlib
import matplotlib.pyplot as plt
import numpy
import os


app = flask.Flask(__name__, static_url_path='')
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>YOLO</h1><p>Hello World!</p><br>dfd"

@app.route('/api/v1/resources/all', methods=['GET'])
def api_all():
    conn = psycopg2.connect(dbname='grad', user='postgres', password='root')
    cursor = conn.cursor()
    query=""" SELECT * FROM jobs"""
    # for i in range(len(frameworks)):
    cursor.execute(query)
    lstOfTuples = cursor.fetchall()
    return jsonify(lstOfTuples)
    # cursor.execute(query, ("mmdfg", 2, ["s", "s"], ["ss", "s"]))
    # conn.commit()

@app.route('/api/v1/top3lang', methods=['GET'])
def api_show3lang():
    root_dir = os.path.dirname(os.getcwd())
    print(root_dir)
    final_path = os.path.join(root_dir, 'api')
    # print(final_path)
    return send_from_directory(os.path.join(root_dir, 'api'), 'to.png')
    # return f"<img src={final_path} alt='s' />"

@app.route('/api/v1/top3langfetch', methods=['GET'])
def api_3toplangfetch():
    conn = psycopg2.connect(dbname='grad', user='postgres', password='root')
    cursor = conn.cursor()
    query=""" SELECT languages FROM jobs"""
    # for i in range(len(frameworks)):
    cursor.execute(query)
    lstOfTuples = cursor.fetchall()
    # print(lstOfTuples)
    print(type(lstOfTuples))
    print(type(lstOfTuples[0]))
    print (type((lstOfTuples[0])[0]))
    

    lst=[]

    for i in lstOfTuples:
        for j in i[0]:
            lst.append(j)

    # flatten = map(lambda lstOfTuples: [item for sublist in lstOfTuples for item in sublist[0]], lstOfTuples)
   
    counter = collections.Counter(lst)
    common = counter.most_common(3) 

    print(common)
    lstnames = []
    lstnum=[]
    for i in common:
        lstnames.append(i[0])
        lstnum.append(i[1])

    print(lstnames)
    y_pos = numpy.arange(len(lstnames))
    print(lstnum)

    plt.bar(y_pos, lstnum, align='center', alpha=0.5)
    plt.xticks(y_pos, lstnames)
    plt.ylabel('Usage')
    plt.title('Programming language usage')
    plt.savefig('to.png')
    


    # plt.show()
    
    # return jsonify(common)
    # return app.send_static_file('to.png')
    

app.run()