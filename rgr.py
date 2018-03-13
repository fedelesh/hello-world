from tkinter import *
root = Tk()
root.title("???????")

Vg = 0
Vb = 5
Vs = 2
Vd = 5
I_base = 1
Vt_base = - 0.2

u_ms = 0 #??????? ????? ??????
u_f = 0.3
q = 1.6 * (10 ** (-19))
m_p = 600 * (10 ** (-4)) #??????????

e0 = 8.85418781762039 * (10 ** (-12))

e = 11.7
E = e * e0 #???????????? ??????????? ????????

eox = 3.9
Eox = eox * e0 #???????????? ??????????? ????????????? ???????????

tox = 100 * (10 ** (-10))
Cox = Eox / tox #?????? ??????? ????????????? ???????????
k = m_p * Cox

Vsb = Vs - Vb
Qss = 0 #????? ? ???????????
Vgs = Vg - Vs
Vds = Vd - Vs

def voltageConc(N):
    answer = u_ms + 2 * u_f - (((2 * q * N * E * (2 * u_f - Vsb)) ** 0.5) / Cox) - Qss / Cox
    print("Voltage: ", answer, "for concentration: ", N)
    return answer

def current(w_l):
    answer = k / 2 * w_l * ((Vgs - Vt) ** 2)
    print("Current: ", answer, " for Width/Length: ", w_l)
    return answer

def width_to_lenght(I):
    answer = (2 * I) / (k * ((Vgs - Vt_base) ** 2))
    print("Width/Length: ", answer, " for Current: ", I)
    return answer

def find_concentration(V):
    up = (((2 * u_f - V) * Cox) ** 2)
    down = (2 * q * E * (2 * u_f - Vsb))
    answer = (((2 * u_f - V) * Cox) ** 2) / (2 * q * E * (2 * u_f - Vsb))
    print("Concentration: ", answer, " for Volatge: ", V)
    return answer

def voltage_thickness(T, N):
    if(T == 0):
        T = 10 ** -20
    C = Eox/T
    answer = u_ms + 2 * u_f - (((2 * q * N * E * (2 * u_f - Vsb)) ** 0.5) / C) - Qss / Cox
    print("Voltage: ", answer, "for concentration: ", N)
    return answer

def scrollbar(canv,root):
        scrollbar = Scrollbar(root)
        scrollbar.pack(side='right')
        scrollbar['command'] = canv.yview
        canv['yscrollcommand'] = scrollbar.set

def plot_voltage_concentration(N_normal):
    root = Tk()

    canv = Canvas(root, width = 1100, height = 1100, bg = "white")
    canv.create_line(100, 1000, 100, 0, width=2, arrow=LAST)
    canv.create_line(0, 500, 1100, 500, width=2, arrow=LAST)
    scrollbar(canv,root)
    graf_range = 1000

    firstX = 100
    step = N_normal / (graf_range)
    for i in range(graf_range):
        N = step * i
        N_next = step * (i + 1)
        V = voltageConc(N)
        V_next = voltageConc(N_next)
        x = i + firstX
        y = - V * 100 + 500
        y_next = - V_next * 100 + 500
        canv.create_oval(x, y, x + 1, y_next, fill = 'black')
        if(abs(Vt - V) < 0.00001):
            canv.create_oval(x - 3, y - 3, x + 3, y + 3, fill='#000')
        if (i % 100 == 0):
            k = firstX + i
            strin = '{:e}'.format(N)
            canv.create_line(k, -3 + 500, k, 3 + 500, width = 0.5, fill = 'black')
            canv.create_text(k + 15, -10 + 500, text = strin, fill="purple", font=("Helvectica", "10"))
            canv.create_line(97, i, 103, i, width = 0.5, fill = 'black')
            canv.create_text(80, i, text = '%.2f' % ((graf_range - i) / 100 - 5), fill="purple", font=("Helvectica", "10"))

    canv.pack()
    root.mainloop()

def plot_current(W_L_normal):
    root = Tk()

    canv = Canvas(root, width = 1100, height = 1000, bg = "white")
    canv.create_line(100, 1000, 100, 0, width=2, arrow=LAST)
    canv.create_line(0, 500, 1100, 500, width=2, arrow=LAST)
    scrollbar(canv,root)
    graf_range = 1000

    firstX = 100
    step = W_L_normal / (2*graf_range)
    for i in range(graf_range):
        W_L = step * i
        W_L_next = step * (i + 1)
        I = current(W_L)
        I_next = current(W_L_next)
        x = i + firstX
        y = - I * 1000 + 500
        y_next = - I_next * 1000 + 500
        canv.create_oval(x, y, x + 1, y_next, fill = 'black')
        if(abs(I_base - I) < 0.0000001):
            canv.create_oval(x - 3, y - 3, x + 3, y + 3, fill='#000')
        if (i % 100 == 0):
            k = firstX + i
            strin =int(W_L)
            canv.create_line(k, -3 + 500, k, 3 + 500, width = 0.5, fill = 'black')
            canv.create_text(k + 15, -10 + 500, text = strin, fill="purple", font=("Helvectica", "10"))
            canv.create_line(97, i, 103, i, width = 0.5, fill = 'black')
            canv.create_text(80, i, text = '%.0f' % (((graf_range - i) / 10 - 50) * 10), fill="purple", font=("Helvectica", "10"))

    canv.pack()
    root.mainloop()

def plot_voltage_thickness(T_normal, N_normal):
    root = Tk()
    canv = Canvas(root, width = 1100, height = 1000, bg = "white")
    canv.create_line(100, 1000, 100, 0, width=2, arrow=LAST)
    canv.create_line(0, 500, 1100, 500, width=2, arrow=LAST)
    scrollbar(canv,root)
    graf_range = 1000
    firstX = 100
    step = T_normal / ( graf_range)
    for i in range(graf_range):
        T = step * i
        T_next = step * (i + 1)
        V = voltage_thickness(T, N_normal)
        V_next = voltage_thickness(T_next, N_normal)
        x = i + firstX
        y = - V * 100 + 500
        y_next = - V_next * 100 + 500
        if(abs(Vt - V) < 0.00001):
            canv.create_oval(x - 3, y - 3, x + 3, y + 3, fill='#000')
        canv.create_oval(x, y, x + 1, y_next, fill = 'black')
        if (i % 100 == 0):
            k = firstX + i
            strin = '{:e}'.format(T)
            canv.create_line(k, -3 + 500, k, 3 + 500, width = 0.5, fill = 'black')
            canv.create_text(k + 15, -10 + 500, text = strin, fill="purple", font=("Helvectica", "10"))
            canv.create_line(97, i, 103, i, width = 0.5, fill = 'black')
            canv.create_text(80, i, text = '%.2f' % ((graf_range - i) / 100 - 5), fill="purple", font=("Helvectica", "10"))
    canv.pack()
    root.mainloop()

Na = find_concentration(Vt_base)
Vt = voltageConc(Na)

W_L_n = width_to_lenght(I_base)
Id = current(W_L_n)

def Voltage(event):
    plot_voltage_concentration(Na)

def Voltage_thickness(event):
    plot_voltage_thickness(tox, Na)

def Current(event):
    plot_current(W_L_n)

btn = Button(root,
             text="?????????? ????????? ??????? ??? ???????????? ??????? ? ????????",
             width=110,height=5,
             bg="white",fg="black")
btn.bind("<Button-1>", Voltage)
btn.grid(row = 1, column = 1, columnspan = 3)

btn1 = Button(root,
             text="?????????? ?????? ? ?????? ??? ?????????? ?????? ?????? ?? ???? ???????",
             width=110,height=5,
             bg="white",fg="black")
btn1.bind("<Button-1>", Current)
btn1.grid(row = 2, column = 1, columnspan = 3)

btn2 = Button(root,
             text="?????????? ????????? ??????? ??? ??????? ????????????? ???????????",
             width=110,height=5,
             bg="white",fg="black")
btn2.bind("<Button-1>", Voltage_thickness)
btn2.grid(row = 3, column = 1, columnspan = 3)
root.mainloop()