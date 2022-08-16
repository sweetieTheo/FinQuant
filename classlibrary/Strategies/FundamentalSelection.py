

class SelectionAlg:
    def __init__(self
                 ):
        self.Algs = {'Top_marketValue': self.mv_selection
                     }

    def __getitem__(self, item):
        return self.Algs[item]

    @ staticmethod
    # candidates： list[Stock]， limits: int
    def mv_selection(candidates, limits, trading_date):
        tmp_dict = {}
        for stock in candidates:
            tmp_dict[stock.stock_id] = stock[trading_date].mv

        return [stock_info[0] for stock_info in sorted(tmp_dict.items(), key=lambda x:x[1])]

