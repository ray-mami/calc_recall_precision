# coding=utf-8
import json
import pandas as pd
import cv2
import os


def preproc(path):
	txt = b""
	f = open(path,'rb')
	text = f.readlines()
	for i in range(len(text)):
		#text[i] = text[i].replace(b": None," , b": \"None\",")
		text[i] = text[i].replace(b": None" , b": \"None\"")
		text[i] = text[i].replace(b": False" , b": \"False\"")
		text[i] = text[i].replace(b": True" , b": \"True\"")
		txt = txt + text[i]

	return txt

def json2list(txt):
	data = json.loads(txt,strict=False)
	#train = pd.DataFrame.from_dict(data, orient='index')
	return data


#提取车牌定位信息，frame_path为帧图片路径，text_path和img_path分别为结果的文本和图片路径
def get_carno_loc(json_path,frame_path,text_path,img_path,offsize=0):
	text = preproc(json_path)
	a = json2list(text)

	if os.path.exists(text_path):
		shutil.rmtree(text_path)
	os.makedirs(text_path)

	if os.path.exists(img_path):
		shutil.rmtree(img_path)
	os.makedirs(img_path)

	for i in range(len(a)):
		
		f = open(text_path + '/gt_img_'+str(i+offsize)+'.txt','w')
		img = cv2.imread(frame_path +'/'+ a[i]['filename'])
		for j in range(len(a[i]['cars'])):
			if  a[i]['cars'][j]['lefttop'] != '':
				res = a[i]['cars'][j]['lefttop']+','+a[i]['cars'][j]['righttop']+','+a[i]['cars'][j]['rightbottom']+','+a[i]['cars'][j]['leftbottom']+'\n'
				f.write(res)
		cv2.imwrite(img_path +'/img_'+str(i+offsize)+'.jpg',img)
		f.close()


#提取车牌号信息，res_path为结果文本路径
def get_carno(json_path,res_path,offsize=0):
	text = preproc(json_path)
	a = json2list(text)
	if os.path.exists(res_path):
		shutil.rmtree(res_path)
	os.makedirs(res_path)

	f = open(res_path,'wb')
	

	for i in range(len(a)):
		for j in range(len(a[i]['cars'])):
			if len(a[i]['cars'][j]['carno']) == 7:
				res =b'./img_'+str(i+offsize).encode()+b'.jpg'+b' '+ a[i]['cars'][j]['carno'].encode()+b'\n'
				f.write(res)
			#cv2.imwrite('./img-2_test/img_'+str(i)+'.jpg',img)	
	f.close()

get_carno_loc('carinforesult-new1.json','./frame-1','text-1','img-1',offsize=0)


