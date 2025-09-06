import tkinter as tk
import random

class DodgeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Difficult Dodge Game")
        self.width = 600
        self.height = 400
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()
        self.player_size = 30
        self.player = self.canvas.create_rectangle(
            self.width//2 - self.player_size//2,
            self.height - self.player_size - 10,
            self.width//2 + self.player_size//2,
            self.height - 10,
            fill="blue"
        )
        self.player_speed = 20
        self.obstacles = []
        self.obstacle_speed = 2
        self.score = 0
        self.game_over = False
        self.score_text = self.canvas.create_text(10, 10, anchor="nw", fill="white", font=("Arial", 16), text="Score: 0")
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.spawn_obstacle()
        self.update()

    def move_left(self, event):
        if not self.game_over:
            self.canvas.move(self.player, -self.player_speed, 0)
            self.check_bounds()

    def move_right(self, event):
        if not self.game_over:
            self.canvas.move(self.player, self.player_speed, 0)
            self.check_bounds()

    def check_bounds(self):
        coords = self.canvas.coords(self.player)
        if coords[0] < 0:
            self.canvas.move(self.player, -coords[0], 0)
        if coords[2] > self.width:
            self.canvas.move(self.player, self.width - coords[2], 0)

    def spawn_obstacle(self):
        size = random.randint(20, 60)
        x = random.randint(0, self.width - size)
        obstacle = self.canvas.create_oval(x, 0, x + size, size, fill="red")
        self.obstacles.append((obstacle, size))
        # Spawn obstacles more frequently as score increases
        interval = max(300, 1000 - self.score * 10)
        self.root.after(interval, self.spawn_obstacle)

    def update(self):
        if self.game_over:
            return
        for obstacle, size in self.obstacles:
            self.canvas.move(obstacle, 0, self.obstacle_speed + self.score/50)
        self.check_collision()
        self.remove_offscreen_obstacles()
        self.score += 1
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
        self.root.after(30, self.update)

    def check_collision(self):
        player_coords = self.canvas.coords(self.player)
        for obstacle, size in self.obstacles:
            obs_coords = self.canvas.coords(obstacle)
            if self.rect_overlap(player_coords, obs_coords):
                self.end_game()

    def rect_overlap(self, rect1, rect2):
        return not (rect1[2] < rect2[0] or rect1[0] > rect2[2] or
                    rect1[3] < rect2[1] or rect1[1] > rect2[3])

    def remove_offscreen_obstacles(self):
        new_obstacles = []
        for obstacle, size in self.obstacles:
            obs_coords = self.canvas.coords(obstacle)
            if obs_coords[1] < self.height:
                new_obstacles.append((obstacle, size))
            else:
                self.canvas.delete(obstacle)
        self.obstacles = new_obstacles

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(self.width//2, self.height//2, fill="yellow", font=("Arial", 32), text="GAME OVER")
        self.canvas.create_text(self.width//2, self.height//2 + 40, fill="white", font=("Arial", 20), text=f"Final Score: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = DodgeGame(root)
    root.mainloop()