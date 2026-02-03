import tkinter as tk
import serial
import time

SERIAL_PORT = 'COM3'  # Zmienić w zalezności od portu
BAUD_RATE = 115200


def send_coordinates():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(0.1)

        x_val = entry_x.get()
        y_val = entry_y.get()

        # Format: "X100Y200\n"
        command = f"X{x_val}Y{y_val}\n"

        ser.write(command.encode())
        print(f"Sent: {command.strip()}")
        ser.close()
        status_label.config(text="Sent!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {e}", fg="red")


root = tk.Tk()
root.title("2D Arm Controller")
root.geometry("250x200")

tk.Label(root, text="Target X:").pack()
entry_x = tk.Entry(root)
entry_x.pack()

tk.Label(root, text="Target Y:").pack()
entry_y = tk.Entry(root)
entry_y.pack()

tk.Button(root, text="Move", command=send_coordinates, height=2, bg="lightblue").pack(pady=10)
status_label = tk.Label(root, text="Ready")
status_label.pack()

root.mainloop()