import os
import shutil

# declare months
DDYY = {'01': 'Jan', '02': 'Feb', '03': ' Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
        '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}

# Source and Destination
SourcelocInput = "c:\Pavi\PickBestPic"
DestlocInput = "c:\GotPics"
# parent Folder
subdir, dirs, files = next(os.walk(SourcelocInput.replace("\\ ", " /")))

# Move Function
def getYearMonthofFileName(eachFile):
    yearMonth_list=[]
    print("YEAR MONTH FUNCTION ",eachFile)
    if "BURST" in eachFile:
        print("Has")
        getYear = eachFile.split('_')[2][5:9]
        getMonth = eachFile.split('_')[2][9:11]
        yearMonth_list.append(getYear)
        yearMonth_list.append(getMonth)
        return yearMonth_list
    else:
        getYear = eachFile.split('_')[1][0:4]
        getMonth = eachFile.split('_')[1][4:6]
        yearMonth_list.append(getYear)
        yearMonth_list.append(getMonth)
        return yearMonth_list


def moveToFunction(subDir, DestlocInput, files):
    print(" MOVE TO FUNCTION SubDIR" , subDir," DestLoc",DestlocInput," Files",files)
    if len(files) > 1:
        for eachFile in files:
            print("EACH FILE ", eachFile)
            Year_Month=getYearMonthofFileName(eachFile)
            getYear=Year_Month[0]
            getMonth=Year_Month[1]
            print("Pic Folder", files, "MONTH :", DDYY.get(getMonth), "  Year", getYear)
            source = subDir.replace("\\", "/")+"/"+eachFile
            target = (DestlocInput + "/" + getYear + "/" + DDYY.get(getMonth)).replace("\\ ", " /")
            print("Source  : ",source,"Target Path : ",target)
            # create the folders if not already exists
            os.makedirs(target, exist_ok=True)
             # adding exception handling
            createdOrNot = shutil.move(source, target)
            print("File Created or not", createdOrNot)
    else:
        one_file=files[0]
        print("Else of moveToFunction " , one_file," SUB DIR ",subDir)
        Year_Month = getYearMonthofFileName(one_file)
        getYear = Year_Month[0]
        getMonth = Year_Month[1]
        print("One Pic", one_file, "MONTH :", getMonth ,DDYY.get(getMonth), "  Year", getYear)
        source = subDir.replace("\\", "/") + "/" + one_file
        target = (DestlocInput + "/" + getYear + "/" + DDYY.get(getMonth)).replace("\\ ", " /")
        print("Source  : ", source, "Target Path : ", target)
        # create the folders if not already exists
        os.makedirs(target, exist_ok=True)
        print("One Source : ", source, "Target ... ", target)
        # adding exception handling
        createdOrNot = shutil.move(source, target)
        print("File Created or not", createdOrNot)


Orign_subdir=subdir
# DCIM directory
for files in dirs:
    print("->",files)
    subdir=Orign_subdir.replace("\\","/")+"/"+files
    print("SUBDIR PATH ",subdir)
    isDir = (os.path.isdir(subdir))
    isFile=os.path.isfile(subdir)
    print("is a direc", isDir)
    print("Is a File ",isFile)
    if "Control Panel" in files:
        print("Ignore this Folder : " + files)
    if ".inflight_lowres" in files:
        print("Ignore this Folder : " + files)
    else:
        # DCIM/IMG
        if ("IMG" in files) and isDir:
            subdir=subdir.replace("\\","/")
            DestlocInput=DestlocInput.replace("\\","/")
            print("SUB DIR ",subdir)
            subdir, dirs, xfiles= next(os.walk(subdir))
            print("FILES ",xfiles)
            if len(xfiles) !=0:
              #inside the IMG folder
              print("IMG FOLDER Subdir ",subdir," FILES :", len(xfiles), "DESTINATION FOLDER ", DestlocInput)
              moveToFunction(subdir, DestlocInput, xfiles)
              print()
            else:
                print(subdir, " is empty")
                print("")

        elif "Raw"  in files:
            # Copy files as per the date to dest folder
            print("Raw DIRECTORY ", subdir)
            DestlocInput=DestlocInput+"/Raw"
            subdir, dirs, files = next(os.walk(subdir))
            moveToFunction(subdir.replace("\\", "/"), DestlocInput.replace("\\", "/"), files)

        #only image files
        else:
            if("IMG" in files and isFile):
                print("IMG FILES ONLY ")
                moveToFunction(subdir.replace("\\","/"),DestlocInput.replace("\\","/"),files)



