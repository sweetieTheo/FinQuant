

class BackTestor:
    def __init__(self,
                 return_method='HPR',
                 start_date=None,
                 end_date=None
                 ):
        self.return_method = return_method
        self.start_date = start_date
        self.end_date = end_date


    # 持有期间收益
    def HPR(self, period, stock):
        return


