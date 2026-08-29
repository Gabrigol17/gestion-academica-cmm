from flask import Flask


from Controllers.ActividadEvaluativaController import actividad_bp
from Controllers.AcudienteCorreoController import acudiente_correo_bp
from Controllers.AcudienteEstudianteController import acudiente_estudiante_bp
from Controllers.AcudienteController import acudiente_bp
from Controllers.AcudienteTelefonoController import acudiente_telefono_bp
from Controllers.AsignacionAcademicaController import asignacion_bp
from Controllers.ComponenteEvaluativoController import componente_bp
from Controllers.CursoController import curso_bp
from Controllers.CursoVigenciaController import curso_vigencia_bp
from Controllers.DetalleHorarioController import detalle_horario_bp
from Controllers.DiaSemanaController import dia_semana_bp
from Controllers.DocenteController import docente_bp
from Controllers.EstudianteController import estudiante_bp
from Controllers.GradoController import grado_bp
from Controllers.MateriaController import materia_bp
from Controllers.MatriculaController import matricula_bp
from Controllers.NivelEducativoController import nivel_educativo_bp
from Controllers.PeriodoAcademicoController import periodo_academico_bp
from Controllers.PersonaController import persona_bp
from Controllers.ResultadoEvaluativoController import resultado_evaluativo_bp
from Controllers.RolController import rol_bp
from Controllers.TipoComponenteController import tipo_componente_bp
from Controllers.VigenciaController import vigencia_bp

app = Flask(__name__)


blueprints = [
    actividad_bp, acudiente_correo_bp, acudiente_estudiante_bp, acudiente_bp,
    acudiente_telefono_bp, asignacion_bp, componente_bp, curso_bp,
    curso_vigencia_bp, detalle_horario_bp, dia_semana_bp, docente_bp,
    estudiante_bp, grado_bp, materia_bp, matricula_bp, nivel_educativo_bp,
    periodo_academico_bp, persona_bp, resultado_evaluativo_bp, rol_bp,
    tipo_componente_bp, vigencia_bp
]

for bp in blueprints:
    app.register_blueprint(bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)