from Data import *


class Filterdata:
    def __init__(self,df):
        self.df = df

    def get_male_df(self):
        df_male = self.df.loc[(self.df['Gender'] == 'Male')]
        return df_male
    
    def get_female_df(self):
        df_female = self.df.loc[(self.df['Gender'] == 'Female')]
        return df_female
    
    def get_age_young(self):
        df_young = self.df.loc[(self.df['Age'] == '16-20')]
        return df_young
    
    def get_age_middle(self):
        df_middle = self.df.loc[(self.df['Age'] == '20-25')]
        return df_middle
    
    def get_age_old(self):
        df_old = self.df.loc[(self.df['Age'] == '25-30')]
        return df_old
    
    def get_age_oldest(self):
        df_oldest = self.df.loc[(self.df['Age'] == '25-30')]
        return df_oldest

print(df)