

class Portfolio:
    def __init__(self,
                 initial_position=100000,
                 transaction_fees=0
                 ):
        self.cash = initial_position
        self.transaction_fees = transaction_fees
        self.holding = {}

    # 做多
    def long(self, stock_id, tstock):
        # 全仓
        NoLong = self.cash // tstock.open_price
        self.cash -= NoLong * (tstock.open_price + self.transaction_fees)
        self.holding[stock_id] = NoLong

    # 做空
    def short(self, stock_id, tstock):
        # 全仓
        self.cash += self.holding[stock_id] * (tstock.open_price + self.transaction_fees)
        del self.holding[stock_id]
