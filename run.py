from proxypool.scheduler import Scheduler
from proxypool.api import app
import sys
def main():
    s = Scheduler()
    s.run()
    app.run()
if __name__ == '__main__':
    main()
    print(sys.path)