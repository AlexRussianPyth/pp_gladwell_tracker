import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
from gui_classes import COLOR_PALETTE

TODAY_DATE = dt.datetime.now().date()

class TimeToday:
    
    def __init__(self, df_time):
        """makes time - it's pandas DataFrame, and session_time - other empty DF for this particular working
         session. They exist until the program closed - when they are passed to Save class"""
        self.time = df_time
        self.hours = sum(((self.time.iloc[0].to_list()[1:]))) // 60
        self.session_time = pd.DataFrame({
        'mm_time':0,
        'th_time':0,
        'sc_time':0,
        'pp_time':0
    }, index=[0])

    def show_time(self):
        return [self.time, self.session_time]

    def increase_time(self, type: str):
        """increase overall time and session time"""
        self.time[type][0] += 30
        self.session_time[type][0] += 30
   
    def make_graph(self):
        plt.pie(
            x=self.time.values.tolist()[0], 
            labels=self.time.columns, 
            colors=[COLOR_PALETTE['lightblue'], COLOR_PALETTE['purple'], COLOR_PALETTE['red'], COLOR_PALETTE['orange']], 
            shadow=True)
        plt.legend()
        plt.show()


class WorkDone:
    def __init__(self, df_past):
        self.past_work = df_past
        self.past_work['Date'] = pd.to_datetime(self.past_work['Date'], format='%Y-%m-%d')

    def show_work(self):
        return self.past_work

    def show_yesterday(self) -> str:
        """return sum of yesterday work OR simple message"""
        yesterday = TODAY_DATE - dt.timedelta(days=1)
        yesterday = pd.to_datetime(yesterday)

        if yesterday in self.past_work['Date'].values:
            yesterday_row = self.past_work[self.past_work['Date'] == yesterday]
            minutes_yesterday = sum(((yesterday_row.iloc[0].to_list()[1:])))

            hours_past = str(minutes_yesterday//60).zfill(2)
            minutes_past = str(minutes_yesterday%60).zfill(2)

            return f'{hours_past}:{minutes_past}'
        else:
            return "Did u even work yesterday, hm?"


class Save:
    '''This class makes all of the saving operations'''
    def __init__(self, time, time_today, work):
        self.time_to_save = time
        self.today = time_today
        self.work_to_save = work 

    def save_all(self):
        self.time_to_save.to_csv('time.csv', index=False) 

        if pd.to_datetime(TODAY_DATE) in self.work_to_save['Date'].values:
            # TODO need to make loop
            self.work_to_save.loc[self.work_to_save['Date'] == pd.to_datetime(TODAY_DATE),'mm_time'] += self.today['mm_time'][0]
            self.work_to_save.loc[self.work_to_save['Date'] == pd.to_datetime(TODAY_DATE),'th_time'] += self.today['th_time'][0]
            self.work_to_save.loc[self.work_to_save['Date'] == pd.to_datetime(TODAY_DATE),'sc_time'] += self.today['sc_time'][0]
            self.work_to_save.loc[self.work_to_save['Date'] == pd.to_datetime(TODAY_DATE),'pp_time'] += self.today['pp_time'][0]

        else:
            self.work_to_save = self.work_to_save.append({
                'Date' : TODAY_DATE, 
                'mm_time' : self.today['mm_time'][0],
                'th_time' : self.today['th_time'][0],
                'sc_time' : self.today['sc_time'][0],
                'pp_time' : self.today['pp_time'][0],
            }, ignore_index=True)

        self.work_to_save.to_csv('past.csv', index=False)
