from process.BackTesting.BackTest import BackTesting
from run.config import Path

if __name__ == '__main__':
    stock_id = 'sh.600054'
    strategy = '交叉移动平均5vs.90'

    process = BackTesting(stock_id=stock_id,
                          strategy=strategy,
                          result_root=Path.result_root,
                          action_root=Path.action_root
                          )

    process.run()
