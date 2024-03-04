"""
    Compiladores y Lenguajes
    Proyecto # 01 - Implementacion de Grafos en Python con POO
    Autor: Angel David Chuncho Jimenez
    Carrera: Ingenieria de Software
    Fecha: 05/01/2024
    Referencia: Data Structures & Algorithms in Python by Michael Goodrich, et al. (1st Edition)
"""

from Lexer import Lexer
from Parser import Parser
from customtkinter import *

# Main window of the project
app = CTk()
app.title("Compiladores")
app_width = 500
app_height = 400

# Calculate the coordinates to center the window
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_coordinate = (screen_width - app_width) // 2
y_coordinate = (screen_height - app_height) // 2

# Set the geometry of the window
app.geometry(f"{app_width}x{app_height}+{x_coordinate}+{y_coordinate}")

# Events
def click_handler():
    user_input = txtInput.get()
    lexer = Lexer(user_input)
    parser = Parser(lexer)
    result, tokens, parse_tree = parser.parse()
    txtResult.configure(state="normal")
    txtResult.delete(1.0, "end")
    txtResult.insert("end", result)
    txtResult.configure(state="disabled")
    tokens_text = "\n".join([str(token) for token in tokens])
    txtTokens.configure(state="normal")
    txtTokens.delete(1.0, "end")  # Limpiar el contenido actual del widget
    txtTokens.insert("end", tokens_text)  # Insertar los tokens
    txtTokens.configure(state="disabled")
    txtParseTree.configure(state="normal")
    txtParseTree.delete(1.0, "end")
    txtParseTree.insert("end", parse_tree)
    txtParseTree.configure(state="disabled")


lblTitle = CTkLabel(master=app, text="PARSER DE OPERACIONES\n ARITMÉTICAS SIMPLES", font=("Berlin Sans FB Demi", 18))
txtInput = CTkEntry(master=app, placeholder_text="Ingresa una operación", width=180)
btnParsing = CTkButton(master=app, text="Parsing", corner_radius=30, font=("Bauhaus 93", 16), width=100, command=click_handler)
lblResult = CTkLabel(master=app, text="Resultado:", font=("Bauhaus 93", 16))
txtResult = CTkTextbox(master=app, height=1, width=120, corner_radius=16, border_width=2, state="disabled")
lblTokens = CTkLabel(master=app, text="Tokens:", font=("Bauhaus 93", 16))
txtTokens = CTkTextbox(master=app, corner_radius=16, border_width=2, state="disabled")
txtParseTree = CTkTextbox(master=app, corner_radius=16, border_width=2, state="disabled")

lblTitle.place(relx=0.5, rely=0.10, anchor="center")
txtInput.place(relx=0.2, rely=0.25, anchor="center")
btnParsing.place(relx=0.2, rely=0.35, anchor="center")
lblResult.place(relx=0.5, rely=0.27, anchor="s")
txtResult.place(relx=0.71, rely=0.3, anchor="s")
lblTokens.place(relx=0.485, rely=0.35, anchor="s")
txtTokens.place(relx=0.63, rely=0.6, anchor="c")
txtParseTree.place(relx=0.22, rely=0.70, anchor="c")


app.mainloop()
