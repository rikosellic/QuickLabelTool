## QuickLabelTool

QuickLabelTool是为MIT锥桶数据集开发的标注工具，在MIT已有标注的基础上对锥桶进行进一步分类并生成符合YOLO格式的标签。

### 下载

##### 数据集下载

MIT提供的数据集中，有许多图片并没有标注信息，筛选过后的数据集请前往https://jbox.sjtu.edu.cn/v/link/view/628f760873b34b51afbed8c375b52573 下载。总共有6个压缩包，images1-5各包含803张未标注过的图片，images6中包含1965张未标注过的图片。

MIT原始数据集请前往https://console.cloud.google.com/storage/browser/mit-driverless-open-source/?project=mitdriverless&pli=1   查看。

##### 软件下载

QuickLabelTool免安装中文硬盘版请前往链接：https://pan.baidu.com/s/1ZcyWIH02STzx4U4_Ciovmg (提取码：dqua)或 https://jbox.sjtu.edu.cn/v/link/view/b3c4e0666645463c9b0e1e570916c293 下载。

### 使用方法

将软件压缩包解压后，把包含待标注图片的文件夹命名为images，放在QuickLabelTool.exe同一级目录中。双击QuickLabelTool.exe运行程序。程序运行界面如下:

![Image text](https://raw.githubusercontent.com/rikosellic/IMAGE/master/labeltool.png)

图中绿框将标识出当前待标注的锥桶，请根据锥桶颜色在键盘上按下对应的数字键，红色锥桶按1，蓝色按2，黄色按3，之后按回车确认，图片将切换到下一个要标注的锥桶。在按下回车之前可以多次按数字键更改自己的选择。YOLO格式的标注文件将存到labels文件夹中。

### Feature与已知bug

支持断点续传，关闭程序并重新打开不影响已标注好的文件。

如果不按数字键直接按回车，程序也将切换到下一个锥桶，但如果某张图片因此有大于等于两个锥桶未标注，将提示本张图片的标注作废并需要重新标注。

**当程序出现提示框或警告框时，尽量使用回车键确认！使用鼠标点击确认可能会导致程序崩溃！！**

该程序仅在Windows下进行过测试，Linux系统可以尝试从源码编译，不保证可以运行。

部分图片可能出现比例失调的现象。