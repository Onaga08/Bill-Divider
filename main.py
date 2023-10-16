import tkinter as tk
from tkinter import ttk
from function import calculate_bill

def on_calculate():
    total_bill = float(entry1.get())
    total_units = float(entry2.get())
    
    m1i = float(m1i_entry.get())
    m1f =float(m1f_entry.get())
    
    m2i = float(m2i_entry.get())
    m2f = float(m2f_entry.get())
    
    m3i = float(m3i_entry.get())
    m3f = float(m3f_entry.get())
    
    m1 = m1f - m1i
    m2 = m2f - m2i
    m3 = m3f - m3i
    animesh, jalaj, mayank, saket, pradyumn = calculate_bill(total_bill, total_units, m1, m2, m3)
    result_label.config(text=f"Animesh: {animesh}\n Jalaj: {jalaj}\n Mayank: {mayank}\n Saket: {saket}\n Pradyumn:{pradyumn}")

window = tk.Tk()
window.title("Bill Calculator")
window.geometry("500x400")
s = ttk.Style()
s.configure("BW.TLabel", foreground = "gold", background = "black")


title_label = ttk.Label(window, text = "Bill Calculator GUI", width = 20, style="BW.TLabel", justify="center")
title_label.grid(row=0, column=1, pady=10)

label1 = tk.Label(window, text="Total Bill:", borderwidth=2, relief="solid")
label1.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

entry1 = tk.Entry(window, width=10)
entry1.grid(row=1, column=1, padx=20, pady=20)

label2 = tk.Label(window, text="Total Units:",borderwidth=2, relief="solid")
label2.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")

entry2 = tk.Entry(window, width=10)
entry2.grid(row=1, column=3, padx=20, pady=20)

m1i_label = tk.Label(window, text="Meter 1 initial:", borderwidth=2, relief="solid")
m1i_label.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

m1i_entry = tk.Entry(window, width=10)
m1i_entry.grid(row=2, column=1, padx=20, pady=20)

m1f_label = tk.Label(window, text="Meter 1 final:", borderwidth=2, relief="solid")
m1f_label.grid(row=2, column=2, padx=20, pady=20, sticky="nsew")

m1f_entry = tk.Entry(window, width=10)
m1f_entry.grid(row=2, column=3, padx=20, pady=20)

m2i_label = tk.Label(window, text="Meter 2 intial:", borderwidth=2, relief="solid")
m2i_label.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")

m2i_entry = tk.Entry(window, width=10)
m2i_entry.grid(row=3, column=1, padx=20, pady=20)

m2f_label = tk.Label(window, text="Meter 2 final:", borderwidth=2, relief="solid")
m2f_label.grid(row=3, column=2, padx=20, pady=20, sticky="nsew")

m2f_entry = tk.Entry(window, width=10)
m2f_entry.grid(row=3, column=3, padx=20, pady=20)

m3i_label = tk.Label(window, text="Meter 3 intial:", borderwidth=2, relief="solid")
m3i_label.grid(row=4, column=0, padx=20, pady=20, sticky="nsew")

m3i_entry = tk.Entry(window, width=10)
m3i_entry.grid(row=4, column=1, padx=20, pady=20)

m3f_label = tk.Label(window, text="Meter 3 final:", borderwidth=2, relief="solid")
m3f_label.grid(row=4, column=2, padx=20, pady=20, sticky="nsew")

m3f_entry = tk.Entry(window, width=10)
m3f_entry.grid(row=4, column=3, padx=20, pady=20)


calculate_button = tk.Button(window, text="Calculate", command=on_calculate)
calculate_button.grid(row=5, column=0, columnspan=40)

result_label = tk.Label(window, text="Result: ")
result_label.grid(row=6, column=0, columnspan=5)

window.mainloop()