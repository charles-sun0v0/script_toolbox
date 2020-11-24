import os
import shutil

def process(input_dir,output_dir):
    file_list = os.listdir(input_dir)
    file_prefix_set = set()
    for file in file_list:
        if os.path.isdir(input_dir+"/"+file):
           continue
        file_prefix_set.add(os.path.splitext(file)[0])
    
    for prefix in file_prefix_set:
        year = str(int(prefix[0:4]))
        mon = str(int(prefix[4:6]))
        day = str(int(prefix[6:8]))
        hour = str(int(prefix[8:10]))
        minute = str(int(prefix[10:12]))
        sec = str(int(prefix[12:]))
        dir = year+'-'+mon+'-'+day+'-'+hour+'-'+minute+'-'+sec
        gen_dir = output_dir + '/' + dir+'/origin'
        os.makedirs(gen_dir,exist_ok=True)
        shutil.copy(input_dir+'/'+prefix+'.png',gen_dir+'/'+'original_data.png')
        # shutil.copy(input_dir+'/'+prefix+'.cld',gen_dir+'/'+'original_data.cld')
        shutil.copy(input_dir+'/'+prefix+'.pcd',gen_dir+'/'+'original_data.pcd')
        if os.path.exists(input_dir+'/'+prefix+'.xml'):
           shutil.copy(input_dir+'/'+prefix+'.xml',gen_dir+'/'+'original_data.xml')
        f= open(output_dir + '/' + dir +'/timestamp.txt','w')
        f.write(year),f.write(' ')
        f.write(mon),f.write(' ')
        f.write(day),f.write(' ')
        f.write(hour),f.write(' ')
        f.write(minute),f.write(' ')
        f.write(sec)
        f.close()


if __name__ == "__main__":
    root = r"Z:/bagtest/test_data/pcd+png"
    output_dir = r"Z:/TestData/bag/test0"
    process(root,output_dir)
