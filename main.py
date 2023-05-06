from flask import Flask, render_template, request
from selectorPresuntivo import *
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

def strToBool(s):
  return s.lower() in ("True", "true")

@app.route('/run')
def runSelectorBootcamp():
  conocimiento_lenguaje_arg = request.args.get('conocimiento_lenguaje')
  conocimiento_arquitectura_arg = request.args.get('conocimiento_arquitectura')
  trabajo_equipo_arg = request.args.get('trabajo_equipo')
  solucion_problemas_arg = request.args.get('solucion_problemas')
  calidad_codigo_arg = request.args.get('calidad_codigo')
  participacion_reuniones_arg = request.args.get('participacion_reuniones')
  uso_tecnologias_arg = request.args.get('uso_tecnologias')
  anios_experiencia_arg = request.args.get('anios_experiencia')
  seniority_arg = request.args.get('seniority')

  engine = SelectorPresuntivo()
  engine.reset()
  selector_bootcamp = SelectorBootcamp(
    conocimiento_lenguaje = conocimiento_lenguaje_arg,
    conocimiento_arquitectura = conocimiento_arquitectura_arg,
    trabajo_equipo = trabajo_equipo_arg,
    solucion_problemas = solucion_problemas_arg,
    calidad_codigo = calidad_codigo_arg,
    participacion_reuniones = strToBool(participacion_reuniones_arg),
    uso_tecnologias = uso_tecnologias_arg,
    anios_experiencia = anios_experiencia_arg,
    seniority = seniority_arg
  )
  engine.declare(selector_bootcamp)
  engine.run()
  return render_template("response.html", result = engine.response)

if __name__ == '__main__':
   app.run(debug = True)
