# coding=utf-8
import json
import pandas as pd
import cv2
import os
import random


def calc_iou(a,b):
	if max(a[0],a[2]) > min(b[0],b[2]) and min(a[0],a[2]) < max(b[0],b[2]) and max(a[1],a[3]) > min(b[1],b[3]) and min(a[1],a[3]) < max(b[1],b[3]): 

		h = sorted([a[1],a[3],b[1],b[3]])
		w = sorted([a[0],a[2],b[0],b[2]])

		return((h[2]-h[1])*(w[2]-w[1])) / ((a[2]-a[0])*(a[3]-a[1]) + (b[2]-b[0])*(b[3]-b[1]) - (h[2]-h[1])*(w[2]-w[1]))

	else:
		return 0

#path_g:定位的groundtruth; path_res:定位的results; path_img:原始图像路径 ; path_gen_text:sample.txt路径；path_gen_img:用于训练的图像路径
def generate(path_gt,path_res,path_img,path_gen_text,path_gen_img):
	flag = 0
	total = 0
	f_gen = open(path_gen_text,'wb')
	train = []
	for filename in os.listdir(path_gt):
		flag = 0
		if filename.endswith(".txt"):
			imgname = filename.split('.')[0]
			imgname = imgname[3:]
			img = cv2.imread(path_img + '/' + imgname + '.jpg')
			res_file = 'res_'+imgname+'.txt'
			gtFullPath = os.path.join(path_gt,filename)
			resFullPath = os.path.join(path_res,res_file)
			f_gt = open(gtFullPath,'rb')
			f_res = open(resFullPath,'r')
			
			gt_lines = f_gt.readlines()
			total += len(gt_lines)
			res_lines = f_res.readlines()
			for line in res_lines:
				flag = 0
				score = 0
				bbb =[]
				a = []
				aa = line.split(',')
				for i in range(len(aa)):
					a.append(float(aa[i]))
				for line_gt in gt_lines:
					bb = line_gt.decode().split(',')
					b = [int(bb[0]),int(bb[1]),int(bb[4]),int(bb[5])]
					t = calc_iou(a,b)
					if t > score:
						score = t
						carno_1 = bb[-1]
						carno_1 = carno_1.replace('\n','')
						bbb = b
						#print (len(carno_1))
						if len(carno_1) == 7:
							flag = 1
							#carno_1 = carno_1.replace('\n','')
							carno_2 = carno_1
							
				#fff.write(imgname + ',' + str(score)+ '\n')

				if score > 0.4 and flag==1:
					if carno_2 in train:
						carno_2 = carno_1 + str(random.randint(1,100000))

					f_gen.write(b'./' + carno_2.encode() + b'.jpg' + b' ' + carno_1.encode() + b'\n')
					res_img = img[int(a[1]):int(a[3]),int(a[0]):int(a[2]),:]
					res_img = cv2.resize(res_img, (120, 32), interpolation=cv2.INTER_CUBIC)
					cv2.imwrite(path_gen_img + '/' + carno_2 + '.jpg',res_img)
					train.append(carno_2)

				if score <= 0.4 and flag==1 and score>=0.1:
					if carno_2 in train:
						carno_2 = carno_1 + str(random.randint(1,100000))
					f_gen.write(b'./' + carno_2.encode() + b'.jpg' + b' ' + carno_1.encode() + b'\n')
					res_img = img[int(bbb[1]):int(bbb[3]),int(bbb[0]):int(bbb[2]),:]
					res_img = cv2.resize(res_img, (120, 32), interpolation=cv2.INTER_CUBIC)
					cv2.imwrite(path_gen_img + '/' + carno_2 + '.jpg',res_img)
					train.append(carno_2)			
		
			f_gt.close()
			f_res.close()
	f_gen.close()


generate('/Users/ray/Desktop/test-car/text','/Users/ray/Desktop/test-car/results_63','/Users/ray/Desktop/test-car/img','/Users/ray/Desktop/test-car/gen/sample.txt','/Users/ray/Desktop/test-car/gen')
