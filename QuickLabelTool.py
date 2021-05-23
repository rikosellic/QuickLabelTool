import sys
import os
from PyQt5 import QtGui
from tool import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QMessageBox
from PyQt5.QtGui import QPixmap,QImage
from cv2 import rectangle,cvtColor,COLOR_BGR2RGB,imread
import csv
import json
import keyboard
from  concurrent.futures import ThreadPoolExecutor
from queue import Queue

CSV='yolov3-training_train.csv'

def cv2qt(cvimg):
    height, width, depth = cvimg.shape
    cvimg = cvtColor(cvimg, COLOR_BGR2RGB)
    cvimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)
    return cvimg

class MyTool(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyTool, self).__init__()
        self.setupUi(self)
        self.img_info={}
        self.labeled=[]
        self.waiting=Queue()
        self.FLAG=0
        self.num=0
        self.pool=ThreadPoolExecutor(1)
        try:
            csv_file=open(CSV,'r')
            csv_reader=csv.reader(csv_file)
            for i, row in enumerate(csv_reader):
                name=row[0]
                width=row[2]
                height=row[3]
                if i < 2:
                    continue
                img_boxes = []
                for img_box_str in row[5:]:
                    if not img_box_str == "":
                        img_boxes.append(json.loads(img_box_str))
                if name!='':
                    self.img_info[name]=(int(width),int(height),img_boxes)
            print(self.img_info)
            csv_file.close()
        except Exception as e:
            QMessageBox.warning(self, 'Error', '读取csv标注文件失败！程序将退出\n错误信息:{}'.format(e))
            sys.exit()
        if not os.path.exists('images'):
            QMessageBox.warning(self, 'Warning', '没有找到要标注的图像文件夹images！程序将退出')
            sys.exit()
        images_names=os.listdir('images')
        if images_names==[]:
            QMessageBox.warning(self, 'Warning', '文件夹里没有图像！程序将退出')
            sys.exit()
        if not os.path.exists('labels'):
            os.mkdir('labels')
        self.labeled=os.listdir('labels')
        self.labeled=[item.split('.')[0] for item in self.labeled]
        if os.path.exists('error.txt'):
            f=open('error.txt','r')
            errors=f.readlines()
            errors=[item.split('.')[0] for item in errors]
            print(errors)
            f.close()
        else:
            errors=[]
        for image_name in images_names:
            pure_name=image_name.split('.')[0]
            if pure_name in self.labeled or pure_name in errors:
                continue
            else:
                self.waiting.put((pure_name,image_name))
                self.num+=1
        if self.waiting.empty():
            QMessageBox.information(self,'Notice','所有图像均已标注！程序将退出')
            sys.exit()
        self.Remaining.setText('还剩{}张图片待标注'.format(self.num))


    def label_red(self):
        if self.FLAG != 1:
            print(1)
            rx = self.x + self.w / 2
            ry = self.y + self.h / 2
            rx = rx / self.width
            ry = ry / self.height
            rw = self.w / self.width
            rh = self.h / self.height
            if self.FLAG == 0:
                f = open(self.txtname, 'a')
                print("0 {:.6f} {:.6f} {:.6f} {:.6f}".format(rx, ry, rw, rh), file=f)
                f.close()
            else:
                f = open(self.txtname, 'r')
                lines = f.readlines()
                f.close()
                f = open(self.txtname, 'w')
                f.writelines([item for item in lines[:-1]])
                print("0 {:.6f} {:.6f} {:.6f} {:.6f}".format(rx, ry, rw, rh), file=f)
                f.close()
            self.FLAG = 1

    def label_blue(self):
        if self.FLAG != 2:
            print(2)
            rx= self.x + self.w/2
            ry = self.y + self.h/2
            rx = rx / self.width
            ry= ry / self.height
            rw = self.w / self.width
            rh = self.h / self.height
            if self.FLAG == 0:
                f = open(self.txtname, 'a')
                print("1 {:.6f} {:.6f} {:.6f} {:.6f}".format(rx, ry, rw, rh), file=f)
                f.close()
            else:
                f = open(self.txtname, 'r')
                lines = f.readlines()
                f.close()
                f = open(self.txtname, 'w')
                f.writelines([item for item in lines[:-1]])
                print("1 {:.6f} {:.6f} {:.6f} {:.6f}".format(rx, ry, rw,rh), file=f)
                f.close()
            self.FLAG = 2

    def label_yellow(self):
        if self.FLAG != 3:
            print(3)
            rx = self.x + self.w / 2
            ry = self.y + self.h / 2
            rx = rx / self.width
            ry = ry / self.height
            rw = self.w / self.width
            rh = self.h / self.height
            if self.FLAG == 0:
                f = open(self.txtname, 'a')
                print("2 {:.6f} {:.6f} {:.6f} {:.6f}".format(rx, ry, rw, rh), file=f)
                f.close()
            else:
                f = open(self.txtname, 'r')
                lines = f.readlines()
                f.close()
                f = open(self.txtname, 'w')
                f.writelines([item for item in lines[:-1]])
                print("2 {:.6f} {:.6f} {:.6f} {:.6f}".format(rx, ry, rw, rh), file=f)
                f.close()
            self.FLAG = 3


    def process(self):
        self.error_file=open('error.txt','a')
        while not self.waiting.empty():
            try:
                simplename,filename=self.waiting.get()
                print(filename)
                try:
                    self.width, self.height, img_boxes = self.img_info[filename]
                except Exception:
                    print(filename,file=self.error_file)
                    self.num-=1
                    self.Remaining.setText('还剩{}张图片待标注'.format(self.num))
                    continue
                self.txtname = 'labels/' + simplename+ '.txt'
                if img_boxes == []:
                    txt_file = open(self.txtname, 'w')
                    txt_file.close()
                    self.num-=1
                    self.Remaining.setText('还剩{}张图片待标注'.format(self.num))
                    continue
                else:
                    img = imread('images/' + filename)
                    f = open(self.txtname, 'w')
                    f.close()
                    for img_box in img_boxes:
                        self.x = img_box[0]
                        self.y = img_box[1]
                        self.w = img_box[3]
                        self.h = img_box[2]
                        show_img = rectangle(img.copy(), (self.x, self.y), (self.x + self.w, self.y + self.h), (0, 255, 0), 2)
                        self.image.setPixmap(QPixmap(cv2qt(show_img)))
                        #QApplication.processEvents()
                        self.FLAG=0
                        keyboard.add_hotkey('1',self.label_red)
                        keyboard.add_hotkey('2',self.label_blue)
                        keyboard.add_hotkey('3',self.label_yellow)
                        keyboard.wait('enter')
                        print('One box labelled')
                    f=open(self.txtname,'r')
                    count=len(f.readlines())
                    f.close()
                    if count<=len(img_boxes)-2:
                        QMessageBox.warning(self,'Warning','本张图片有超过两个bounded box未标注！之后将重新标注此图')
                        os.remove(self.txtname)
                        self.waiting.put((simplename,filename))
                        continue
                    self.num-=1
                    self.Remaining.setText('还剩{}张图片待标注'.format(self.num))
            except Exception as e:
                result=QMessageBox.warning(self, 'Warning', '出错！程序将退出\n错误信息:{}'.format(e))
        self.error_file.close()
        QMessageBox.information(self,"Info","所有图片均已标注!")


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)
        result = QtWidgets.QMessageBox.question(self, "Notice", "是否关闭程序?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if (result == QtWidgets.QMessageBox.Yes):
            a0.accept()
            if self.num!=0:
                os.remove(self.txtname)
            os._exit()
        else:
            a0.ignore()

    def main(self):
        self.pool.submit(self.process)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mytool = MyTool()
    mytool.show()
    mytool.main()
    sys.exit(app.exec_())