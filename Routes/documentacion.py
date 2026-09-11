from flask import Blueprint, render_template_string, send_from_directory

documentacion_bp = Blueprint('documentacion', __name__)


@documentacion_bp.route('/swagger.json')
def swagger_json():
    # Entrega la especificación OpenAPI que consume la interfaz de Swagger.
    return send_from_directory('.', 'swagger.json')


@documentacion_bp.route('/documentacion')
def swagger_ui():
    # La documentación ya no vive en la raíz "/" sino en "/documentacion".
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>Gestión Académica CMM - Documentación de la API</title>
      <link rel="stylesheet" href="/static/swagger-ui/swagger-ui.css" />
      <style>
        body { margin: 0; background: #fafafa; }
        .swagger-ui .topbar { background-color: #1b5e20; }
      </style>
    </head>
    <body>
      <div id="swagger-ui"></div>

      <script src="/static/swagger-ui/swagger-ui-bundle.js"></script>
      <script src="/static/swagger-ui/swagger-ui-standalone-preset.js"></script>
      <script>
        window.onload = function () {
          window.ui = SwaggerUIBundle({
            // La especificación se sirve desde el mismo servidor.
            url: "/swagger.json",
            dom_id: "#swagger-ui",
            // Layout con barra superior y selector de servidor.
            presets: [
              SwaggerUIBundle.presets.apis,
              SwaggerUIStandalonePreset
            ],
            plugins: [
              SwaggerUIBundle.plugins.DownloadUrl
            ],
            layout: "StandaloneLayout",
            // Permite probar los endpoints directamente contra la base de datos.
            tryItOutEnabled: true,
            // Muestra el buscador para filtrar endpoints por nombre.
            filter: true,
            // Abre los endpoints colapsados para una navegación más limpia.
            docExpansion: "none",
            defaultModelsExpandDepth: 1,
            displayRequestDuration: true,
            persistAuthorization: true,
            deepLinking: true,
            syntaxHighlight: { activate: true, theme: "agate" }
          });
        };
      </script>
    </body>
    </html>
    """)
