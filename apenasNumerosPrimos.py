import os 
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def numerosPrimos():
    c = 1
    p = 1
    numero = 3
    nrprimos = '2,'

    while p < 100:
        eprimo = 1
        for i in range(2, numero):
            if numero % i == 0:
                eprimo = 0
                break
        if (eprimo):
            nrprimos = nrprimos + str(numero) + ','
            p += 1
        numero += 1
    return nrprimos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3333))
    app.run(host='0.0.0.0', port=port)