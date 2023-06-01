#!/usr/bin/env python3

import numpy as np
import rclpy
from std_msgs.msg import String
from pynput import keyboard
from rclpy.node import Node
from PIL import ImageTk, Image
import tkinter as tk
import os




class Publicador(Node):

    def __init__(self):
        super().__init__('manipulator')
        self.publisher_ = self.create_publisher(String, 'manipulator_ang', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.movement = String()
        self.presionado=False
        #por defecto la velocidades son 1 
        self.angular_value = 1.0
        self.linear_value = 1.0

        # Crear ventana de tkinter para la interfaz de movimiento
        self.root = tk.Tk()
        self.root.title("Robot Teleop")
        self.root.geometry("500x500")

        #mportar imagen de fondo
        ruta_imagen = os.path.abspath("imagen_de_fondo.jpg")
        image = Image.open(ruta_imagen)
        image = image.resize((500, 500), Image.ANTIALIAS) # Redimensionar la imagen
        bg_image = ImageTk.PhotoImage(image)
        # Crear un Label con la imagen de fondo
        bg_label = tk.Label(self.root, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

       

        # Crear marcos para los botones de movimiento y establecer la imagen de fondo
        self.defaultbg = self.root.cget('bg')
        movement_frame = tk.Frame(self.root, bg=self.defaultbg)
        movement_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True) 
        movement_frame.grid_columnconfigure(0, weight=1)
        movement_frame.grid_columnconfigure(1, weight=1)
        movement_frame.grid_columnconfigure(2, weight=1)
        movement_frame.grid_columnconfigure(3, weight=1)
        
        movement_frame.grid_rowconfigure(0, weight=1)
        movement_frame.grid_rowconfigure(1, weight=1)
        movement_frame.grid_rowconfigure(2, weight=1)
        movement_frame.grid_rowconfigure(3, weight=1)

        bg_label = tk.Label(movement_frame, image=bg_image)
        bg_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Crear botones de movimiento y hacerlos transparentes
        
        self.z_button = tk.Button(movement_frame, text="Z", width=5, height=5, command=lambda:self.grip_on(self,self.z_button), highlightthickness=0, bg='#191970', fg='white', font=('Arial', 16))
        self.x_button = tk.Button(movement_frame, text="X", width=5, height=5, command=lambda:self.grip_off(self,self.x_button), highlightthickness=0, bg='#191970', fg='white', font=('Arial', 16))
        self.y_button = tk.Button(movement_frame, text="Y", width=5, height=5, command=lambda:self.antarm_forward(self,self.y_button), highlightthickness=0,bg='#191970', fg='white', font=('Arial', 16))
        self.u_button = tk.Button(movement_frame, text="U", width=5, height=5, command=lambda:self.antarm_backward(self,self.u_button), highlightthickness=0, bg='#191970', fg='white', font=('Arial', 16))
        self.h_button = tk.Button(movement_frame, text="H", width=5, height=5, command=lambda:self.arm_forward(self,self.h_button), highlightthickness=0, bg='#191970', fg='white', font=('Arial', 16))
        self.j_button = tk.Button(movement_frame, text="J", width=5, height=5, command=lambda:self.arm_backward(self,self.j_button), highlightthickness=0, bg='#191970', fg='white', font=('Arial', 16))
        self.n_button = tk.Button(movement_frame, text="N", width=5, height=5, command=lambda:self.base_left(self,self.n_button), highlightthickness=0, bg='#191970', fg='white', font=('Arial', 16))
        self.m_button = tk.Button(movement_frame, text="M", width=5, height=5, command=lambda:self.base_right(self,self.m_button), highlightthickness=0, bg='#191970', fg='white', font=('Arial', 16))
        
        
        self.z_button.grid(row=0, column=0)
        self.x_button.grid(row=0, column=1) 
        self.y_button.grid(row=1, column=2)
        self.u_button.grid(row=1, column=3)
        self.h_button.grid(row=2, column=0)
        self.j_button.grid(row=2, column=1) 
        self.n_button.grid(row=3, column=2)
        self.m_button.grid(row=3, column=3)                    


        # Asociar teclas del teclado con los botones de movimiento
        self.root.bind('<KeyPress-z>', lambda event: self.z_button.config(relief=tk.SUNKEN))
        self.root.bind('<KeyPress-x>', lambda event: self.x_button.config(relief=tk.SUNKEN))
        self.root.bind('<KeyPress-y>', lambda event: self.y_button.config(relief=tk.SUNKEN))
        self.root.bind('<KeyPress-u>', lambda event: self.u_button.config(relief=tk.SUNKEN))
        self.root.bind('<KeyPress-h>', lambda event: self.h_button.config(relief=tk.SUNKEN))
        self.root.bind('<KeyPress-j>', lambda event: self.j_button.config(relief=tk.SUNKEN))
        self.root.bind('<KeyPress-n>', lambda event: self.n_button.config(relief=tk.SUNKEN))
        self.root.bind('<KeyPress-m>', lambda event: self.m_button.config(relief=tk.SUNKEN))

        self.root.bind('<KeyRelease-z>', lambda event: self.z_button.config(relief=tk.RAISED))
        self.root.bind('<KeyRelease-x>', lambda event: self.x_button.config(relief=tk.RAISED))
        self.root.bind('<KeyRelease-y>', lambda event: self.y_button.config(relief=tk.RAISED))
        self.root.bind('<KeyRelease-u>', lambda event: self.u_button.config(relief=tk.RAISED))
        self.root.bind('<KeyRelease-h>', lambda event: self.h_button.config(relief=tk.RAISED))
        self.root.bind('<KeyRelease-j>', lambda event: self.j_button.config(relief=tk.RAISED))
        self.root.bind('<KeyRelease-n>', lambda event: self.n_button.config(relief=tk.RAISED))
        self.root.bind('<KeyRelease-m>', lambda event: self.m_button.config(relief=tk.RAISED))

        # Iniciar listener de teclado
        self.key_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.key_listener.start()
        self.root.mainloop()

        
    def open_grip(self):
        button=self.z_button
        self.movement.data = "z"
        print(self.movement)
        self.publisher_.publish(self.movement)
        button.configure(bg='#FFA500')

    def close_grip(self):
        button=self.x_button
        self.movement.data = "x"
        self.publisher_.publish(self.movement)
        button.configure(bg='#FFA500')

    def antarm_forward(self):
        button=self.y_button
        self.movement.data = "y"
        self.publisher_.publish(self.movement)
        button.configure(bg='#FFA500')

    def antarm_backward(self):
        button=self.u_button
        self.movement.data = "u"
        self.publisher_.publish(self.movement)
        button.configure(bg='#FFA500')
        
    def arm_forward(self):
        button=self.h_button
        self.movement.data = "h"
        self.publisher_.publish(self.movement)
        button.configure(bg='#FFA500')

    def arm_backward(self):
        button=self.j_button
        self.movement.data = "j"
        self.publisher_.publish(self.movement)
        button.configure(bg='#FFA500')    
        
    def base_left(self):
        button=self.n_button
        self.movement.data = "n"
        self.publisher_.publish(self.movement)
        button.configure(bg='#FFA500')

    def base_right(self):
        button=self.m_button
        self.movement.data = "m"
        self.publisher_.publish(self.movement)
        button.configure(bg='#FFA500')
    
    def unopen_grip(self):
        button=self.z_button
        self.movement.data = "0.0"
        self.publisher_.publish(self.movement)
        button.configure(bg='#191970')

    def unclose_grip(self):
        button=self.x_button
        self.movement.data = "0.0"
        self.publisher_.publish(self.movement)
        button.configure(bg='#191970')

    def antarm_unforward(self):
        button=self.y_button
        self.movement.data = "0.0"
        self.publisher_.publish(self.movement)
        button.configure(bg='#191970')

    def antarm_unbackward(self):
        button=self.u_button
        self.movement.data = "0.0"
        self.publisher_.publish(self.movement)
        button.configure(bg='#191970')
        
    def arm_unforward(self):
        button=self.h_button
        self.movement.data = "0.0"
        self.publisher_.publish(self.movement)
        button.configure(bg='#191970')

    def arm_unbackward(self):
        button=self.j_button
        self.movement.data = "0.0"
        self.publisher_.publish(self.movement)
        button.configure(bg='#191970')
        
    def base_unleft(self):
        button=self.n_button
        self.movement.data = "0.0"
        self.publisher_.publish(self.movement)
        button.configure(bg='#191970')

    def base_unright(self):
        button=self.m_button
        self.movement.data = "0.0"
        self.publisher_.publish(self.movement)
        button.configure(bg='#191970')


    def custom_cmd(self, cmd):
        self.get_logger().info('Custom command received: "%s"' % cmd)
        # Aquí puedes implementar lo que quieras que haga el robot cuando reciba un comando personalizado

    def on_press(self, key):
        try:
            # Mapear teclas de flechas a comandos de movimiento
            if key.char == 'z' and (not self.presionado):
                self.presionado=True
                self.open_grip()
            elif key.char == 'x'and (not self.presionado):
                self.presionado=True
                self.close_grip()
            elif key.char == 'y'and (not self.presionado):
                self.presionado=True
                self.antarm_forward()
            elif key.char == 'u' and (not self.presionado):
                self.presionado=True
                self.antarm_backward()
            elif key.char == 'h'and (not self.presionado):
                self.presionado=True
                self.arm_forward()
            elif key.char == 'j'and (not self.presionado):
                self.presionado=True
                self.arm_backward()
            elif key.char == 'n'and (not self.presionado):
                self.presionado=True
                self.base_left()
            elif key.char == 'm'and (not self.presionado):
                self.presionado=True
                self.base_right()
            else:
                # Si se presiona cualquier otra tecla, tomar el comando personalizado de la entrada de texto
                cmd = self.custom_cmd_entry.get()
                self.custom_cmd(cmd)
        except AttributeError:
            # Ignorar teclas de modificación (Shift, Ctrl, Alt, etc.)
            pass

    def on_release(self, key):
        # Detener el movimiento al soltar cualquier tecla de movimiento
        try:
            if key.char == 'z'and (self.presionado):
                self.presionado=False
                self.unopen_grip()
            elif key.char == 'x'and (self.presionado):
                self.presionado=False
                self.unclose_grip()
            elif key.char == 'y'and ( self.presionado):
                self.presionado=False
                self.antarm_unforward()
            elif key.char == 'u'and ( self.presionado):
                self.presionado=False
                self.antarm_unbackward()
            elif key.char == 'h'and (self.presionado):
                self.presionado=False
                self.arm_unforward()
            elif key.char == 'j'and (self.presionado):
                self.presionado=False
                self.arm_unbackward()
            elif key.char == 'n'and ( self.presionado):
                self.presionado=False
                self.base_unleft()
            elif key.char == 'm'and ( self.presionado):
                self.presionado=False
                self.base_unright()
        except AttributeError:
            # Ignorar teclas de modificación (Shift, Ctrl, Alt, etc.)
            pass

    def timer_callback(self):
        print(self.linear_speed_entry)
        print(self.angular_speed_entry)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)     
    publicador = Publicador()

    rclpy.spin(publicador)

    publicador.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
    print("¡El programa se ha ejecutado correctamente!")