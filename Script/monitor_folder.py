import os
import shutil
import logging
import datetime

# Path to monitor
path_to_monitor=r'E:\Python\test\source\in'

#log fodler path
log_path=r'E:\Python\test\log\log.txt'
logging.basicConfig(filename=log_path,level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


#source & dist
source_path=r'E:\Python\test\source\in'
dist_path=r'E:\Python\test\dist\out'
incorrect_file_path=r'E:\Python\test\incorrectFiles'
temp_path=r'E:\Python\test\temp'

files=os.listdir(path_to_monitor)

file_count=len(files)

#monve files if count>0
try:
    logger.info("------------------------------------Start-------------------------->")
    if file_count >0:
        for file in files:
            if file.endswith('.txt'):
                src= os.path.join(source_path,file)
                dst= os.path.join(dist_path,file)
                tempath=os.path.join(temp_path,file)
                logger.info("moved file from %s to %s",src,tempath)
                shutil.move(src,tempath)
                
                #rename the file
                time_now=datetime.datetime.now()
                timestamp= time_now.strftime("%y%m%d_%H%M")
                basename,fileextension=os.path.splitext(file)
                new_name=f"{timestamp}{basename}{fileextension}"
                dst2=os.path.join(temp_path,new_name)
                os.rename(tempath,dst2)
                logger.info("----------------Rename done---------")
                
                #move the file from temp to out folder
                shutil.move(dst2,dist_path)
                logger.info("the following file %s is renaemd %s and  moved to %s folder",file,new_name,dist_path)
    
                
            else:
                src=os.path.join(source_path, file)
                dst= os.path.join(incorrect_file_path,file)
                shutil.move(src,dst)
                logger.error("File format is wrong: %s, and moved to %s",file,incorrect_file_path)
    else:
        logger.info("no files to move ")
        

except OSError as er:
    logger.error("Process done with followed error %s",er)

else:
    logger.info("Process Done")
    logger.info("---------------------------------END-------------------------------->")



