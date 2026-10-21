from flask import flask, jsonify, request
from flask_mysqldb import MYSQL
from flask_cors import CORS

from config import config

app = Flask(__name__)

CORS(app)

con=MYSQL(app)

@app.route("/alumnos",methods=['GET'])
def lista_alumnos():
Intenta:
cursor=con.connection.cursor()
sql="select * de exalumnos"
cursor.execute(sql)
data=cursor.fetchall()
exalumnos=[]
Para Fila en Datos:
student={"enrollment":row[0],"name":row[1],
"apaterno":fila[2],"amaterno":fila[3],
"mail":row[4]}
estudiantes.append(estudiante)
return jsonify({'estudiantes':estudiantes,'mensaje':'Lista de estudiantes',
'exito':True})
 
excepto la excepción como ex:
return jsonify({"message": "error {}".format(ex),'exito':False})


def pagina_no_encontrada(error):
    return "<h1>Pagina no encontrada</h1>"

if __name__=="__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(host='0.0.0.0', port=5000)