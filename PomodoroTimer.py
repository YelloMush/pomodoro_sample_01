import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x400')
        self.root.title("Pomodoro Timer")
        self.root.tk.call('wm','iconphoto',self.root._w,PhotoImage(file="timer-icon.png"))
        
        self.style = ttk.Style()
        self.style.configure('TNotebook.Tab', font=('Arial',12))
        self.style.configure('TButton', font=('Arial', 12))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill='both',padx=10,pady=10,expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=400)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=400)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=400)

        self.pomodoro_timer_label = ttk.Label(self.tab1, text='25:00', font=('Arial',50))
        self.pomodoro_timer_label.pack(pady = 95)

        self.shortbreak_timer_label = ttk.Label(self.tab2, text='05:00', font=('Arial',50))
        self.shortbreak_timer_label.pack(pady = 95)

        self.longbreak_timer_label = ttk.Label(self.tab3, text='15:00', font=('Arial',50))
        self.longbreak_timer_label.pack(pady = 95)
        

        self.tabs.add(self.tab1, text='Pomodoro')
        self.tabs.add(self.tab2, text='Short Break')
        self.tabs.add(self.tab3, text='Long Break')

        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)

        self.start_button = ttk.Button(self.grid_layout, text='Start',command=self.start_timer_thread)
        self.start_button.grid(row=0,column=0)

        self.skip_button = ttk.Button(self.grid_layout, text='Skip',command=self.skip_timer)
        self.skip_button.grid(row=0,column=1)

        self.reset_button = ttk.Button(self.grid_layout, text='Reset',command=self.reset_timer)
        self.reset_button.grid(row=0,column=2)

        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text='Pomodoros : 0', font=('Arial',14))
        self.pomodoro_counter_label.grid(row=1,column=0,columnspan=3,pady=10)

        self.pomodoro = 0
        self.skipped = False
        self.stopped = False
        self.running = False

        self.root.mainloop()


    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True

    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:
            full_second = 60 * 25
            full_second = 5
            while full_second > 0 and not self.stopped:
                minutes,seconds = divmod(full_second,60)
                self.pomodoro_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_second -= 1
            
            if not self.stopped or self.skipped:
                self.pomodoro += 1
                self.pomodoro_counter_label.config(text=f"Pomodoro : {self.pomodoro}")
                if self.pomodoro % 4 == 0:
                    self.tabs.select(2)
                else:
                    self.tabs.select(1)
                self.start_timer()

        elif timer_id == 2:
            full_second = 60 * 25
            full_second = 5
            while full_second > 0 and not self.stopped:
                minutes,seconds = divmod(full_second,60)
                self.shortbreak_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_second -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()

        elif timer_id == 3:
            full_second = 60 * 25
            full_second = 5
            while full_second > 0 and not self.stopped:
                minutes,seconds = divmod(full_second,60)
                self.longbreak_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_second -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()

    def reset_timer(self):
        self.stopped = True
        self.skipped = False
        self.pomodoro = 0
        self.pomodoro_timer_label.config(text='25:00')
        self.shortbreak_timer_label.config(text='05:00')
        self.longbreak_timer_label.config(text='15:00')
        self.pomodoro_counter_label.config(text='Pomodoro : 0')
        self.running = False

    def skip_timer(self):
        current_tab = self.tabs.index(self.tabs.select())

        if current_tab == 0:
            self.pomodoro_timer_label.config(text='25:00')
        if current_tab == 1:    
            self.shortbreak_timer_label.config(text='05:00')
        if current_tab == 2:
            self.longbreak_timer_label.config(text='15:00')

        self.stopped = True
        self.skipped = True


    

PomodoroTimer()