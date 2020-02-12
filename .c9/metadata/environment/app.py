{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":74,"column":0},"end":{"row":75,"column":0},"action":"remove","lines":["        ",""],"id":2118}],[{"start":{"row":77,"column":12},"end":{"row":77,"column":42},"action":"remove","lines":["# check password using hashing"],"id":2119},{"start":{"row":77,"column":12},"end":{"row":77,"column":13},"action":"insert","lines":["h"]},{"start":{"row":77,"column":13},"end":{"row":77,"column":14},"action":"insert","lines":["a"]},{"start":{"row":77,"column":14},"end":{"row":77,"column":15},"action":"insert","lines":["s"]},{"start":{"row":77,"column":15},"end":{"row":77,"column":16},"action":"insert","lines":["h"]},{"start":{"row":77,"column":16},"end":{"row":77,"column":17},"action":"insert","lines":["e"]},{"start":{"row":77,"column":17},"end":{"row":77,"column":18},"action":"insert","lines":["d"]},{"start":{"row":77,"column":18},"end":{"row":77,"column":19},"action":"insert","lines":["_"]}],[{"start":{"row":77,"column":12},"end":{"row":77,"column":19},"action":"remove","lines":["hashed_"],"id":2120},{"start":{"row":77,"column":12},"end":{"row":77,"column":27},"action":"insert","lines":["hashed_password"]}],[{"start":{"row":77,"column":27},"end":{"row":77,"column":28},"action":"insert","lines":[" "],"id":2121},{"start":{"row":77,"column":28},"end":{"row":77,"column":29},"action":"insert","lines":["="]}],[{"start":{"row":77,"column":29},"end":{"row":77,"column":30},"action":"insert","lines":[" "],"id":2122}],[{"start":{"row":78,"column":15},"end":{"row":79,"column":52},"action":"remove","lines":["bcrypt.hashpw(request.form['password'].encode('utf-8'),","                             found_user['password'])"],"id":2123}],[{"start":{"row":77,"column":30},"end":{"row":78,"column":52},"action":"insert","lines":["bcrypt.hashpw(request.form['password'].encode('utf-8'),","                             found_user['password'])"],"id":2124}],[{"start":{"row":77,"column":44},"end":{"row":78,"column":0},"action":"insert","lines":["",""],"id":2125},{"start":{"row":78,"column":0},"end":{"row":78,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":79,"column":51},"end":{"row":80,"column":0},"action":"insert","lines":["",""],"id":2126},{"start":{"row":80,"column":0},"end":{"row":80,"column":29},"action":"insert","lines":["                             "]}],[{"start":{"row":80,"column":28},"end":{"row":80,"column":29},"action":"remove","lines":[" "],"id":2127},{"start":{"row":80,"column":24},"end":{"row":80,"column":28},"action":"remove","lines":["    "]},{"start":{"row":80,"column":20},"end":{"row":80,"column":24},"action":"remove","lines":["    "]},{"start":{"row":80,"column":16},"end":{"row":80,"column":20},"action":"remove","lines":["    "]},{"start":{"row":80,"column":12},"end":{"row":80,"column":16},"action":"remove","lines":["    "]}],[{"start":{"row":79,"column":12},"end":{"row":79,"column":16},"action":"remove","lines":["    "],"id":2128},{"start":{"row":79,"column":12},"end":{"row":79,"column":16},"action":"remove","lines":["    "]},{"start":{"row":79,"column":12},"end":{"row":79,"column":16},"action":"remove","lines":["    "]},{"start":{"row":79,"column":12},"end":{"row":79,"column":16},"action":"remove","lines":["    "]},{"start":{"row":79,"column":12},"end":{"row":79,"column":13},"action":"remove","lines":[" "]}],[{"start":{"row":79,"column":12},"end":{"row":79,"column":16},"action":"insert","lines":["    "],"id":2129}],[{"start":{"row":49,"column":57},"end":{"row":49,"column":58},"action":"remove","lines":[" "],"id":2130}],[{"start":{"row":49,"column":57},"end":{"row":50,"column":0},"action":"insert","lines":["",""],"id":2131},{"start":{"row":50,"column":0},"end":{"row":50,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":82,"column":15},"end":{"row":82,"column":29},"action":"insert","lines":["bcrypt.checkpw"],"id":2132}],[{"start":{"row":82,"column":29},"end":{"row":82,"column":31},"action":"insert","lines":["()"],"id":2133}],[{"start":{"row":82,"column":30},"end":{"row":82,"column":70},"action":"insert","lines":["request.form['password'].encode('utf-8')"],"id":2134}],[{"start":{"row":82,"column":70},"end":{"row":82,"column":75},"action":"remove","lines":[") == "],"id":2135},{"start":{"row":82,"column":70},"end":{"row":82,"column":71},"action":"insert","lines":[","]}],[{"start":{"row":82,"column":71},"end":{"row":82,"column":72},"action":"insert","lines":[" "],"id":2136}],[{"start":{"row":82,"column":94},"end":{"row":82,"column":95},"action":"insert","lines":[")"],"id":2137}],[{"start":{"row":82,"column":15},"end":{"row":82,"column":95},"action":"remove","lines":["bcrypt.checkpw(request.form['password'].encode('utf-8'), found_user['password'])"],"id":2138}],[{"start":{"row":78,"column":12},"end":{"row":81,"column":13},"action":"remove","lines":["hashed_password = bcrypt.hashpw(","                request.form['password'].encode('utf-8'),","                found_user['password']","            )"],"id":2139},{"start":{"row":78,"column":12},"end":{"row":78,"column":13},"action":"insert","lines":["p"]},{"start":{"row":78,"column":13},"end":{"row":78,"column":14},"action":"insert","lines":["a"]},{"start":{"row":78,"column":14},"end":{"row":78,"column":15},"action":"insert","lines":["s"]},{"start":{"row":78,"column":15},"end":{"row":78,"column":16},"action":"insert","lines":["s"]},{"start":{"row":78,"column":16},"end":{"row":78,"column":17},"action":"insert","lines":["w"]},{"start":{"row":78,"column":17},"end":{"row":78,"column":18},"action":"insert","lines":["o"]},{"start":{"row":78,"column":18},"end":{"row":78,"column":19},"action":"insert","lines":["r"]},{"start":{"row":78,"column":19},"end":{"row":78,"column":20},"action":"insert","lines":["d"]},{"start":{"row":78,"column":20},"end":{"row":78,"column":21},"action":"insert","lines":["_"]}],[{"start":{"row":78,"column":21},"end":{"row":78,"column":22},"action":"insert","lines":["m"],"id":2140},{"start":{"row":78,"column":22},"end":{"row":78,"column":23},"action":"insert","lines":["a"]},{"start":{"row":78,"column":23},"end":{"row":78,"column":24},"action":"insert","lines":["t"]},{"start":{"row":78,"column":24},"end":{"row":78,"column":25},"action":"insert","lines":["c"]},{"start":{"row":78,"column":25},"end":{"row":78,"column":26},"action":"insert","lines":["h"]},{"start":{"row":78,"column":26},"end":{"row":78,"column":27},"action":"insert","lines":["e"]},{"start":{"row":78,"column":27},"end":{"row":78,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":78,"column":28},"end":{"row":78,"column":29},"action":"insert","lines":[" "],"id":2141},{"start":{"row":78,"column":29},"end":{"row":78,"column":30},"action":"insert","lines":["="]}],[{"start":{"row":78,"column":30},"end":{"row":78,"column":31},"action":"insert","lines":[" "],"id":2142}],[{"start":{"row":78,"column":31},"end":{"row":78,"column":111},"action":"insert","lines":["bcrypt.checkpw(request.form['password'].encode('utf-8'), found_user['password'])"],"id":2143}],[{"start":{"row":78,"column":46},"end":{"row":79,"column":0},"action":"insert","lines":["",""],"id":2144},{"start":{"row":79,"column":0},"end":{"row":79,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":79,"column":57},"end":{"row":79,"column":58},"action":"remove","lines":[" "],"id":2145}],[{"start":{"row":79,"column":57},"end":{"row":80,"column":0},"action":"insert","lines":["",""],"id":2146},{"start":{"row":80,"column":0},"end":{"row":80,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":80,"column":38},"end":{"row":81,"column":0},"action":"insert","lines":["",""],"id":2147},{"start":{"row":81,"column":0},"end":{"row":81,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":81,"column":12},"end":{"row":81,"column":16},"action":"remove","lines":["    "],"id":2148}],[{"start":{"row":82,"column":15},"end":{"row":82,"column":31},"action":"insert","lines":["password_matches"],"id":2149}],[{"start":{"row":85,"column":0},"end":{"row":86,"column":0},"action":"remove","lines":["                # successful redirect to home logged in",""],"id":2150}],[{"start":{"row":82,"column":32},"end":{"row":83,"column":0},"action":"insert","lines":["",""],"id":2151},{"start":{"row":83,"column":0},"end":{"row":83,"column":16},"action":"insert","lines":["                "]},{"start":{"row":83,"column":16},"end":{"row":83,"column":17},"action":"insert","lines":["#"]}],[{"start":{"row":83,"column":17},"end":{"row":83,"column":18},"action":"insert","lines":[" "],"id":2152},{"start":{"row":83,"column":18},"end":{"row":83,"column":19},"action":"insert","lines":["S"]},{"start":{"row":83,"column":19},"end":{"row":83,"column":20},"action":"insert","lines":["u"]},{"start":{"row":83,"column":20},"end":{"row":83,"column":21},"action":"insert","lines":["c"]},{"start":{"row":83,"column":21},"end":{"row":83,"column":22},"action":"insert","lines":["c"]},{"start":{"row":83,"column":22},"end":{"row":83,"column":23},"action":"insert","lines":["e"]},{"start":{"row":83,"column":23},"end":{"row":83,"column":24},"action":"insert","lines":["s"]},{"start":{"row":83,"column":24},"end":{"row":83,"column":25},"action":"insert","lines":["s"]},{"start":{"row":83,"column":25},"end":{"row":83,"column":26},"action":"insert","lines":["f"]},{"start":{"row":83,"column":26},"end":{"row":83,"column":27},"action":"insert","lines":["u"]},{"start":{"row":83,"column":27},"end":{"row":83,"column":28},"action":"insert","lines":["l"]}],[{"start":{"row":83,"column":28},"end":{"row":83,"column":29},"action":"insert","lines":[" "],"id":2153},{"start":{"row":83,"column":29},"end":{"row":83,"column":30},"action":"insert","lines":["l"]},{"start":{"row":83,"column":30},"end":{"row":83,"column":31},"action":"insert","lines":["o"]},{"start":{"row":83,"column":31},"end":{"row":83,"column":32},"action":"insert","lines":["g"]},{"start":{"row":83,"column":32},"end":{"row":83,"column":33},"action":"insert","lines":["-"]}],[{"start":{"row":83,"column":33},"end":{"row":83,"column":34},"action":"insert","lines":["i"],"id":2154},{"start":{"row":83,"column":34},"end":{"row":83,"column":35},"action":"insert","lines":["n"]},{"start":{"row":83,"column":35},"end":{"row":83,"column":36},"action":"insert","lines":[","]}],[{"start":{"row":83,"column":36},"end":{"row":83,"column":37},"action":"insert","lines":[" "],"id":2155},{"start":{"row":83,"column":37},"end":{"row":83,"column":38},"action":"insert","lines":["r"]},{"start":{"row":83,"column":38},"end":{"row":83,"column":39},"action":"insert","lines":["e"]},{"start":{"row":83,"column":39},"end":{"row":83,"column":40},"action":"insert","lines":["d"]},{"start":{"row":83,"column":40},"end":{"row":83,"column":41},"action":"insert","lines":["u"]},{"start":{"row":83,"column":41},"end":{"row":83,"column":42},"action":"insert","lines":["r"]},{"start":{"row":83,"column":42},"end":{"row":83,"column":43},"action":"insert","lines":["e"]},{"start":{"row":83,"column":43},"end":{"row":83,"column":44},"action":"insert","lines":["c"]},{"start":{"row":83,"column":44},"end":{"row":83,"column":45},"action":"insert","lines":["t"]}],[{"start":{"row":83,"column":40},"end":{"row":83,"column":41},"action":"remove","lines":["u"],"id":2156},{"start":{"row":83,"column":40},"end":{"row":83,"column":41},"action":"insert","lines":["i"]}],[{"start":{"row":83,"column":35},"end":{"row":83,"column":36},"action":"remove","lines":[","],"id":2157},{"start":{"row":83,"column":35},"end":{"row":83,"column":36},"action":"insert","lines":[":"]}],[{"start":{"row":83,"column":36},"end":{"row":83,"column":37},"action":"insert","lines":[" "],"id":2158},{"start":{"row":83,"column":37},"end":{"row":83,"column":38},"action":"insert","lines":["S"]},{"start":{"row":83,"column":38},"end":{"row":83,"column":39},"action":"insert","lines":["t"]},{"start":{"row":83,"column":39},"end":{"row":83,"column":40},"action":"insert","lines":["o"]},{"start":{"row":83,"column":40},"end":{"row":83,"column":41},"action":"insert","lines":["r"]},{"start":{"row":83,"column":41},"end":{"row":83,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":83,"column":42},"end":{"row":83,"column":43},"action":"insert","lines":[" "],"id":2159}],[{"start":{"row":83,"column":43},"end":{"row":83,"column":44},"action":"insert","lines":["u"],"id":2160},{"start":{"row":83,"column":44},"end":{"row":83,"column":45},"action":"insert","lines":["s"]},{"start":{"row":83,"column":45},"end":{"row":83,"column":46},"action":"insert","lines":["e"]},{"start":{"row":83,"column":46},"end":{"row":83,"column":47},"action":"insert","lines":["r"]}],[{"start":{"row":83,"column":37},"end":{"row":83,"column":47},"action":"remove","lines":["Store user"],"id":2161},{"start":{"row":83,"column":37},"end":{"row":83,"column":38},"action":"insert","lines":["S"]},{"start":{"row":83,"column":38},"end":{"row":83,"column":39},"action":"insert","lines":["t"]},{"start":{"row":83,"column":39},"end":{"row":83,"column":40},"action":"insert","lines":["o"]},{"start":{"row":83,"column":40},"end":{"row":83,"column":41},"action":"insert","lines":["r"]},{"start":{"row":83,"column":41},"end":{"row":83,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":83,"column":42},"end":{"row":83,"column":43},"action":"insert","lines":[" "],"id":2162},{"start":{"row":83,"column":43},"end":{"row":83,"column":44},"action":"insert","lines":["a"]},{"start":{"row":83,"column":44},"end":{"row":83,"column":45},"action":"insert","lines":["n"]},{"start":{"row":83,"column":45},"end":{"row":83,"column":46},"action":"insert","lines":["d"]}],[{"start":{"row":87,"column":0},"end":{"row":88,"column":0},"action":"remove","lines":["            # must have failed set flash message",""],"id":2163}],[{"start":{"row":87,"column":35},"end":{"row":87,"column":36},"action":"insert","lines":[" "],"id":2164}],[{"start":{"row":87,"column":37},"end":{"row":87,"column":38},"action":"insert","lines":[" "],"id":2165}],[{"start":{"row":111,"column":16},"end":{"row":112,"column":0},"action":"insert","lines":["",""],"id":2166},{"start":{"row":112,"column":0},"end":{"row":112,"column":4},"action":"insert","lines":["    "]},{"start":{"row":112,"column":4},"end":{"row":112,"column":5},"action":"insert","lines":["i"]},{"start":{"row":112,"column":5},"end":{"row":112,"column":6},"action":"insert","lines":["f"]}],[{"start":{"row":112,"column":6},"end":{"row":112,"column":7},"action":"insert","lines":[" "],"id":2167}],[{"start":{"row":112,"column":7},"end":{"row":112,"column":35},"action":"insert","lines":["if 'username' not in session"],"id":2168}],[{"start":{"row":112,"column":6},"end":{"row":112,"column":7},"action":"remove","lines":[" "],"id":2169},{"start":{"row":112,"column":5},"end":{"row":112,"column":6},"action":"remove","lines":["f"]},{"start":{"row":112,"column":4},"end":{"row":112,"column":5},"action":"remove","lines":["i"]}],[{"start":{"row":112,"column":32},"end":{"row":112,"column":33},"action":"insert","lines":[":"],"id":2170}],[{"start":{"row":112,"column":33},"end":{"row":113,"column":0},"action":"insert","lines":["",""],"id":2171},{"start":{"row":113,"column":0},"end":{"row":113,"column":8},"action":"insert","lines":["        "]},{"start":{"row":113,"column":8},"end":{"row":113,"column":9},"action":"insert","lines":["r"]},{"start":{"row":113,"column":9},"end":{"row":113,"column":10},"action":"insert","lines":["e"]},{"start":{"row":113,"column":10},"end":{"row":113,"column":11},"action":"insert","lines":["t"]},{"start":{"row":113,"column":11},"end":{"row":113,"column":12},"action":"insert","lines":["u"]},{"start":{"row":113,"column":12},"end":{"row":113,"column":13},"action":"insert","lines":["r"]},{"start":{"row":113,"column":13},"end":{"row":113,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":113,"column":14},"end":{"row":113,"column":15},"action":"insert","lines":[" "],"id":2172}],[{"start":{"row":113,"column":8},"end":{"row":113,"column":15},"action":"remove","lines":["return "],"id":2173},{"start":{"row":113,"column":8},"end":{"row":113,"column":18},"action":"insert","lines":["abort(401)"]}],[{"start":{"row":1,"column":50},"end":{"row":1,"column":51},"action":"insert","lines":[","],"id":2174}],[{"start":{"row":1,"column":51},"end":{"row":1,"column":52},"action":"insert","lines":[" "],"id":2175},{"start":{"row":1,"column":52},"end":{"row":1,"column":53},"action":"insert","lines":["a"]},{"start":{"row":1,"column":53},"end":{"row":1,"column":54},"action":"insert","lines":["b"]},{"start":{"row":1,"column":54},"end":{"row":1,"column":55},"action":"insert","lines":["o"]},{"start":{"row":1,"column":55},"end":{"row":1,"column":56},"action":"insert","lines":["r"]},{"start":{"row":1,"column":56},"end":{"row":1,"column":57},"action":"insert","lines":["t"]}],[{"start":{"row":113,"column":8},"end":{"row":113,"column":18},"action":"remove","lines":["abort(401)"],"id":2176},{"start":{"row":113,"column":8},"end":{"row":113,"column":9},"action":"insert","lines":["r"]},{"start":{"row":113,"column":9},"end":{"row":113,"column":10},"action":"insert","lines":["e"]},{"start":{"row":113,"column":10},"end":{"row":113,"column":11},"action":"insert","lines":["t"]},{"start":{"row":113,"column":11},"end":{"row":113,"column":12},"action":"insert","lines":["u"]},{"start":{"row":113,"column":12},"end":{"row":113,"column":13},"action":"insert","lines":["r"]},{"start":{"row":113,"column":13},"end":{"row":113,"column":14},"action":"insert","lines":["n"]}],[{"start":{"row":113,"column":14},"end":{"row":113,"column":15},"action":"insert","lines":[" "],"id":2177}],[{"start":{"row":113,"column":15},"end":{"row":113,"column":50},"action":"insert","lines":["redirect(url_for('get_plant_record'"],"id":2178}],[{"start":{"row":113,"column":50},"end":{"row":113,"column":51},"action":"insert","lines":[")"],"id":2179},{"start":{"row":113,"column":51},"end":{"row":113,"column":52},"action":"insert","lines":[")"]}],[{"start":{"row":113,"column":33},"end":{"row":113,"column":49},"action":"remove","lines":["get_plant_record"],"id":2180},{"start":{"row":113,"column":33},"end":{"row":113,"column":34},"action":"insert","lines":["l"]},{"start":{"row":113,"column":34},"end":{"row":113,"column":35},"action":"insert","lines":["o"]},{"start":{"row":113,"column":35},"end":{"row":113,"column":36},"action":"insert","lines":["g"]},{"start":{"row":113,"column":36},"end":{"row":113,"column":37},"action":"insert","lines":["i"]},{"start":{"row":113,"column":37},"end":{"row":113,"column":38},"action":"insert","lines":["n"]}],[{"start":{"row":109,"column":0},"end":{"row":109,"column":4},"action":"remove","lines":["    "],"id":2181}],[{"start":{"row":109,"column":0},"end":{"row":110,"column":0},"action":"insert","lines":["",""],"id":2182},{"start":{"row":110,"column":0},"end":{"row":110,"column":1},"action":"insert","lines":["d"]},{"start":{"row":110,"column":1},"end":{"row":110,"column":2},"action":"insert","lines":["e"]},{"start":{"row":110,"column":2},"end":{"row":110,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":110,"column":3},"end":{"row":110,"column":4},"action":"insert","lines":[" "],"id":2183}],[{"start":{"row":110,"column":0},"end":{"row":110,"column":4},"action":"remove","lines":["def "],"id":2184}],[{"start":{"row":109,"column":0},"end":{"row":110,"column":0},"action":"remove","lines":["",""],"id":2185}],[{"start":{"row":124,"column":0},"end":{"row":126,"column":0},"action":"insert","lines":["    if 'username' not in session:","        return redirect(url_for('login'))",""],"id":2186}],[{"start":{"row":118,"column":0},"end":{"row":120,"column":0},"action":"insert","lines":["    if 'username' not in session:","        return redirect(url_for('login'))",""],"id":2187}],[{"start":{"row":119,"column":8},"end":{"row":119,"column":41},"action":"remove","lines":["return redirect(url_for('login'))"],"id":2188},{"start":{"row":119,"column":8},"end":{"row":119,"column":9},"action":"insert","lines":["a"]},{"start":{"row":119,"column":9},"end":{"row":119,"column":10},"action":"insert","lines":["b"]},{"start":{"row":119,"column":10},"end":{"row":119,"column":11},"action":"insert","lines":["o"]},{"start":{"row":119,"column":11},"end":{"row":119,"column":12},"action":"insert","lines":["r"]},{"start":{"row":119,"column":12},"end":{"row":119,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":119,"column":13},"end":{"row":119,"column":15},"action":"insert","lines":["()"],"id":2189}],[{"start":{"row":119,"column":14},"end":{"row":119,"column":15},"action":"insert","lines":["4"],"id":2190},{"start":{"row":119,"column":15},"end":{"row":119,"column":16},"action":"insert","lines":["0"]},{"start":{"row":119,"column":16},"end":{"row":119,"column":17},"action":"insert","lines":["1"]}],[{"start":{"row":157,"column":0},"end":{"row":159,"column":0},"action":"insert","lines":["    if 'username' not in session:","        abort(401)",""],"id":2191}],[{"start":{"row":165,"column":0},"end":{"row":167,"column":0},"action":"insert","lines":["    if 'username' not in session:","        abort(401)",""],"id":2192}],[{"start":{"row":44,"column":110},"end":{"row":45,"column":57},"action":"remove","lines":["","            return redirect(url_for('register_new_user'))"],"id":2199}],[{"start":{"row":163,"column":27},"end":{"row":164,"column":0},"action":"insert","lines":["",""],"id":2200},{"start":{"row":164,"column":0},"end":{"row":164,"column":4},"action":"insert","lines":["    "]},{"start":{"row":164,"column":4},"end":{"row":164,"column":5},"action":"insert","lines":["p"]},{"start":{"row":164,"column":5},"end":{"row":164,"column":6},"action":"insert","lines":["r"]},{"start":{"row":164,"column":6},"end":{"row":164,"column":7},"action":"insert","lines":["i"]},{"start":{"row":164,"column":7},"end":{"row":164,"column":8},"action":"insert","lines":["n"]},{"start":{"row":164,"column":8},"end":{"row":164,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":164,"column":9},"end":{"row":164,"column":11},"action":"insert","lines":["()"],"id":2201}],[{"start":{"row":164,"column":10},"end":{"row":164,"column":12},"action":"insert","lines":["''"],"id":2202}],[{"start":{"row":164,"column":11},"end":{"row":164,"column":12},"action":"insert","lines":["d"],"id":2203},{"start":{"row":164,"column":12},"end":{"row":164,"column":13},"action":"insert","lines":["e"]},{"start":{"row":164,"column":13},"end":{"row":164,"column":14},"action":"insert","lines":["l"]},{"start":{"row":164,"column":14},"end":{"row":164,"column":15},"action":"insert","lines":["e"]},{"start":{"row":164,"column":15},"end":{"row":164,"column":16},"action":"insert","lines":["t"]},{"start":{"row":164,"column":16},"end":{"row":164,"column":17},"action":"insert","lines":["e"]},{"start":{"row":164,"column":17},"end":{"row":164,"column":18},"action":"insert","lines":["_"]},{"start":{"row":164,"column":18},"end":{"row":164,"column":19},"action":"insert","lines":["p"]},{"start":{"row":164,"column":19},"end":{"row":164,"column":20},"action":"insert","lines":["l"]},{"start":{"row":164,"column":20},"end":{"row":164,"column":21},"action":"insert","lines":["a"]}],[{"start":{"row":164,"column":21},"end":{"row":164,"column":22},"action":"insert","lines":["n"],"id":2204},{"start":{"row":164,"column":22},"end":{"row":164,"column":23},"action":"insert","lines":["t"]}],[{"start":{"row":164,"column":0},"end":{"row":165,"column":0},"action":"remove","lines":["    print('delete_plant')",""],"id":2205}],[{"start":{"row":162,"column":37},"end":{"row":162,"column":38},"action":"insert","lines":[","],"id":2207}],[{"start":{"row":162,"column":38},"end":{"row":162,"column":39},"action":"insert","lines":[" "],"id":2208},{"start":{"row":162,"column":39},"end":{"row":162,"column":40},"action":"insert","lines":["m"]},{"start":{"row":162,"column":40},"end":{"row":162,"column":41},"action":"insert","lines":["e"]},{"start":{"row":162,"column":41},"end":{"row":162,"column":42},"action":"insert","lines":["t"]},{"start":{"row":162,"column":42},"end":{"row":162,"column":43},"action":"insert","lines":["h"]},{"start":{"row":162,"column":43},"end":{"row":162,"column":44},"action":"insert","lines":["o"]}],[{"start":{"row":162,"column":44},"end":{"row":162,"column":45},"action":"insert","lines":["s"],"id":2209}],[{"start":{"row":162,"column":45},"end":{"row":163,"column":0},"action":"insert","lines":["",""],"id":2210}],[{"start":{"row":162,"column":45},"end":{"row":163,"column":0},"action":"remove","lines":["",""],"id":2211},{"start":{"row":162,"column":44},"end":{"row":162,"column":45},"action":"remove","lines":["s"]}],[{"start":{"row":162,"column":44},"end":{"row":162,"column":45},"action":"insert","lines":["d"],"id":2212},{"start":{"row":162,"column":45},"end":{"row":162,"column":46},"action":"insert","lines":["s"]},{"start":{"row":162,"column":46},"end":{"row":162,"column":47},"action":"insert","lines":["="]}],[{"start":{"row":162,"column":47},"end":{"row":162,"column":49},"action":"insert","lines":["[]"],"id":2213}],[{"start":{"row":162,"column":48},"end":{"row":162,"column":49},"action":"insert","lines":["|"],"id":2214}],[{"start":{"row":162,"column":48},"end":{"row":162,"column":49},"action":"remove","lines":["|"],"id":2215}],[{"start":{"row":162,"column":48},"end":{"row":162,"column":50},"action":"insert","lines":["\"\""],"id":2216}],[{"start":{"row":162,"column":49},"end":{"row":162,"column":50},"action":"insert","lines":["P"],"id":2217},{"start":{"row":162,"column":50},"end":{"row":162,"column":51},"action":"insert","lines":["O"]},{"start":{"row":162,"column":51},"end":{"row":162,"column":52},"action":"insert","lines":["S"]},{"start":{"row":162,"column":52},"end":{"row":162,"column":53},"action":"insert","lines":["T"]}],[{"start":{"row":163,"column":27},"end":{"row":164,"column":0},"action":"insert","lines":["",""],"id":2218},{"start":{"row":164,"column":0},"end":{"row":164,"column":4},"action":"insert","lines":["    "]},{"start":{"row":164,"column":4},"end":{"row":164,"column":5},"action":"insert","lines":["p"]},{"start":{"row":164,"column":5},"end":{"row":164,"column":6},"action":"insert","lines":["r"]},{"start":{"row":164,"column":6},"end":{"row":164,"column":7},"action":"insert","lines":["i"]},{"start":{"row":164,"column":7},"end":{"row":164,"column":8},"action":"insert","lines":["n"]},{"start":{"row":164,"column":8},"end":{"row":164,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":164,"column":9},"end":{"row":164,"column":11},"action":"insert","lines":["()"],"id":2219}],[{"start":{"row":164,"column":10},"end":{"row":164,"column":12},"action":"insert","lines":["\"\""],"id":2220}],[{"start":{"row":164,"column":11},"end":{"row":164,"column":12},"action":"insert","lines":["o"],"id":2221},{"start":{"row":164,"column":12},"end":{"row":164,"column":13},"action":"insert","lines":["o"]},{"start":{"row":164,"column":13},"end":{"row":164,"column":14},"action":"insert","lines":["p"]},{"start":{"row":164,"column":14},"end":{"row":164,"column":15},"action":"insert","lines":["s"]},{"start":{"row":164,"column":15},"end":{"row":164,"column":16},"action":"insert","lines":["i"]},{"start":{"row":164,"column":16},"end":{"row":164,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":156,"column":0},"end":{"row":157,"column":0},"action":"insert","lines":["    print(\"oopsie\")",""],"id":2222}],[{"start":{"row":156,"column":11},"end":{"row":156,"column":17},"action":"remove","lines":["oopsie"],"id":2223},{"start":{"row":156,"column":11},"end":{"row":156,"column":12},"action":"insert","lines":["w"]},{"start":{"row":156,"column":12},"end":{"row":156,"column":13},"action":"insert","lines":["h"]},{"start":{"row":156,"column":13},"end":{"row":156,"column":14},"action":"insert","lines":["a"]},{"start":{"row":156,"column":14},"end":{"row":156,"column":15},"action":"insert","lines":["p"]},{"start":{"row":156,"column":15},"end":{"row":156,"column":16},"action":"insert","lines":["s"]},{"start":{"row":156,"column":16},"end":{"row":156,"column":17},"action":"insert","lines":["i"]},{"start":{"row":156,"column":17},"end":{"row":156,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":163,"column":49},"end":{"row":163,"column":53},"action":"remove","lines":["POST"],"id":2224},{"start":{"row":163,"column":49},"end":{"row":163,"column":50},"action":"insert","lines":["D"]},{"start":{"row":163,"column":50},"end":{"row":163,"column":51},"action":"insert","lines":["E"]},{"start":{"row":163,"column":51},"end":{"row":163,"column":52},"action":"insert","lines":["L"]},{"start":{"row":163,"column":52},"end":{"row":163,"column":53},"action":"insert","lines":["E"]},{"start":{"row":163,"column":53},"end":{"row":163,"column":54},"action":"insert","lines":["T"]},{"start":{"row":163,"column":54},"end":{"row":163,"column":55},"action":"insert","lines":["E"]}],[{"start":{"row":163,"column":37},"end":{"row":163,"column":57},"action":"remove","lines":[", methods=[\"DELETE\"]"],"id":2225}]]},"ace":{"folds":[],"scrolltop":2175,"scrollleft":0,"selection":{"start":{"row":163,"column":37},"end":{"row":163,"column":37},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1581369774039,"hash":"c9c32a3fdf8e1e8d4273a2f28702e4dd700d5a3b"}