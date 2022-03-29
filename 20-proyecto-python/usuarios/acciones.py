from usuarios import usuario as modelo

class Acciones:

    def registro(self):
        print("\n¡¡OK!! vamos a registrate en el sistema...")
        nombre = input("¿Cuál es tu nombre?: ")
        apellidos = input("¿Cuáles son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        
        else:
            print("\nNo te has registrado correctamente.")

    def login(self):
        print("\n¡¡Vale!! identifícate en el sistema...")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario("", "", email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has resitrado en el sistema el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto!! Inténtalo más tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - salir (salir)
        """)

        accion = input("Qué quieres hacer?: ")

        if accion == "crear":
            print("Vamos a crear")
            self.proximasAcciones(usuario)
        
        elif accion == "mostrar":
            print("Vamos a mostrar")
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            print("Vamos a eliminar")
            self.proximasAcciones(usuario)
        
        elif accion == "salir":
            print(f"OK {usuario[1]}, hasta pronto!!!")
            exit()

        