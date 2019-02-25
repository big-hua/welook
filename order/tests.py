from django.test import TestCase

import datetime
import random
nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
print(nowTime)
randomNum=random.randint(0,100)
if randomNum<=10:
    randomNum=str(0)+str(randomNum)
uniqueNum=str(nowTime)+str(randomNum)
print(uniqueNum)


