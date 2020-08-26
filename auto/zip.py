#! python3
#ZipF is to zip entire folders and files - also you zip specific extentions
# usage: "python3 zip.py /user/root/"
# or "python3 zip.py /user/root/ .txt"
import zipfile, os, sys

if len(sys.argv) <= 2:
    

    folder_path = sys.argv[1]
    fileEx = None
else:
    folder_path = sys.argv[1]
    fileEx = sys.argv[2]
def zipf(folder_path, fileEx=None):

    folder_path = os.path.abspath(folder_path)

    number = 1
    while True:
        zipfilename= os.path.basename(folder_path) + "_" + str(number) +'.zip'
        if not os.path.exists(zipfilename):
            break
        number = number + 1
    
    # creat the zip file
    print(f'creating {zipfilename}')
    backupZip = zipfile.ZipFile(zipfilename, 'w')

    # walking through folders
    for foldername , subfolders , filenames in os.walk(folder_path):
        print(f'Adding files in {foldername}. . . ')
        #adding the folder
        backupZip.write(foldername)
        # adding all files in the folder to zipfile
        for filename in filenames:
            newBase = os.path.basename(folder_path) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            if fileEx:
                if filename.endswith(fileEx):
                    os.chdir(foldername)
                    backupZip.write(os.path.join(foldername, filename))
            else:
                backupZip.write(os.path.join(foldername, filename))
    backupZip.close()

zipf(folder_path, fileEx)

