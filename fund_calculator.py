# -*- coding: utf-8 -*-
# !/usr/bin/python

__author__ = 'Long'

import json
import os
import os.path
import subprocess

if __name__ == "__main__":
    array = []
    config = '''
    [
      {
        "stock": "000017",
        "amount": 1629.84,
        "name": "kechixu",
        "cost": 5000,
        "done": 2690.98
      },
      {
        "stock": "233009",
        "amount": 1263.13,
        "name": "damo",
        "cost": 4000,
        "done": 2185.92
      },
      {
        "stock": "161024",
        "amount": 0,
        "name": "jungong",
        "cost": 4000,
        "done": 4424.81
      },
      {
        "stock": "000550",
        "amount": 1530.30,
        "name": "xindongli",
        "cost": 4000,
        "done": 2606.25
      },
      {
        "stock": "519983",
        "amount": 0,
        "name": "changxinlianghua",
        "cost": 5000,
        "done": 5430.00
      }
    ]
    '''
    stocks = json.loads(config)

    total = 0
    index = 0
    cost = 0
    done = 0
    print 'Calculation of earnings...'
    os.system('date')
    for stock in stocks:
        cmd = "curl -s  http://fund.eastmoney.com/%s.html?spm=aladin | sed -n '/statuspzgz/p' | sed 's/<\/span>/<\/span>\\n/g' | sed -n '/statuspzgz/p' | sed 's/>/ /g' | sed 's/</ /g' | awk '{print $8}'" % \
              stock['stock']
        result = subprocess.check_output(cmd, shell=True)
        result = result.strip()
        now = float(result) * stock['amount']
        print 'Code: %s , Price: %s , Amount: %s , Cost: %s , Total: %s ,Done: %s , Percent: %s' % (
            stock['stock'], result, stock['amount'], stock['cost'], now, stock['done'],
            (now + stock['done'] - stock['cost']) / stock['cost'])

        total += float(result) * stock['amount']
        cost += stock['cost']
        done += done + stock['done']
    print "Cost: %s , Total: %s , Win: %s , Done: %s , Percent: %s" % (
        cost, total, (total + done - cost), done, (total + done - cost) / cost)