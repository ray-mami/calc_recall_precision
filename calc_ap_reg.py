import numpy as np
import math
import os





def calc_res_prec(path_gt,path_res):
	flag = 0
	total = 0
	f = open(path_gt,'rb')
	ff = open(path_res,'rb')

	a1 = f.readlines()
	a2 = ff.readlines()

	for i in range(len(a2)):
		total += 1
		img = a2[i].decode().split(',')[0]
		carno = a2[i].decode().split(',')[1]
		for j in range(len(a1)):
			img_1 = a1[j].decode().split(' ')[0]
			carno_1 = a1[j].decode().split(' ')[1]
			if img in img_1:
				carno_1 = carno_1.replace('\n','')
				if carno == carno_1:
					 flag+=1
	print (flag/total)
	print (flag)
	print (total)




                    

calc_res_prec('/Users/ray/Desktop/test-car/reg.txt','/Users/ray/Desktop/test-car/reg_res.txt')


#print(calc_iou([1035,532.0,1118,553.0],[1034,528,1118,559]))