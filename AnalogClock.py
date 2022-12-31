import tkinter as tk
import time
import math

class AnalogClock(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self.width = self.winfo_reqwidth()
        self.height = self.winfo_reqheight()
        self.center_x = self.width / 2
        self.center_y = self.height / 2
        self.face = self.create_oval(0, 0, self.width, self.height, fill='white')
        self.update_clock()

    def update_clock(self):
        self.delete(tk.ALL)
        self.face = self.create_oval(0, 0, self.width, self.height, fill='white')
        self.draw_numbers()
        self.draw_hands()
        self.after(200, self.update_clock)

    def draw_numbers(self):
        self.create_text(self.center_x, self.center_y - 0.8 * self.center_y, text='12', font=('TkDefaultFont', 16))
        for i in range(1, 12):
            angle = i * (360 / 12)
            x = self.center_x + 0.8 * self.center_y * math.sin(math.radians(angle))
            y = self.center_y - 0.8 * self.center_y * math.cos(math.radians(angle))
            self.create_text(x, y, text=str(i), font=('Courier', 16))

    def draw_hands(self):
        now = time.localtime()
        hour = now.tm_hour % 12
        minute = now.tm_min
        second = now.tm_sec
        hour_angle = hour * (360 / 12) + minute * (360 / (12 * 60))
        minute_angle = minute * (360 / 60)
        second_angle = second * (360 / 60)
        self.draw_hand(hour_angle, 0.5 * self.center_x, 'red')
        self.draw_hand(minute_angle, 0.7 * self.center_x, 'blue')
        self.draw_hand(second_angle, 0.9 * self.center_x, 'green')

    def draw_hand(self, angle, length, color):
        x = self.center_x + length * math.sin(math.radians(angle))
        y = self.center_y - length * math.cos(math.radians(angle))
        self.create_line(self.center_x, self.center_y, x, y, fill=color, width=2)

root = tk.Tk()
clock = AnalogClock(root, width=400, height=400)
clock.pack()
root.mainloop()
