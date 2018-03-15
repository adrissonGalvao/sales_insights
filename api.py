from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
from flask import Response
import service as serv

app = Flask(__name__)
service = serv.Service()
@app.route("/")
def hello():
    return "Hello World!" 

@app.route("/product/<product>")
def product_handler(product):
    if product==None:
        abort(400, 'INVALID PARAMETERS')
    
    result = service.product_more_sale_country(product)  	
    return  result

@app.route("/client/")
def best_client():
    result = service.best_client()

    return result

@app.route("/product/price/<product>")
def price_max_and_min(product):
    if product==None:
        abort(400, 'INVALID PARAMETERS')
    result = service.price_max_and_min(product)
    return result

@app.route("/product/percentage/<product>")
def percentage_product(product):
    if product==None:
        abort(400, 'INVALID PARAMETERS')
    result = service.percentage_product(product)
    return result
if __name__ == "__main__":
    app.run()
