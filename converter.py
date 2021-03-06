import urllib, csv , operator
urls = [
"https://raw.github.com/ossenegal/ossenegal.github.io/master/survey/2012.csv"
]
def run(url):
    r = urllib.urlopen(url)
    reader = csv.DictReader(r, dialect=csv.excel,
                            delimiter=",")
    out ={}
    for dic in reader:
      print dic
      for key in dic.keys() :
        try:
            x = float(dic[key])
        except (ValueError ,TypeError):
            continue
        if key in out:
            out[key] = float(out[key]) + float(dic[key])
        else:
            out[key] = float(dic[key])
    total = sum(out.values())
    for  key, val in out.items():
        out[key]= (out[key] /total)*100
    out = sorted(out.iteritems(), key=operator.itemgetter(1),
                 reverse=True)
    js_data = "\
\n{\
\n annee: " + "\"%s\"" % url.split('/')[-1].replace(".csv", "")       + ", \
\n data : [" +  ",".join(["\"%s\"" % str(x) for x, y in out]) + "],\
\n value: [" +  ",".join([str(y) for x, y in out ]) + "]\
\n }\
"
    return js_data

def runs():
    js_data = "var Annees = ["
    for url in urls:
        js_data  += run(url)
    #
    
    js_data += "]"
    open("js/catalog.js", "wb").write(js_data)
        
if __name__== "__main__":
  runs()
  



    
    
  
