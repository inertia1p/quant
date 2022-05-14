#-*- codig:utf-8 -*-
import jqdatasdk as jq
from datetime import datetime, timedelta
import time
import numpy as np
import math


# module 0
# get the data api
#1 joinquant
jq.auth('18367301905','Zyq137946285')


## module 1
# stock selection module
# tpye: Momentum factor rotation
#

## parameter
# stockPool:list 
# day:int recall days

day = 1


def get_rank(stockPool):
    scoreList = []
    for stock in stockPool:
        # today
        curDate = datetime.strptime(time.strftime("%Y-%m-%d", time.localtime()), '%Y-%m-%d')
        preDate = curDate - timedelta(days = day)
