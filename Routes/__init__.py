from Routes.RolRoute import rol_bp
from Routes.PersonaRoute import persona_bp
from Routes.DocenteRoute import docente_bp
from Routes.EstudianteRoute import estudiante_bp
from Routes.MatriculaRoute import matricula_bp
from Routes.AcudienteRoute import acudiente_bp
from Routes.AcudienteCorreoRoute import acudiente_correo_bp
from Routes.AcudienteTelefonoRoute import acudiente_telefono_bp
from Routes.AcudienteEstudianteRoute import acudiente_estudiante_bp
from Routes.MateriaRoute import materia_bp
from Routes.DiaSemanaRoute import dia_semana_bp
from Routes.NivelEducativoRoute import nivel_educativo_bp
from Routes.GradoRoute import grado_bp
from Routes.CursoVigenciaRoute import curso_vigencia_bp
from Routes.VigenciaRoute import vigencia_bp
from Routes.PeriodoAcademicoRoute import periodo_academico_bp
from Routes.AsignacionAcademicaRoute import asignacion_academica_bp
from Routes.TipoComponenteRoute import tipo_componente_bp
from Routes.ComponenteEvaluativoRoute import componente_evaluativo_bp
from Routes.ActividadEvaluativaRoute import actividad_evaluativa_bp
from Routes.ResultadoEvaluativoRoute import resultado_evaluativo_bp
from Routes.DetalleHorarioRoute import detalle_horario_bp


def CargarRutas(app):
    app.register_blueprint(rol_bp)
    app.register_blueprint(persona_bp)
    app.register_blueprint(docente_bp)
    app.register_blueprint(estudiante_bp)
    app.register_blueprint(matricula_bp)
    app.register_blueprint(acudiente_bp)
    app.register_blueprint(acudiente_correo_bp)
    app.register_blueprint(acudiente_telefono_bp)
    app.register_blueprint(acudiente_estudiante_bp)
    app.register_blueprint(materia_bp)
    app.register_blueprint(dia_semana_bp)
    app.register_blueprint(nivel_educativo_bp)
    app.register_blueprint(grado_bp)
    app.register_blueprint(curso_vigencia_bp)
    app.register_blueprint(vigencia_bp)
    app.register_blueprint(periodo_academico_bp)
    app.register_blueprint(asignacion_academica_bp)
    app.register_blueprint(tipo_componente_bp)
    app.register_blueprint(componente_evaluativo_bp)
    app.register_blueprint(actividad_evaluativa_bp)
    app.register_blueprint(resultado_evaluativo_bp)
    app.register_blueprint(detalle_horario_bp)
