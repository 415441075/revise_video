import os,shutil


mp4_List_Path = [] #存放取出mp4文件路径列表
mp3_List_Path = [] #存放取出mp3文件路径列表

mp4_List_Fulfil_path = [] #存放输出mp4文件路径列表
mp3_List_Fulfil_path = [] #存放输出mp3文件路径列表


path =r'E:\课件\django项目视频B站\74931733' #input('请复制文件路径') #要提取文件路径
fulfil_path = path + '(完成)\\' #提取完存放文件路径
print(fulfil_path)

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:

        temp_Path = os.path.join(root, name)
        # print(temp_Path)
        # print(temp_Path[-9:])

        if name[-9:] == 'audio.m4s':
            mp3_List_Path.append(temp_Path)

            if temp_Path[-15:].startswith("\\"):
                mp3_List_Fulfil_path.append(temp_Path[-14:])
            else:
                mp3_List_Fulfil_path.append(temp_Path[-15:])
        if name[-9:] == 'video.m4s':
            mp4_List_Path.append(temp_Path)

            if temp_Path[-15:].startswith("\\"):
                mp4_List_Fulfil_path.append(temp_Path[-14:])
            else:
                mp4_List_Fulfil_path.append(temp_Path[-15:])

j = 0
for i in mp3_List_Fulfil_path:
    # print((fulfil_path+i).replace('\80','',1))
    print((fulfil_path + mp4_List_Fulfil_path[j]).replace('\80', '', 1))
    fpath, fname = os.path.split((fulfil_path+i).replace('\80','',1))
    if not os.path.exists(fpath):
        os.makedirs(fpath)
    shutil.copyfile(mp3_List_Path[j],((fulfil_path+i).replace('\80','',1)).replace('m4s','mp3', 1))      #复制文件
    shutil.copyfile(mp4_List_Path[j],((fulfil_path + mp4_List_Fulfil_path[j]).replace('\80', '', 1)).replace('m4s','mp4', 1))
    j+=1

