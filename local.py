# coding=utf-8
import json
import pandas as pd
import cv2


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



def get_carno_loc(json_path,frame_path,text_path,img_path,offsize=0)
	text = preproc(json_path)

	a = json2list(text)

	for i in range(len(a)):
		
		f = open(text_path + '/gt_img_'+str(i+offsize)+'.txt','w')
		img = cv2.imread(frame_path +'/'+ a[i]['filename'])
		for j in range(len(a[i]['cars'])):
			if  a[i]['cars'][j]['lefttop'] != '':
				res = a[i]['cars'][j]['lefttop']+','+a[i]['cars'][j]['righttop']+','+a[i]['cars'][j]['rightbottom']+','+a[i]['cars'][j]['leftbottom']+'\n'
				f.write(res)
		cv2.imwrite(img_path +'/img_'+str(i+offsize)+'.jpg',img)
		f.close()



def get_carno(json_path,res_path,offsize=0):
	text = preproc(json_path)
	a = json2list(text)	

	f = open(res_path,'wb')
	

	for i in range(len(a)):
		for j in range(len(a[i]['cars'])):
			if len(a[i]['cars'][j]['carno']) == 7:
				res =b'./img_'+str(i+offsize).encode()+b'.jpg'+b' '+ a[i]['cars'][j]['carno'].encode()+b'\n'
				f.write(res)
			#cv2.imwrite('./img-2_test/img_'+str(i)+'.jpg',img)	
	f.close()




