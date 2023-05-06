from random import choice
from experta import *

class SelectorBootcamp(Fact):
	pass

class SelectorPresuntivo(KnowledgeEngine):
	def __init__(self):
		super().__init__()
		self.response = "No se puede determinar la respuesta con los datos de entrada. Asesorar con un experto."

	@Rule(SelectorBootcamp(conocimiento_lenguaje = "REGULAR"))
	def NoContratadoPorLenguaje(self):
		self.response = "No contratado. El personal no dispone de conocimiento suficiente sobre lenguajes de programación."

	@Rule(SelectorBootcamp(trabajo_equipo = "REGULAR"))
	def NoContratadoPorTrabajoEquipo(self):
		self.response = "No contratado. El personal no dispone de conocimiento suficiente sobre trabajo en equipo."

	@Rule(SelectorBootcamp(solucion_problemas = "REGULAR"))
	def NoContratadoPorSolucionProblemas(self):
		self.response = "No contratado. El personal no dispone de conocimiento suficiente para resolver problemas de código."

	@Rule(SelectorBootcamp(calidad_codigo = "REGULAR"))
	def NoContratadoPorCalidadCodigo(self):
		self.response = "No contratado. El personal no dispone de conocimiento suficiente para desarrollar un código de buena calidad."

	@Rule(SelectorBootcamp(
		conocimiento_lenguaje = "EXCELENTE",
		conocimiento_arquitectura = "EXCELENTE",
		trabajo_equipo = "EXCELENTE",
		solucion_problemas = "EXCELENTE",
		calidad_codigo = "EXCELENTE",
		participacion_reuniones = True,
		uso_tecnologias = "EXCELENTE",
		anios_experiencia = "MAS3"
		)
	)
	def ContratadoParaSenior(self):
		self.response  = "Contratado. El personal no tiene necesidad de acceder al bootcamp dado que dispone de los conocimientos necesarios para acceder a uno de los equipos de proyecto."

	@Rule(
		OR(
			SelectorBootcamp(
				conocimiento_lenguaje = "EXCELENTE",
				conocimiento_arquitectura = "BUENO",
				trabajo_equipo = L("EXCELENTE") | L("BUENO"),
				solucion_problemas = L("EXCELENTE") | L("BUENO"),
				calidad_codigo = "EXCELENTE",
				participacion_reuniones = True,
				uso_tecnologias = L("EXCELENTE") | L("BUENO"),
				anios_experiencia = L("MAS3") | L("2"),
				seniority = "SEMISENIOR"
			),
			SelectorBootcamp(
				conocimiento_lenguaje = "EXCELENTE",
				conocimiento_arquitectura = L("EXCELENTE") | L("BUENO"),
				trabajo_equipo = "BUENO",
				solucion_problemas = L("EXCELENTE") | L("BUENO"),
				calidad_codigo = "EXCELENTE",
				participacion_reuniones = True,
				uso_tecnologias = L("EXCELENTE") | L("BUENO"),
				anios_experiencia = L("MAS3") | L("2"),
				seniority = "SEMISENIOR"
			),
			SelectorBootcamp(
				conocimiento_lenguaje = "EXCELENTE",
				conocimiento_arquitectura = L("EXCELENTE") | L("BUENO"),
				trabajo_equipo = L("EXCELENTE") | L("BUENO"),
				solucion_problemas = "BUENO",
				calidad_codigo = "EXCELENTE",
				participacion_reuniones = True,
				uso_tecnologias = L("EXCELENTE") | L("BUENO"),
				anios_experiencia = L("MAS3") | L("2"),
				seniority = "SEMISENIOR"
			),
			SelectorBootcamp(
				conocimiento_lenguaje = "EXCELENTE",
				conocimiento_arquitectura = L("EXCELENTE") | L("BUENO"),
				trabajo_equipo = L("EXCELENTE") | L("BUENO"),
				solucion_problemas = L("EXCELENTE") | L("BUENO"),
				calidad_codigo = "EXCELENTE",
				participacion_reuniones = True,
				uso_tecnologias = "BUENO",
				anios_experiencia = L("MAS3") | L("2"),
				seniority = "SEMISENIOR"
			),
			SelectorBootcamp(
				conocimiento_lenguaje = "EXCELENTE",
				conocimiento_arquitectura = L("EXCELENTE") | L("BUENO"),
				trabajo_equipo = L("EXCELENTE") | L("BUENO"),
				solucion_problemas = L("EXCELENTE") | L("BUENO"),
				calidad_codigo = "EXCELENTE",
				participacion_reuniones = True,
				uso_tecnologias = L("EXCELENTE") | L("BUENO"),
				anios_experiencia = "2",
				seniority = "SEMISENIOR"
			)
		)
	)
	def ContratadoParaSemiSenior(self):
		self.response  = "Contratado. El personal dispone de los conocimientos necesarios para acceder al bootcamp de semiseniors."

	@Rule(
		OR(
			SelectorBootcamp(
				conocimiento_lenguaje = "EXCELENTE",
				conocimiento_arquitectura = "BUENO",
				trabajo_equipo = L("EXCELENTE") | L("BUENO"),
				solucion_problemas = L("EXCELENTE") | L("BUENO"),
				calidad_codigo = "EXCELENTE",
				participacion_reuniones = True,
				uso_tecnologias = L("EXCELENTE") | L("BUENO"),
				anios_experiencia = L("MAS3") | L("2"),
				seniority = "JUNIOR"
			),
			SelectorBootcamp(
				conocimiento_lenguaje = "EXCELENTE",
				conocimiento_arquitectura = L("EXCELENTE") | L("BUENO"),
				trabajo_equipo = "BUENO",
				solucion_problemas = L("EXCELENTE") | L("BUENO"),
				calidad_codigo = "EXCELENTE",
				participacion_reuniones = True,
				uso_tecnologias = L("EXCELENTE") | L("BUENO"),
				anios_experiencia = L("MAS3") | L("2"),
				seniority = "JUNIOR"
			),
			SelectorBootcamp(
				conocimiento_lenguaje = "EXCELENTE",
				conocimiento_arquitectura = L("EXCELENTE") | L("BUENO"),
				trabajo_equipo = L("EXCELENTE") | L("BUENO"),
				solucion_problemas = "BUENO",
				calidad_codigo = "EXCELENTE",
				participacion_reuniones = True,
				uso_tecnologias = L("EXCELENTE") | L("BUENO"),
				anios_experiencia = L("MAS3") | L("2"),
				seniority = "JUNIOR"
			),
			SelectorBootcamp(
				conocimiento_lenguaje = "EXCELENTE",
				conocimiento_arquitectura = L("EXCELENTE") | L("BUENO"),
				trabajo_equipo = L("EXCELENTE") | L("BUENO"),
				solucion_problemas = L("EXCELENTE") | L("BUENO"),
				calidad_codigo = "EXCELENTE",
				participacion_reuniones = True,
				uso_tecnologias = "BUENO",
				anios_experiencia = L("MAS3") | L("2"),
				seniority = "JUNIOR"
			),
			SelectorBootcamp(
				conocimiento_lenguaje = "EXCELENTE",
				conocimiento_arquitectura = L("EXCELENTE") | L("BUENO"),
				trabajo_equipo = L("EXCELENTE") | L("BUENO"),
				solucion_problemas = L("EXCELENTE") | L("BUENO"),
				calidad_codigo = "EXCELENTE",
				participacion_reuniones = True,
				uso_tecnologias = L("EXCELENTE") | L("BUENO"),
				anios_experiencia = "2",
				seniority = "JUNIOR"
			)
		)
	)
	def ContratadoParaSemiSeniorConCambio(self):
		self.response  = "Contratado. El personal dispone de conocimientos más experimentados que los requeridos para junior. Es necesario derivarlo a un bootcamp para semiseniors."

	@Rule(
		OR(
			SelectorBootcamp(
				conocimiento_lenguaje = L("EXCELENTE") | L("BUENO"),
				trabajo_equipo = L("EXCELENTE") | L("BUENO"),
				solucion_problemas = L("EXCELENTE") | L("BUENO"),
				calidad_codigo = L("EXCELENTE") | L("BUENO"),
				anios_experiencia = "MENOR1",
				seniority = "JUNIOR"
			),
			SelectorBootcamp(
				conocimiento_lenguaje = L("EXCELENTE") | L("BUENO"),
				trabajo_equipo = L("EXCELENTE") | L("BUENO"),
				solucion_problemas = L("EXCELENTE") | L("BUENO"),
				calidad_codigo = L("EXCELENTE") | L("BUENO"),
				anios_experiencia = "1",
				seniority = "JUNIOR"
			),
			SelectorBootcamp(
				conocimiento_lenguaje=L("EXCELENTE") | L("BUENO"),
				trabajo_equipo=L("EXCELENTE") | L("BUENO"),
				solucion_problemas=L("EXCELENTE") | L("BUENO"),
				calidad_codigo=L("EXCELENTE") | L("BUENO"),
				anios_experiencia="2",
				seniority="JUNIOR"
			)
		)
	)
	def ContratadoParaJunior(self):
		self.response  = "Contratado. El personal dispone de los conocimientos necesarios para acceder al bootcamp de juniors."

	@Rule(
		OR(
			SelectorBootcamp(
				conocimiento_lenguaje = L("EXCELENTE") | L("BUENO"),
				trabajo_equipo = L("EXCELENTE") | L("BUENO"),
				solucion_problemas = L("EXCELENTE") | L("BUENO"),
				calidad_codigo = L("EXCELENTE") | L("BUENO"),
				anios_experiencia = "MENOR1",
				seniority = "SEMISENIOR"
			),
			SelectorBootcamp(
				conocimiento_lenguaje = L("EXCELENTE") | L("BUENO"),
				trabajo_equipo = L("EXCELENTE") | L("BUENO"),
				solucion_problemas = L("EXCELENTE") | L("BUENO"),
				calidad_codigo = L("EXCELENTE") | L("BUENO"),
				anios_experiencia = "1",
				seniority = "SEMISENIOR"
			),
			SelectorBootcamp(
				conocimiento_lenguaje = L("EXCELENTE") | L("BUENO"),
				trabajo_equipo = L("EXCELENTE") | L("BUENO"),
				solucion_problemas = L("EXCELENTE") | L("BUENO"),
				calidad_codigo = L("EXCELENTE") | L("BUENO"),
				anios_experiencia = "2",
				seniority = "SEMISENIOR"
			)
		)
	)
	def ContratadoParaJuniorConCambio(self):
		self.response  = "Contratado. El personal no dispone de conocimientos suficientes para semisenior. Es necesario derivarlo a un bootcamp para juniors."
