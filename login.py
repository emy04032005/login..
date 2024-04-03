from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Aquí normalmente configurarías tu base de datos, sistema de autenticación, etc.

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Aquí normalmente validarías el nombre de usuario y contraseña
        # y realizarías alguna lógica de autenticación.
        # Por ahora, solo redireccionaremos al usuario después de enviar el formulario.
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/inicio')
def inicio():
    # Aquí pondrías el código para la página de inicio después de iniciar sesión.
    return 'Bienvenido'

if __name__ == '__main__':
    app.run(debug=True)
