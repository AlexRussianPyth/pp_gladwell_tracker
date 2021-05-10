import tkinter as tk
import tkinter.ttk as ttk
import random

WINDOW_COLOR = '#334443'
TEXT_COLOR = '#fffbdf'
MILESTONE = 100 # uses for progress bar
MAIN_FONT = "Georgia"
COLOR_PALETTE = {
    'yellow' : '#fdca40',
    'red' : '#fb3640',
    'lightblue' : '#3edbf0',
    'purple' : '#542e71',
    'orange' : '#e1701a'
}

class MyGui(tk.Tk):

    def __init__(self, yesterday_time, time_instance):
        super().__init__()

        self.config(bg=WINDOW_COLOR, padx=20, pady=20)
 
        # Quote
        self.productivity_quote = tk.Label(
            text=self.random_quote(), 
            padx=20, 
            pady=20, 
            wraplength=250, 
            justify='center', 
            font=(MAIN_FONT, 10, 'italic'),
            bg=WINDOW_COLOR,
            fg=TEXT_COLOR)
        self.productivity_quote.grid(row=0, column=2, rowspan=3, columnspan=2, stick="wens")

        # Yesterday Time
        # TODO change color from the time
        self.yesterday_label = tk.Label(text='Yesterday', bg=WINDOW_COLOR, fg=TEXT_COLOR, font=(MAIN_FONT, 12, 'bold'))
        self.yesterday_label.grid(column=0, row=0, columnspan=2, stick='we')

        self.yesterday_time = tk.Label(text=yesterday_time, bg=WINDOW_COLOR, fg=TEXT_COLOR, font=(MAIN_FONT, 20))
        self.yesterday_time.grid(row=1, column=0, columnspan=2)
        
        # Graph Button
        self.graph_btn = tk.Button(text="Make Graph", command=time_instance.make_graph, bg=COLOR_PALETTE['yellow'], padx=20)
        self.graph_btn.grid(row=2, column=0, columnspan=2, pady=10)

        # Progress Bar
        self.progress_bar = ttk.Progressbar(length=700, mode='determinate', maximum=MILESTONE, value=time_instance.hours)
        self.progress_bar.grid(row=3, column=0, columnspan=4, pady=5)

        # Buttons
        self.mm_btn = tk.Button(text="MM +30m", command=lambda: time_instance.increase_time('mm_time'), bg=COLOR_PALETTE['lightblue'])
        self.mm_btn.grid(row=4, column=0, stick='we')

        self.th_btn = tk.Button(text="TH +30m", command=lambda: time_instance.increase_time('th_time'), bg=COLOR_PALETTE['purple'])
        self.th_btn.grid(row=4, column=1, stick='we')

        self.sc_btn = tk.Button(text="SC +30m", command=lambda: time_instance.increase_time('sc_time'), bg=COLOR_PALETTE['red'])
        self.sc_btn.grid(row=4, column=2, stick='we')

        self.pp_btn = tk.Button(text="MM +30m", command=lambda: time_instance.increase_time('pp_time'), bg=COLOR_PALETTE['orange'])
        self.pp_btn.grid(row=4, column=3, stick='we')
        
    def random_quote(self):
        """this method return random productivity quote"""
        with open("quotes.txt") as new_file:
            quotes = new_file.readlines()
            return random.choice(quotes)