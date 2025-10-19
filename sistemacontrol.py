usuarios = []
tareas = []    
roles = ("Admin", "Empleado", "Invitado")
estados = ("pendiente", "en progreso", "completada")


def crear_usuario():
    print("\n--- Crear Usuario ---")
    nombre = input("Nombre: ")
    idu = input("ID: ")
    print("Roles:", ", ".join(roles))
    rol = input("Rol: ")
    if rol not in roles:
        rol = "Invitado"
    usuarios.append({"id": idu, "nombre": nombre, "rol": rol})
    print("Usuario agregado.")

def listar_usuarios():
    if not usuarios:
        print("No hay usuarios.")
        return
    for u in usuarios:
        print(f"ID: {u['id']} | Nombre: {u['nombre']} | Rol: {u['rol']}")

def actualizar_usuario():
    idu = input("ID del usuario a actualizar: ")
    for u in usuarios:
        if u["id"] == idu:
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_rol = input("Nuevo rol: ")
            if nuevo_nombre:
                u["nombre"] = nuevo_nombre
            if nuevo_rol in roles:
                u["rol"] = nuevo_rol
            print("Usuario actualizado.")
            return
    print("Usuario no encontrado.")

def eliminar_usuario():
    idu = input("ID del usuario a eliminar: ")
    for u in usuarios:
        if u["id"] == idu:
            usuarios.remove(u)
            print("Usuario eliminado.")
            return
    print("Usuario no encontrado.")

def crear_tarea():
    print("\n--- Crear Tarea ---")
    titulo = input("Título: ")
    desc = input("Descripción: ")
    asignado = input("ID del usuario asignado: ")
    if not any(u["id"] == asignado for u in usuarios):
        print("El usuario no existe.")
        return
    print("Estados:", ", ".join(estados))
    estado = input("Estado: ")
    if estado not in estados:
        estado = "pendiente"
    tareas.append({"titulo": titulo, "descripcion": desc, "usuario": asignado, "estado": estado})
    print("Tarea creada.")

def listar_tareas():
    if not tareas:
        print("No hay tareas.")
        return
    for t in tareas:
        print(f"Título: {t['titulo']} | Asignado a: {t['usuario']} | Estado: {t['estado']}")

def actualizar_tarea():
    titulo = input("Título de la tarea a actualizar: ")
    for t in tareas:
        if t["titulo"] == titulo:
            nuevo_estado = input("Nuevo estado: ")
            if nuevo_estado in estados:
                t["estado"] = nuevo_estado
            print("Tarea actualizada.")
            return
    print("Tarea no encontrada.")

def eliminar_tarea():
    titulo = input("Título de la tarea a eliminar: ")
    for t in tareas:
        if t["titulo"] == titulo:
            tareas.remove(t)
            print("Tarea eliminada.")
            return
    print("Tarea no encontrada.")

def menu_usuarios():
    while True:
        print("\n-- Menú Usuarios --")
        print("1. Crear")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver")
        op = input("Opción: ")
        if op == "1":
            crear_usuario()
        elif op == "2":
            listar_usuarios()
        elif op == "3":
            actualizar_usuario()
        elif op == "4":
            eliminar_usuario()
        elif op == "5":
            break

def menu_tareas():
    while True:
        print("\n-- Menú Tareas --")
        print("1. Crear")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver")
        op = input("Opción: ")
        if op == "1":
            crear_tarea()
        elif op == "2":
            listar_tareas()
        elif op == "3":
            actualizar_tarea()
        elif op == "4":
            eliminar_tarea()
        elif op == "5":
            break

def main():
    while True:
        print("\n===== SISTEMA DE CONTROL DE TAREAS =====")
        print("1. Menú Usuarios")
        print("2. Menú Tareas")
        print("3. Salir")
        op = input("Opción: ")
        if op == "1":
            menu_usuarios()
        elif op == "2":
            menu_tareas()
        elif op == "3":
            print("Saliendo del sistema")
            break

main()

