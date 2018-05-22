import numpy as np
import math
import os

def calc_iou(a,b):
	if max(a[0],a[2]) > min(b[0],b[2]) and min(a[0],a[2]) < max(b[0],b[2]) and max(a[1],a[3]) > min(b[1],b[3]) and min(a[1],a[3]) < max(b[1],b[3]): 

		h = sorted([a[1],a[3],b[1],b[3]])
		w = sorted([a[0],a[2],b[0],b[2]])

		return((h[2]-h[1])*(w[2]-w[1])) / ((a[2]-a[0])*(a[3]-a[1]) + (b[2]-b[0])*(b[3]-b[1]) - (h[2]-h[1])*(w[2]-w[1]))

	else:
		return 0




def calc_res_recall(path_gt,path_res,res):
	flag = 0
	total = 0
	fff = open(res,'w')
	for filename in os.listdir(path_gt):
		if filename.endswith(".txt"):
			imgname = filename.split('.')[0]
			imgname = imgname[3:]
			res_file = 'res_'+imgname+'.txt'
			gtFullPath = os.path.join(path_gt,filename)
			resFullPath = os.path.join(path_res,res_file)
			f = open(gtFullPath,'r')
			ff = open(resFullPath,'r')
			gt_lines = f.readlines()
			total += len(gt_lines)
			res_lines = ff.readlines()
			for line in res_lines:
				score = 0
				a = []
				aa = line.split(',')
				for i in range(len(aa)):
					a.append(float(aa[i]))
				for line_gt in gt_lines:
					bb = line_gt.split(',')
					b = [int(bb[0]),int(bb[1]),int(bb[4]),int(bb[5])]
					t = calc_iou(a,b)
					if t > score:
						score = t
				
				fff.write(imgname + ',' + str(score)+ '\n')

				if score > 0.4:
					flag +=1
		
			f.close()
			ff.close()
	fff.close()
	print (total)
	print (flag/total)


def calc_res_precision(path_gt,path_res):
	flag = 0
	total = 0
	#fff = open('conclude.txt','w')
	for filename in os.listdir(path_gt):
		if filename.endswith(".txt"):
			imgname = filename.split('.')[0]
			imgname = imgname[3:]
			res_file = 'res_'+imgname+'.txt'
			gtFullPath = os.path.join(path_gt,filename)
			resFullPath = os.path.join(path_res,res_file)
			f = open(gtFullPath,'r')
			ff = open(resFullPath,'r')
			gt_lines = f.readlines()
			res_lines = ff.readlines()
			total += len(res_lines)
			for line in res_lines:
				score = 0
				a = []
				aa = line.split(',')
				for i in range(len(aa)):
					a.append(float(aa[i]))
				for line_gt in gt_lines:
					bb = line_gt.split(',')
					b = [int(bb[0]),int(bb[1]),int(bb[4]),int(bb[5])]
					t = calc_iou(a,b)
					if t > score:
						score = t
				
				#fff.write(imgname + ',' + str(score)+ '\n')

				if score > 0.5:
					flag +=1
		
			f.close()
			ff.close()
	#fff.close()
	print (total)
	print (flag/total)




                    

calc_res_precision('/Users/ray/Desktop/test-car/text','/Users/ray/Desktop/test-car/results_1')


#print(calc_iou([1035,532.0,1118,553.0],[1034,528,1118,559]))