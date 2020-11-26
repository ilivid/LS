import pandas as pd
import os,sys

def rename_files():             #定义函数名称
    old_names = os.listdir( path )  #取路径下的文件名，生成列表
    for old_name in old_names:      #遍历列表下的文件名
            if  old_name!= sys.argv[0]:  #代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
                if old_name.find("(")<0:   #when文件名以.txt后缀结尾时
                    new_name=old_name.replace('.csv',' (00).csv')   #将原来名字里的‘.txt’替换为‘-test.txt’,相当于加个后缀了
                    os.rename(os.path.join(path,old_name),os.path.join(path,new_name))  #重命名文件
                    print (old_name,"has been renamed successfully! New name is: ",new_name)
                elif old_name.find(")")-old_name.find("(")==2:
                    new_name=old_name.replace('(','(0')   
                    os.rename(os.path.join(path,old_name),os.path.join(path,new_name))  #重命名文件
                    print (old_name,"has been renamed successfully! New name is: ",new_name)

if __name__ == '__main__': 
    path = r'C:\\Data'   #运行程序前，记得修改主文件夹路径！
    rename_files()         #调用定义的函数，注意名称与定义的函数名一致


	# 根据需要修改以下部分
    path = os.path.abspath('C:\\Data\\')  # 文件夹路径
    filename_extenstion = '.csv'  # 文件后缀
    new_file_name = 'data.csv'  # 合并后的文件名
    cols_new_name = ['列名1', '列名2', '列名3', '列名4', '列名5']  # 汇总后的列名，根据需要修改
    cols_num = [1, 2, 3]  # 需要合并的列的索引，从0开始
    file_allname = []  # 用于存储全部文件的名字
    for filename in os.listdir(path):
        if os.path.splitext(filename)[1] == filename_extenstion and filename != new_file_name:  # 按.csv后缀匹配
            t = os.path.splitext(filename)[0]
            file_allname.append(t + filename_extenstion)  # 拼接.csv后缀，生成完整文件名
    df = pd.DataFrame(cols_new_name).T
    try:
        print('开始合并：')
        #df.to_csv(path + '/' + new_file_name, encoding='gbk', header=False, index=False)
        for fn in file_allname:
            data = pd.read_csv(path + '/' + fn)
            print('合并' + fn)
            #data = data.iloc[1:, cols_num]  # 跳过标题行
            data.to_csv(path + '/' + new_file_name, mode='a', encoding='utf-8', header=True, index=False)
        print('合并结束，生成新文件：' + new_file_name)
    except PermissionError as e:
        print('出现异常:' + str(type(e)) + '！\n文件已打开？请先关闭')