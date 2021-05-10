import pandas as pd
# import our classes
from time_classes import TimeToday, WorkDone, Save
from gui_classes import MyGui

# Download Time Data and make TimeToday instance. If 'time.csv' doesn't exist - makes new.
try:
    time_data = pd.read_csv('time.csv')
except FileNotFoundError: 
    time_data = pd.DataFrame({
        'mm_time':0,
        'th_time':0,
        'sc_time':0,
        'pp_time':0,
    }, index=[0])

my_time = TimeToday(time_data)

# Download the Past Data and make WorkDone instance (or create new)
try:
    work_done_data = pd.read_csv('past.csv')
except FileNotFoundError:
    work_done_data = pd.DataFrame({
        'Date': '1970-01-01',
        'mm_time':0,
        'th_time':0,
        'sc_time':0,
        'pp_time':0,
    }, index=[0])

my_work = WorkDone(work_done_data)

# Create MyGui Instance and pass arguments (string with yesterday's anount of work and instance of other class)
window = MyGui(my_work.show_yesterday(), my_time)

window.mainloop() # RUN!

# After Exit we create Save class instance and pass all of our data in this class
exit_class = Save(my_time.time, my_time.session_time, my_work.past_work)
exit_class.save_all()