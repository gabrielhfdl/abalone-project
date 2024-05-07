import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from dog.dog_actor import DogActor
from dog.dog_interface import DogPlayerInterface
class ActorPlayer(DogPlayerInterface):
    def __init__(self):
        self.board = [
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 3, 3, 1, 1, 1, 3, 3, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3],
            [0, 3, 3, 3, 3, 3, 3, 3, 3],
            [0, 3, 3, 2, 2, 2, 3, 3, 0],
            [0, 0, 2, 2, 2, 2, 2, 2, 0],
            [0, 0, 2, 2, 2, 2, 2, 0, 0]
        ]

          # 1: player 1
          # 2: player 2
          # 3: espaço vazio
          # 0: fora do tabuleiro

        self.circle_size = 40
        self.circles_distance = 20
        self.screen_width = 1280
        self.screen_height = 720


        self.interface()

    def interface(self):
        self.window = tk.Tk()
        self.window.title("Abalone")

        self.canvas = tk.Canvas(self.window, width=self.screen_width, height=self.screen_height, bg="gray")
        self.canvas.pack()

        self.draw_board()

        play_button = tk.Button(self.window, text="Jogar", bg="blue", fg="white", width=20, font=("Arial", 14, 'bold'), command=self.draw_players)
        play_button.place(relx=0.5, rely=1.0, y=-20, anchor=tk.S)

        message = "Bem-vindo ao Abalone!"
        label = tk.Label(self.window, text=message, fg="black", font=("Arial", 12))
        label.place(x=10, y=10, anchor=tk.NW)

        player_name = simpledialog.askstring(title="Player identification", prompt= "Olá, qual é o seu nome?")
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        
        messagebox.showinfo(message = message)
        self.window.mainloop()

    def draw_board(self):
        for i in range(len(self.board)): # desenha os círculos representando as posições do tabuleiro
            # calcula a posição inicial dos espaços do tabuleiro
            row_size = len([pos for pos in self.board[i] if pos != 0])
            total_space = row_size * self.circle_size + (row_size - 1) * self.circles_distance
            position_x = (self.screen_width - total_space) / 2

            for j in range(len(self.board[i])):
                if self.board[i][j] != 0:
                    position_y = (self.screen_height - (len(self.board) * (self.circle_size + self.circles_distance))) / 2 + i * (self.circle_size + self.circles_distance)
                    self.canvas.create_oval(position_x, position_y, position_x + self.circle_size, position_y + self.circle_size, fill="black")
                    position_x += self.circle_size + self.circles_distance

    def draw_players(self):
        for i in range(len(self.board)):
            # calcula a posição inicial das peças
            row_size = len([pos for pos in self.board[i] if pos != 0])
            total_space = row_size * self.circle_size + (row_size - 1) * self.circles_distance
            if i == 2 or i == 6: 
                position_x = (self.screen_width - total_space) / 2 + 2 * (self.circle_size + self.circles_distance)
            else:
                position_x = (self.screen_width - total_space) / 2

            for j in range(len(self.board[i])):
                if self.board[i][j] == 1:
                    position_y = (self.screen_height - (len(self.board) * (self.circle_size + self.circles_distance))) / 2 + i * (self.circle_size + self.circles_distance)
                    self.canvas.create_oval(position_x, position_y, position_x + self.circle_size, position_y + self.circle_size, fill="red")
                    position_x += self.circle_size + self.circles_distance
                elif self.board[i][j] == 2:
                    position_y = (self.screen_height - (len(self.board) * (self.circle_size + self.circles_distance))) / 2 + i * (self.circle_size + self.circles_distance)
                    self.canvas.create_oval(position_x, position_y, position_x + self.circle_size, position_y + self.circle_size, fill="blue")
                    position_x += self.circle_size + self.circles_distance

ActorPlayer()
