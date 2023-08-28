# Fictitious database
database = {
    "user": {"password": "userpass", "role": "user"},
    "admin": {"password": "adminpass", "role": "admin"},
    "super_user": {"password": "superpass", "role": "superuser"}
}

# Function to verify credentials
def authenticate(username, password, required_role):
    if username in database and database[username]["password"] == password and database[username]["role"] == required_role:
        return True
    return False

# Decorator for multi-level authentication
def auth_required(required_role):
    def decorator(function):
        def wrapper(username, password):
            if authenticate(username, password, required_role):
                return function(username)
            return "Acceso no autorizado"
        return wrapper
    return decorator

# Functions protected by authentication levels
@auth_required("superuser")
def superuser_function(username):
    return f"Saludos, superusuario {username}!"

@auth_required("admin")
def admin_function(username):
    return f"Bienvenido, administrador {username}."

@auth_required("user")
def user_function(username):
    return f"¡Hola, usuario {username}!"

# Get inputs
username = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contraseña: ")

# Try each authentication level
authenticated = False
auth_functions = [superuser_function, admin_function, user_function]

for function in auth_functions:
    result = function(username, password)
    if result != "Acceso no autorizado":
        print(result)
        authenticated = True
        break

if not authenticated:
    print("Acceso no autorizado en todos los niveles.")
