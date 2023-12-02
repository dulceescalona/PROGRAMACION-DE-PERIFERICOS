# Importación de bibliotecas necesarias
import tkinter as tk  # Para la interfaz gráfica
import socket  # Para la comunicación por sockets
import serial  # Para la comunicación con el Arduino
import threading  # Para manejar múltiples hilos

# Variables globales para la comunicación con el cliente y el Arduino
client_socket = None
arduino_port = None

# Función para aceptar conexiones entrantes de clientes
def accept_connections():
    while True:
        try:
            client, addr = server_socket.accept()
            clients.append((client, addr))
            # Inicia un hilo para manejar las interacciones con el cliente
            client_thread = threading.Thread(target=handle_client, args=(client, addr))
            client_thread.start()
            update_chat(f"{addr} se ha conectado.")
        except OSError:
            break

# Función para manejar las interacciones con un cliente específico
def handle_client(client, addr):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                # Verifica si el cliente envía un comando de salida
                if message == "/exit":
                    remove_client(client, addr)
                else:
                    # Actualiza el chat con el mensaje del cliente y lo difunde a otros clientes
                    update_chat(f"Cliente {addr}: {message}")
                    broadcast_message(f"Cliente {addr}: {message}", client)
        except OSError:
            break

# Función para actualizar el chat en la interfaz gráfica
def update_chat(message):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"{message}\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.see(tk.END)

# Función para difundir un mensaje a todos los clientes
def broadcast_message(message, sender_client):
    for client, addr in clients:
        if client != sender_client:
            try:
                client.send(bytes(message, 'utf-8'))
            except OSError:
                remove_client(client, addr)

# Función para desconectar a un cliente específico
def remove_client(client, addr):
    for c, a in clients:
        if c == client:
            clients.remove((c, a))
            c.close()
            update_chat(f"{a} se ha desconectado.")
            break

# Función para enviar un mensaje del servidor a todos los clientes
def send_server_message(event=None):
    message = server_message.get()
    server_message.set("")
    update_chat(f"Servidor: {message}")
    broadcast_message(f"Servidor: {message}", None)

# Función para iniciar el servidor
def start_server():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.69.54', 5555))  # Reemplaza con la IP y puerto de tu servidor
    server_socket.listen(5)
    server_status.set("Servidor iniciado")
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    accept_thread = threading.Thread(target=accept_connections)
    accept_thread.start()

# Función para detener el servidor
def stop_server():
    global server_socket
    server_socket.close()
    server_status.set("Servidor apagado")
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# Funciones de control del Arduino

# Función para conectar con el Arduino
def connect_to_arduino():
    global arduino_port
    
    try:
        arduino_port = serial.Serial('COM3', 9600)  # Reemplaza 'COMX' con tu puerto COM asignado
        update_interface("Conectado al Arduino")
    except serial.SerialException:
        update_interface("Error al conectar con Arduino")

# Función para desconectar del Arduino
def disconnect_from_arduino():
    global arduino_port
    
    if arduino_port:
        arduino_port.close()
        update_interface("Desconectado del Arduino")
    else:
        update_interface("No hay conexión activa con Arduino")

# Función para encender/apagar el motor del ventilador
def toggle_fan_motor():
    if arduino_port:
        arduino_port.write(b'FAN_TOGGLE\n')  # Envía el comando al Arduino
        update_interface("Motor del Ventilador Toggled")
    else:
        update_interface("No hay conexión con Arduino para controlar el motor")

# Función para ajustar la velocidad del motor del ventilador
def set_fan_speed():
    speed = fan_speed_slider.get()
    if arduino_port:
        arduino_port.write(f'FAN_SPEED {speed}\n'.encode())  # Envía el comando al Arduino
        update_interface(f"Velocidad del Motor del Ventilador ajustada a {speed}")
    else:
        update_interface("No hay conexión con Arduino para controlar la velocidad del motor del ventilador")

# Funciones de control adicional

# Función para encender/apagar la bomba de agua
def toggle_water_pump():
    if arduino_port:
        arduino_port.write(b'WATER_TOGGLE\n')  # Envía el comando al Arduino
        update_interface("Bomba de Agua Toggled")
    else:
        update_interface("No hay conexión con Arduino para controlar la bomba de agua")

# Función para ajustar la intensidad de las luces LED
def set_led_intensity():
    intensity = led_intensity_slider.get()
    if arduino_port:
        arduino_port.write(f'LED {intensity}\n'.encode())  # Envía el comando al Arduino
        update_interface(f"Luces LED ajustadas a intensidad {intensity}")
    else:
        update_interface("No hay conexión con Arduino para controlar las luces LED")
        
# Función para actualizar la interfaz con el mensaje recibido
def update_interface(message):
    messages_text.config(state=tk.NORMAL)
    messages_text.insert(tk.END, message + '\n')
    messages_text.see(tk.END)
    messages_text.config(state=tk.DISABLED)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("servidoor")

# Controles del servidor 

# Marco para la interfaz del chat
frame = tk.Frame(root)
frame.pack()

# Barra de desplazamiento para el chat
scrollbar = tk.Scrollbar(frame)
chat_box = tk.Text(frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_box.pack(side=tk.LEFT, fill=tk.BOTH)
chat_box.config(state=tk.DISABLED)

# Variable para el estado del servidor
server_status = tk.StringVar()
server_status.set("Servidor apagado")
status_label = tk.Label(root, textvariable=server_status)
status_label.pack()

# Botones para iniciar y detener el servidor
start_button = tk.Button(root, text="Iniciar Servidor", command=start_server)
start_button.pack()

stop_button = tk.Button(root, text="Detener Servidor", command=stop_server, state=tk.DISABLED)
stop_button.pack()

