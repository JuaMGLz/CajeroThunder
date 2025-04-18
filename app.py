from flask import Flask, render_template_string, send_from_directory
import os
from flask import request, jsonify
from bson.decimal128 import Decimal128
from conexion import obtener_conexion
from datetime import datetime
from bson.decimal128 import Decimal128
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


app = Flask(__name__)

# Ruta manual para servir imágenes desde carpeta "Imagenes"
@app.route('/Imagenes/<filename>')
def imagenes(filename):
    return send_from_directory(os.path.join(app.root_path, 'Imagenes'), filename)

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Cajero Thunder</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://unpkg.com/html5-qrcode" type="text/javascript"></script>
        <!-- ========== SECCIÓN CSS ========== -->
        <style>
            * {
                box-sizing: border-box;
            }

            html, body {
                margin: 0;
                padding: 0;
                font-family: 'Times New Roman', Times, serif;
                height: 100%;
                background: linear-gradient(135deg, #2e003e, #1a001f, #3b003b);
                background-size: 400% 400%;
                animation: fondoAnimado 15s ease infinite;
                color: white;
                display: flex;
                flex-direction: column;
            }

            @keyframes fondoAnimado {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            /* ========== BARRA DE NAVEGACIÓN ========== */
            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: rgba(0, 0, 0, 0.5);
                padding: 20px 40px;
                height: 100px;
            }

            .navbar img {
                height: 70px;
            }

            .navbar h1 {
                margin: 0;
                font-size: 2.5rem;
                color: #fff;
            }

            .nav-buttons {
                display: flex;
                gap: 15px;
            }

            .nav-buttons button {
                background-color: #6a0dad;
                color: #fff;
                border: none;
                padding: 10px 18px;
                font-size: 1rem;
                border-radius: 5px;
                cursor: pointer;
                opacity: 1;
            }

            .nav-buttons button[disabled] {
                background-color: #444;
                cursor: not-allowed;
                opacity: 0.5;
            }

            /* ========== BOTONES CENTRALES ========== */
            .main {
                flex: 1;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 30px 0;
            }

            .main-buttons {
                display: flex;
                gap: 60px;
                flex-wrap: wrap;
                justify-content: center;
            }

            .boton-personalizado {
                background-color: #6a0dad;
                color: #fff;
                border: none;
                padding: 15px 20px;
                width: 600px;  /* MÁS ANCHO */
                height: 280px; /* MÁS ALTO */
                font-size: 3.3rem;
                border-radius: 12px;
                cursor: pointer;
                transition: background 0.3s;
                display: flex;
                align-items: center;
                gap: 20px;
            }

            .boton-personalizado img {
                width: 200px;
                height: 200px;
            }

            .boton-personalizado:hover {
                background-color: #580c8c;
            }

            /* ========== PIE DE PÁGINA ========== */
            footer {
                background-color: rgba(0, 0, 0, 0.4);
                text-align: center;
                padding: 20px;
                font-size: 2.2rem;
            }

            @media (max-width: 768px) {
                .boton-personalizado {
                    width: 90%;
                    height: 160px;
                    font-size: 1rem;
                    flex-direction: column;
                    gap: 10px;
                }

                .boton-personalizado img {
                    width: 70px;
                    height: 70px;
                }
            }
        </style>
    </head>
    <body>

        <!-- ========== SECCIÓN HTML ========== -->

        <!-- Barra de navegación superior -->
        <div class="navbar">
            <img src="/Imagenes/Logo.jpeg" alt="Logo Empresa">
            <h1>Cajero Thunder</h1>
            <div class="nav-buttons">
                <a href="/ayuda"><button>Ayuda</button></a>
                <button disabled>Volver</button>
            </div>
        </div>

        <!-- Botones principales -->
        <div class="main">
            <div class="main-buttons">
                <button class="boton-personalizado" onclick="window.location.href='/escanear'">
                    <img src="/Imagenes/qr.png" alt="QR">
                    <span>Escanear QR</span>
                </button>
                <button class="boton-personalizado" onclick="window.location.href='/retiro_sin_tarjeta'">
                    <img src="/Imagenes/noTarjeta.png" alt="Sin tarjeta">
                    <span>Retiro sin tarjeta</span>
                </button>
            </div>
        </div>

        <!-- Pie de página -->
        <footer>
            <span id="fechaHora"></span>
        </footer>

        <!-- ========== SECCIÓN JAVASCRIPT ========== -->
        <script>
            function actualizarFechaHora() {
                const ahora = new Date();
                const fecha = ahora.toLocaleDateString();
                const hora = ahora.toLocaleTimeString();
                document.getElementById('fechaHora').textContent = `Fecha y hora: ${fecha} ${hora}`;
            }

            setInterval(actualizarFechaHora, 1000);
            actualizarFechaHora();
        </script>
    </body>
    </html>
    """
    return render_template_string(html)


# Ruta de AYUDA
@app.route('/ayuda')
def ayuda():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Ayuda - Cajero Thunder</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://unpkg.com/html5-qrcode" type="text/javascript"></script>
        <!-- ========== SECCIÓN CSS ========== -->
        <style>
            body {
                margin: 0;
                font-family: 'Times New Roman', Times, serif;
                background: linear-gradient(135deg, #2e003e, #1a001f, #3b003b);
                background-size: 400% 400%;
                animation: fondoAnimado 15s ease infinite;
                color: white;
                display: flex;
                flex-direction: column;
                height: 100vh;
            }

            @keyframes fondoAnimado {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: rgba(0, 0, 0, 0.5);
                padding: 20px 40px;
                height: 100px;
            }

            .navbar img {
                height: 70px;
            }

            .navbar h1 {
                margin: 0;
                font-size: 2.5rem;
                color: #fff;
            }

            .nav-buttons {
                display: flex;
                gap: 15px;
            }

            .nav-buttons a button {
                background-color: #6a0dad;
                color: #fff;
                border: none;
                padding: 10px 18px;
                font-size: 1rem;
                border-radius: 5px;
                cursor: pointer;
            }

            .main {
                flex: 1;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 40px 0;
            }
            .main-content {
                display: flex;
                flex-direction: row;
                align-items: flex-start;
                justify-content: center;
                gap: 100px;
                max-width: 1200px;
                width: 100%;
                padding: 0 60px;
            }

            .instrucciones {
                flex: 1;
                max-width: 600px;
                font-size: 2.2rem;
                text-align: justify;
            }

            .ayuda-btn {
                flex: 1;
                max-width: 220px;
                display: flex;
                justify-content: center;
                margin-top: 200px;     /* Más abajo */
                margin-left: 30px;    /* Más a la derecha */
            }

            .boton-asistencia {
                background-color: #00b894;
                color: white;
                padding: 20px;
                border-radius: 12px;
                font-size: 2.2rem;
                text-decoration: none;
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 10px;
                width: 250px;
            }

            .boton-asistencia img {
                width: 100px;
                height: 100px;
                display: block;
                margin: 0 auto;
            }

            footer {
                background-color: rgba(0, 0, 0, 0.4);
                text-align: center;
                padding: 20px;
                font-size: 1.2rem;
            }
        </style>
    </head>
    <body>

        <!-- ========== SECCIÓN HTML ========== -->

        <!-- Barra de navegación -->
        <div class="navbar">
            <img src="/Imagenes/Logo.jpeg" alt="Logo Empresa">
            <h1>Cajero Thunder</h1>
            <div class="nav-buttons">
                <a href="/"><button>Volver</button></a>
            </div>
        </div>

        <!-- Cuerpo dividido en dos columnas -->
            <div class="main">
                <div class="main-content">
                    <!-- Columna izquierda: Instrucciones -->
                    <div class="instrucciones">
                        <h2>Instrucciones</h2>
                        <p>• Si desea realizar un retiro desde su tarjeta, por favor presione el botón <strong>Escanear QR</strong> en la pantalla principal y muestre el código QR de su tarjeta en la cámara.</p>
                        <p>• Si desea realizar un retiro sin tarjeta, seleccione la opción correspondiente e ingrese su <strong>número de cuenta</strong> y <strong>NIP</strong> de forma segura.</p>
                    </div>

                    <!-- Columna derecha: Botón de ayuda -->
                    <div class="ayuda-btn">
                        <a href="https://wa.me/5215576315553?text=Hola,%20solicito%20asistencia%20en%20el%20cajero." target="_blank" class="boton-asistencia">
                            <img src="/Imagenes/asistente.png" alt="Asistente">
                            <div>Llamar a un empleado</div>
                        </a>
                    </div>
                </div>
            </div>

        <!-- Pie de página -->
        <footer>
            <span id="fechaHora"></span>
        </footer>

        <!-- ========== SECCIÓN JAVASCRIPT ========== -->
        <script>
            function actualizarFechaHora() {
                const ahora = new Date();
                const fecha = ahora.toLocaleDateString();
                const hora = ahora.toLocaleTimeString();
                document.getElementById('fechaHora').textContent = `Fecha y hora: ${fecha} ${hora}`;
            }

            setInterval(actualizarFechaHora, 1000);
            actualizarFechaHora();
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/escanear')
def escanear():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Escanear QR</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://unpkg.com/html5-qrcode" type="text/javascript"></script>
        <style>
            body {
                margin: 0;
                font-family: 'Times New Roman', Times, serif;
                background: linear-gradient(135deg, #2e003e, #1a001f, #3b003b);
                background-size: 400% 400%;
                animation: fondoAnimado 15s ease infinite;
                color: white;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
            }

            @keyframes fondoAnimado {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: rgba(0, 0, 0, 0.5);
                padding: 20px 40px;
                height: 100px;
            }

            .navbar img {
                height: 70px;
            }

            .navbar h1 {
                margin: 0 auto;
                font-size: 2.5rem;
                color: #fff;
            }

            .nav-buttons {
                display: flex;
                gap: 15px;
            }

            .nav-buttons a button {
                background-color: #6a0dad;
                color: #fff;
                border: none;
                padding: 10px 18px;
                font-size: 1rem;
                border-radius: 5px;
                cursor: pointer;
            }

            #reader {
                width: 400px;
                margin: 40px auto;
            }

            #mensaje {
                text-align: center;
                font-size: 1.5rem;
                padding: 10px;
            }

            footer {
                background-color: rgba(0, 0, 0, 0.4);
                text-align: center;
                padding: 20px;
                font-size: 1.2rem;
                margin-top: auto;
            }
        </style>
    </head>
    <body>
        <!-- Barra de navegación -->
        <div class="navbar">
            <img src="/Imagenes/Logo.jpeg" alt="Logo Empresa">
            <h1>Cajero Thunder</h1>
            <div class="nav-buttons">
                <a href="/"><button>Volver</button></a>
                <a href="/ayuda"><button>Ayuda</button></a>
            </div>
        </div>

        <div id="reader"></div>
        <p id="mensaje">Escanea tu código QR...</p>

        <footer>
            <span id="fechaHora"></span>
        </footer>

        <script>
            function actualizarFechaHora() {
                const ahora = new Date();
                const fecha = ahora.toLocaleDateString();
                const hora = ahora.toLocaleTimeString();
                document.getElementById('fechaHora').textContent = `Fecha y hora: ${fecha} ${hora}`;
            }

            setInterval(actualizarFechaHora, 1000);
            actualizarFechaHora();

            function onScanSuccess(decodedText, decodedResult) {
                console.log("Texto leído del QR:", decodedText);
                document.getElementById("mensaje").textContent = "Cuenta detectada, redirigiendo para validar NIP...";

                fetch('/verificar_qr', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ cuenta: decodedText })
                })
                .then(res => res.json())
                .then(data => {
                    if (data.ok) {
                        setTimeout(() => window.location.href = "/verificar_nip/" + decodedText, 1000);
                    } else {
                        document.getElementById("mensaje").textContent = "Cuenta no encontrada. Intenta nuevamente.";
                    }
                })
                .catch(err => {
                    console.error("Error:", err);
                    document.getElementById("mensaje").textContent = "Error al verificar cuenta.";
                });
            }

            const html5Qrcode = new Html5Qrcode("reader");
            html5Qrcode.start({ facingMode: "environment" }, { fps: 10, qrbox: 250 }, onScanSuccess);
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/verificar_qr', methods=['POST'])
def verificar_qr():
    try:
        data = request.get_json(force=True)
        cuenta = data.get('cuenta', '').strip()

        print(" Texto escaneado:", cuenta)

        if not cuenta:
            print(" No se recibió cuenta válida.")
            return jsonify({ "ok": False, "error": "Cuenta vacía" }), 400

        db = obtener_conexion()
        if db is None:
            print(" Conexión fallida con MongoDB")
            return jsonify({ "ok": False, "error": "Sin conexión a la base de datos" }), 500

        cuenta_doc = db.cuentas.find_one({ "num_cuenta": cuenta })

        if cuenta_doc:
            print(" Cuenta encontrada:", cuenta_doc)
            return jsonify({ "ok": True })
        else:
            print(" Cuenta no encontrada.")
            return jsonify({ "ok": False })

    except Exception as e:
        print(" Error interno:", str(e))
        return jsonify({ "ok": False, "error": str(e) }), 500


@app.route('/verificar_nip/<cuenta>')
def verificar_nip_qr(cuenta):
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Verificar NIP</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{
                margin: 0;
                font-family: 'Times New Roman', Times, serif;
                background: linear-gradient(135deg, #2e003e, #1a001f, #3b003b);
                color: white;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
            }}

            .navbar {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: rgba(0, 0, 0, 0.5);
                padding: 20px 40px;
                height: 100px;
            }}

            .navbar img {{
                height: 70px;
            }}

            .navbar h1 {{
                margin: 0;
                font-size: 2.5rem;
                color: #fff;
            }}

            .nav-buttons {{
                display: flex;
                gap: 15px;
            }}

            .nav-buttons a button {{
                background-color: #6a0dad;
                color: #fff;
                border: none;
                padding: 10px 18px;
                font-size: 1rem;
                border-radius: 5px;
                cursor: pointer;
            }}

            .formulario {{
                margin: auto;
                background-color: rgba(0, 0, 0, 0.4);
                padding: 30px;
                border-radius: 12px;
                text-align: center;
                width: 300px;
            }}

            .formulario input {{
                padding: 10px;
                margin: 10px;
                font-size: 1.2rem;
                border-radius: 6px;
                border: none;
                width: 100%;
            }}

            .formulario button {{
                margin-top: 20px;
                padding: 10px 25px;
                font-size: 1.2rem;
                background-color: #6a0dad;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                width: 100%;
            }}

            footer {{
                background-color: rgba(0, 0, 0, 0.4);
                text-align: center;
                padding: 20px;
                font-size: 1.2rem;
                margin-top: auto;
            }}
        </style>
    </head>
    <body>
        <div class="navbar">
            <img src="/Imagenes/Logo.jpeg" alt="Logo Empresa">
            <h1>Cajero Thunder</h1>
            <div class="nav-buttons">
                <a href="/"><button>Volver</button></a>
                <a href="/ayuda"><button>Ayuda</button></a>
            </div>
        </div>

        <div class="formulario">
            <h2>Ingrese su NIP</h2>
            <input type="password" id="nip" placeholder="NIP"><br>
            <button onclick="verificarNIP()">Ingresar</button>
            <div id="mensaje"></div>
        </div>

        <footer>
            <span id="fechaHora"></span>
        </footer>

        <script>
            function actualizarFechaHora() {{
                const ahora = new Date();
                const fecha = ahora.toLocaleDateString();
                const hora = ahora.toLocaleTimeString();
                document.getElementById('fechaHora').textContent = `Fecha y hora: ${{fecha}} ${{hora}}`;
            }}
            setInterval(actualizarFechaHora, 1000);
            actualizarFechaHora();

            function verificarNIP() {{
                const nip = document.getElementById("nip").value;
                fetch("/verificar_nip_qr", {{
                    method: "POST",
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ cuenta: "{cuenta}", nip: nip }})
                }})
                .then(res => res.json())
                .then(data => {{
                    if (data.ok) {{
                        window.location.href = "/cuenta/{cuenta}";
                    }} else {{
                        document.getElementById("mensaje").textContent = "❌ NIP incorrecto.";
                    }}
                }});
            }}
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

def generar_pdf_retiro(folio, cuenta, monto, fecha, num_cajero):
    hora_str = fecha.strftime("%H%M%S")  # formato HHMMSS
    archivo = f"ticket_{hora_str}.pdf"
    ruta = os.path.join("comprobantes", archivo)
    os.makedirs("comprobantes", exist_ok=True)

    c = canvas.Canvas(ruta, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Comprobante de Retiro - Cajero Thunder")
    c.setFont("Helvetica", 12)
    c.drawString(100, 720, f"Folio: {folio}")
    c.drawString(100, 700, f"Número de cuenta: {cuenta}")
    c.drawString(100, 680, f"Monto retirado: ${monto}")
    c.drawString(100, 660, f"Número de cajero: {num_cajero}")
    c.drawString(100, 640, f"Fecha y hora: {fecha.strftime('%d/%m/%Y %H:%M:%S')}")
    c.drawString(100, 620, f"Autenticado: Sí")
    c.save()

    return archivo  # retorna el nombre del archivo generado

@app.route('/descargar_comprobante/<archivo>')
def descargar_comprobante(archivo):
    return send_from_directory('comprobantes', archivo, as_attachment=True)



@app.route('/cuenta/<num>')
def cuenta(num):
    db = obtener_conexion()
    cuenta_doc = db.cuentas.find_one({"num_cuenta": num})
    cliente = db.clientes.find_one({"id_cliente": cuenta_doc["id_cliente"]}) if cuenta_doc else None

    if not cuenta_doc or not cliente:
        return "Cuenta no encontrada", 404

    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Cuenta %s</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                margin: 0;
                font-family: 'Times New Roman', Times, serif;
                background: linear-gradient(135deg, #2e003e, #1a001f, #3b003b);
                background-size: 400%% 400%%;
                animation: fondoAnimado 15s ease infinite;
                color: white;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
                text-align: center;
            }

            @keyframes fondoAnimado {
                0%% { background-position: 0%% 50%%; }
                50%% { background-position: 100%% 50%%; }
                100%% { background-position: 0%% 50%%; }
            }

            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: rgba(0, 0, 0, 0.5);
                padding: 20px 40px;
                height: 100px;
            }

            .navbar img {
                height: 70px;
            }

            .navbar h1 {
                margin: 0;
                font-size: 2.5rem;
                color: #fff;
            }

            .nav-buttons {
                display: flex;
                gap: 15px;
            }

            .nav-buttons a button {
                background-color: #6a0dad;
                color: #fff;
                border: none;
                padding: 10px 18px;
                font-size: 1rem;
                border-radius: 5px;
                cursor: pointer;
            }

            h2 {
                font-size: 2.3rem;
                margin-top: 40px;
            }

            h3 {
                font-size: 1.7rem;
                margin-top: 10px;
                margin-bottom: 30px;
            }

            .boton {
                background-color: #6a0dad;
                border: none;
                color: white;
                padding: 15px 25px;
                font-size: 1.2rem;
                border-radius: 8px;
                cursor: pointer;
                margin: 10px;
            }

            footer {
                background-color: rgba(0, 0, 0, 0.4);
                text-align: center;
                padding: 20px;
                font-size: 1.2rem;
                margin-top: auto;
            }
        </style>
    </head>
    <body>
        <div class="navbar">
            <img src="/Imagenes/Logo.jpeg" alt="Logo Empresa">
            <h1>Cajero Thunder</h1>
            <div class="nav-buttons">
                <a href="/"><button>Volver</button></a>
                <a href="/ayuda"><button>Ayuda</button></a>
            </div>
        </div>

        <h2>%s %s %s</h2>
        <h3>Saldo actual: $%s</h3>

        <div>
            <button class="boton" onclick="retirar(100)">Retirar $100</button>
            <button class="boton" onclick="retirar(200)">Retirar $200</button>
            <button class="boton" onclick="retirar(500)">Retirar $500</button>
            <button class="boton" onclick="
                let m = prompt('Monto personalizado:');
                if (m !== null && m.trim() !== '' && !isNaN(m) && parseFloat(m) > 0) {
                    retirar(parseFloat(m));
                } else if (m !== null) {
                    alert('Por favor ingresa un monto válido mayor a 0.');
                }
            ">Otra cantidad</button>
        </div>

        <footer>
            <span id="fechaHora"></span>
        </footer>

        <script>
            function retirar(monto) {
                fetch("/retirar", {
                    method: "POST",
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        cuenta: "%s",
                        monto: monto,
                        num_cajero: 1
                    })
                })
                .then(function(res) { return res.json(); })
                .then(function(data) {
                    if (data.ok) {
                        alert("Retiro exitoso. Nuevo saldo: $" + data.nuevo_saldo);
                        window.open("/descargar_comprobante/" + data.archivo_pdf, "_blank");
                        location.reload();
                    } else {
                        alert("Error: " + data.msg);
                    }
                });
            }

            function actualizarFechaHora() {
                const ahora = new Date();
                const fecha = ahora.toLocaleDateString();
                const hora = ahora.toLocaleTimeString();
                document.getElementById('fechaHora').textContent = "Fecha y hora: " + fecha + " " + hora;
            }

            setInterval(actualizarFechaHora, 1000);
            actualizarFechaHora();
        </script>
    </body>
    </html>
    """ % (
        num,  # título
        cliente["nombre"], cliente["apellido_paterno"], cliente["apellido_materno"],
        cuenta_doc["saldo_actual"],  # saldo
        num  # cuenta para fetch
    )

    return render_template_string(html)

@app.route('/retiro_sin_tarjeta')
def retiro_sin_tarjeta():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Retiro sin Tarjeta</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                margin: 0;
                font-family: 'Times New Roman', Times, serif;
                background: linear-gradient(135deg, #2e003e, #1a001f, #3b003b);
                background-size: 400% 400%;
                animation: fondoAnimado 15s ease infinite;
                color: white;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
            }

            @keyframes fondoAnimado {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: rgba(0,0,0,0.5);
                padding: 20px 40px;
                height: 100px;
            }

            .navbar img {
                height: 70px;
            }

            .navbar h1 {
                margin: 0;
                font-size: 2.5rem;
                color: #fff;
            }

            .nav-buttons {
                display: flex;
                gap: 15px;
            }

            .nav-buttons a button {
                background-color: #6a0dad;
                color: #fff;
                border: none;
                padding: 10px 18px;
                font-size: 1rem;
                border-radius: 5px;
                cursor: pointer;
            }

            .formulario {
                margin: auto;
                background-color: rgba(0, 0, 0, 0.4);
                padding: 30px;
                border-radius: 12px;
                text-align: center;
                width: 300px;
            }

            .formulario input {
                padding: 10px;
                margin: 10px;
                font-size: 1.2rem;
                border-radius: 6px;
                border: none;
                width: 100%;
            }

            .formulario button {
                margin-top: 20px;
                padding: 10px 25px;
                font-size: 1.2rem;
                background-color: #6a0dad;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                width: 100%;
            }

            #mensaje {
                margin-top: 15px;
                font-size: 1.1rem;
                color: red;
            }

            footer {
                background-color: rgba(0, 0, 0, 0.4);
                text-align: center;
                padding: 20px;
                font-size: 1.2rem;
                margin-top: auto;
            }
        </style>
    </head>
    <body>

        <div class="navbar">
            <img src="/Imagenes/Logo.jpeg" alt="Logo Empresa">
            <h1>Cajero Thunder</h1>
            <div class="nav-buttons">
                <a href="/"><button>Volver</button></a>
                <a href="/ayuda"><button>Ayuda</button></a>
            </div>
        </div>

        <div class="formulario">
            <h2>Retiro sin Tarjeta</h2>
            <input type="text" id="cuenta" placeholder="Número de cuenta"><br>
            <input type="password" id="nip" placeholder="NIP"><br>
            <button onclick="verificar()">Ingresar</button>
            <div id="mensaje"></div>
        </div>

        <footer>
            <span id="fechaHora"></span>
        </footer>

        <script>
            function actualizarFechaHora() {
                const ahora = new Date();
                const fecha = ahora.toLocaleDateString();
                const hora = ahora.toLocaleTimeString();
                document.getElementById('fechaHora').textContent = `Fecha y hora: ${fecha} ${hora}`;
            }

            setInterval(actualizarFechaHora, 1000);
            actualizarFechaHora();

            function verificar() {
                const cuenta = document.getElementById("cuenta").value;
                const nip = document.getElementById("nip").value;

                fetch("/verificar_manual", {
                    method: "POST",
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({cuenta: cuenta, nip: nip})
                })
                .then(res => res.json())
                .then(data => {
                    if (data.ok) {
                        window.location.href = "/cuenta/" + cuenta;
                    } else {
                        document.getElementById("mensaje").textContent = " Datos incorrectos.";
                    }
                });
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/verificar_manual', methods=['POST'])
def verificar_manual():
    data = request.get_json()
    cuenta = data.get("cuenta")
    nip = data.get("nip")

    db = obtener_conexion()
    cuenta_doc = db.cuentas.find_one({"num_cuenta": cuenta})
    
    if cuenta_doc:
        cliente = db.clientes.find_one({"id_cliente": cuenta_doc["id_cliente"]})
        if cliente and cliente.get("nip") == nip:
            return jsonify({"ok": True})
    return jsonify({"ok": False})

@app.route('/verificar_nip_qr', methods=['POST'])
def verificar_nip_qr_post():
    data = request.get_json()
    cuenta = data.get("cuenta")
    nip = data.get("nip")

    db = obtener_conexion()
    cuenta_doc = db.cuentas.find_one({"num_cuenta": cuenta})
    
    if cuenta_doc:
        cliente = db.clientes.find_one({"id_cliente": cuenta_doc["id_cliente"]})
        if cliente and cliente.get("nip") == nip:
            return jsonify({"ok": True})
    return jsonify({"ok": False})



@app.route('/retirar', methods=['POST'])
def retirar():
    data = request.get_json()
    cuenta = data.get("cuenta")
    monto = float(data.get("monto"))
    num_cajero = 1  # fijo

    db = obtener_conexion()
    cuenta_doc = db.cuentas.find_one({"num_cuenta": cuenta})

    if not cuenta_doc:
        return jsonify({"ok": False, "msg": "Cuenta no encontrada"})

    saldo_actual = float(cuenta_doc["saldo_actual"].to_decimal())
    if monto > saldo_actual:
        return jsonify({"ok": False, "msg": "Fondos insuficientes"})

    nuevo_saldo = Decimal128(str(saldo_actual - monto))
    db.cuentas.update_one({"num_cuenta": cuenta}, {"$set": {"saldo_actual": nuevo_saldo}})

    folio = db.retiros_cajero.count_documents({}) + 1
    fecha = datetime.now()

    db.retiros_cajero.insert_one({
        "folio": folio,
        "num_cuenta": cuenta,
        "num_cajero": num_cajero,
        "monto": Decimal128(str(monto)),
        "fecha_hora": fecha,
        "autenticado": True
    })

    archivo_pdf = generar_pdf_retiro(folio, cuenta, monto, fecha, num_cajero)

    return jsonify({
        "ok": True,
        "msg": "Retiro exitoso",
        "nuevo_saldo": str(nuevo_saldo),
        "archivo_pdf": archivo_pdf  # nombre del PDF
    })



if __name__ == '__main__':
    # Si está en Render, la variable PORT ya viene definida automáticamente
    puerto = int(os.environ.get('PORT', 5000))
    debug = puerto == 5000  # Solo debug si estás en localhost
    app.run(host='0.0.0.0', port=puerto, debug=debug)