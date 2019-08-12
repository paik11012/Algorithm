from datetime import datetime, timedelta
import sys
from typing import Any, Union
sys.stdin = open('input2.txt','r')

sm, sd, em, ed = map(int, input().split())
start_day=datetime.datet~ime(2000,sm,sd,0)
end_day=datetime.datetime(2000,em,ed,0)
gap=end_day - start_day
print(gap)