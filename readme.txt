
1、local.py
从给定的json中抽取车牌的定位信息。


2、calc_ap_loc.py
计算定位的IOU,根据IOU设定的阈值来计算recall\precision
输入：path_gt：定位的groudtruth文件夹
	 path_res：定位的结果输出文件夹
	 path_iou：输入每个图片的iou结果的文件

3、calc_ap_reg.py
计算识别的准确率。
输入：path_gt：识别的groudtruth文件
	 path_res：识别的结果输出文件


4、generate_train_ocr.py
根据定位的输出结果，生成用于CRNN训练的数据样本
