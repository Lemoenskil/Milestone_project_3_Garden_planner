{"changed":true,"filter":false,"title":"app.py","tooltip":"/app.py","value":"import os\nfrom flask import Flask, render_template, redirect, request, url_for\nfrom flask_pymongo import PyMongo\nfrom bson.objectid import ObjectId\n\n\n\napp = Flask (\"----name----\")\n@app.route('/')\ndef hello():\n    return \"hello world\"\n\nif __name__ == '__main__':\n    app.run(host=os.environ.get('IP'),\n            port=int(os.environ.get('PORT')),\n            debug=True)","undoManager":{"mark":66,"position":68,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["I"],"id":1},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":["m"],"id":2},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["I"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":3},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":4},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["o"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":0,"column":9},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":5}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["import os",""],"id":6},{"start":{"row":0,"column":0},"end":{"row":3,"column":34},"action":"insert","lines":["import os","from flask import Flask, render_template, redirect, request, url_for","from flask_pymongo import PyMongo","from bson.objectid import ObjectId"]}],[{"start":{"row":3,"column":34},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":9,"column":23},"action":"insert","lines":["if __name__ == '__main__':","    app.run(host=os.environ.get('IP'),","            port=int(os.environ.get('PORT')),","            debug=True)"],"id":8}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":9}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["@"],"id":10}],[{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"insert","lines":["a"],"id":11},{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"insert","lines":["p"]},{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"insert","lines":["p"]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["."],"id":12},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["r"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["o"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["u"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["t"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":10},"end":{"row":5,"column":12},"action":"insert","lines":["()"],"id":13}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":13},"action":"insert","lines":["\"\""],"id":14}],[{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["/"],"id":15}],[{"start":{"row":5,"column":15},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":16}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "],"id":17}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["d"],"id":18},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["e"]},{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["f"]}],[{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":[" "],"id":19},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["h"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["e"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["l"]}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":[";"],"id":20}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"remove","lines":[";"],"id":21}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["l"],"id":22},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["l"]}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"remove","lines":["l"],"id":23}],[{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["o"],"id":24}],[{"start":{"row":6,"column":13},"end":{"row":6,"column":15},"action":"insert","lines":["()"],"id":25}],[{"start":{"row":6,"column":15},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":26},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["r"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["t"],"id":27},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["e"]},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["r"]}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"remove","lines":["r"],"id":28},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"remove","lines":["e"]}],[{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["u"],"id":29},{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["r"]},{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":[" "],"id":30}],[{"start":{"row":7,"column":11},"end":{"row":7,"column":13},"action":"insert","lines":["\"\""],"id":31}],[{"start":{"row":7,"column":12},"end":{"row":7,"column":13},"action":"insert","lines":["h"],"id":32},{"start":{"row":7,"column":13},"end":{"row":7,"column":14},"action":"insert","lines":["e"]},{"start":{"row":7,"column":14},"end":{"row":7,"column":15},"action":"insert","lines":["l"]},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["o"]},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"remove","lines":["o"],"id":33},{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"remove","lines":["o"]}],[{"start":{"row":7,"column":15},"end":{"row":7,"column":16},"action":"insert","lines":["l"],"id":34},{"start":{"row":7,"column":16},"end":{"row":7,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":7,"column":17},"end":{"row":7,"column":18},"action":"insert","lines":[" "],"id":35},{"start":{"row":7,"column":18},"end":{"row":7,"column":19},"action":"insert","lines":["w"]},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["o"]},{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["r"]},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["l"]},{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["d"]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":8},"action":"insert","lines":["    "],"id":36}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "],"id":37}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":8},"action":"remove","lines":["    "],"id":38}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"remove","lines":["\""],"id":39}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["'"],"id":40}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"remove","lines":["\""],"id":41}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["'"],"id":42}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":[":"],"id":43}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"remove","lines":[":"],"id":44}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":[";"],"id":45}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"remove","lines":[";"],"id":46}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":[":"],"id":47}],[{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":48}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["a"],"id":49},{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"insert","lines":["p"]},{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"insert","lines":["p"]}],[{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"insert","lines":[" "],"id":50},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["="]}],[{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":[" "],"id":51},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["F"]}],[{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["l"],"id":52},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["a"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["s"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["k"]}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":[" "],"id":53}],[{"start":{"row":5,"column":12},"end":{"row":5,"column":14},"action":"insert","lines":["()"],"id":54}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["-"],"id":55},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["-"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["-"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["-"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["n"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["a"]}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["m"],"id":56},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["e"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["_"]}],[{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":[" "],"id":57},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":[" "]}],[{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"remove","lines":[" "],"id":58},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"remove","lines":[" "]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"remove","lines":["_"]}],[{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["-"],"id":59},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["-"]},{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":["-"]}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["-"],"id":60}],[{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["\""],"id":61}],[{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"insert","lines":["\""],"id":62}],[{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":[" "],"id":63}],[{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"remove","lines":[" "],"id":64}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["p"],"id":65}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["p"],"id":66}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "],"id":67},{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"remove","lines":["# "],"id":68},{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":3,"column":34},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":69},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":0},"end":{"row":5,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1578849120236}