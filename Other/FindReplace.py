import fileinput
import sys
import os
import collections
import re
import csv
from xml.dom.minidom import *
from optparse import OptionParser
   
   
##################################
#KNOWN ISSUES     
#Will only replace first occurence of Set_Alarm(###) in the string
#Odd behavior if same file exists twice in the director xml file
#
#
###################################

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def directoryStructure(dirStruct):
	args = []
	path = ""
	dirFiles = []
	greatestIndex = 0 
	
	parentDir = dirStruct.getElementsByTagName("TOP")[0]
	#print(getText(parentDir.childNodes));
	directories = dirStruct.getElementsByTagName("DIR")
	for directory in directories:
		#print("Path: "+directory.getAttribute("PATH"));
		path = directory.getAttribute("PATH")
		files = directory.getElementsByTagName("FILE")
		dirFiles = []
		for myFile in files:
			#print(getText(myFile.childNodes));
			dirFiles.append((getText(myFile.childNodes),int(myFile.getAttribute("INDEX")), myFile.getAttribute("ISEXAMINED")))
			if int(myFile.getAttribute("INDEX")) > greatestIndex:
				greatestIndex = int(myFile.getAttribute("INDEX"))
		args.append((path,dirFiles))
	myMap = {"TOP":getText(parentDir.childNodes), "PATHS": args, "IdxMax":greatestIndex}
	return myMap
	
def addNewFiles(expected, actual, startingIdx):
	results = []
	fileList = []
	pathExists = False
	fileExists = False
	#TBD Merge existing file stuff back
	# Start by comparing Actual Dirs versus the ones from the xml file (expected)
	for path,files in actual:
		pathExists = False
		fileList = []
		for pathExpected, filesExpected in expected:
			#Path exists in both actual and expected
			if path == pathExpected:
				pathExists = True
				#compare the Actual Files versuses the expected ones
				for myFile, idx, isExamined in files:
					fileExists = False
					for myFileExpected, idxExpected, isExaminedExpected in filesExpected:
						#The File exists doesn't do anything special
						if myFile == myFileExpected:
							fileExists = True
							fileList.append((myFileExpected,idxExpected,isExaminedExpected.upper()))
					#File didn't exists add my new name plus a revised index
					if fileExists == False:
						fileList.append((myFile,startingIdx,'Y'))
						startingIdx = startingIdx+1
				####### Search the opposite direction aka find out what expected ones we have that aren't in actuals
				for myFileExpected, idxExpected, isExaminedExpected in filesExpected:
					fileExists = False
					for myFile, idx, isExpected in files:
						#The File exists doesn't do anything special
						if myFile == myFileExpected:
							#Already added above
							fileExists = True
					#File didn't exists add my new name plus a revised index
					if fileExists == False:
						fileList.append((myFileExpected,idxExpected,isExaminedExpected.upper()))
				break
		#End expected for
		#Path wasnt found so add all files under the path
		if pathExists == False:
			for myFile, idx, isExpected in files:
				fileList.append((myFile,startingIdx,'Y'))
				startingIdx = startingIdx+1
		#add our new data item
		results.append((path,fileList))
	#Bad idea breaks on first find of the path...
	#results = expected+ results
	#print(results)	
	return results		
				

#This function will take our file structure array and build an xml file.  It gets recreated each time.
# Instead of modding the existing file.  This made constructing the file significantly easier.	
def buildXMLFile(filePath,dirPath, fileMap):
	mapFile = open(filePath, 'w')
	#Build the XML structure
	mapFile.write('<ROOT>\n')
	#Dirpath is either assigned via the filePath (new xml file) or the path in the top tag in an existing xml
	mapFile.write('  <TOP>'+dirPath+'</TOP>\n');
	for root, files in fileMap:
		root = root.replace('\\','/')
		#print('d:',root)
		#print('f:',files)
		mapFile.write('  <DIR PATH=\''+root+'\'>\n')
		for name,idx, isExamined in files:
			name = name.replace('\\','/')
			mapFile.write('    <FILE INDEX=\''+str(idx)+'\' ISEXAMINED=\''+isExamined.upper()+'\'>'+name+'</FILE>\n')
		mapFile.write('   </DIR>\n')
	mapFile.write('</ROOT>')	
	mapFile.close()

def genFileMap(filePath,updateCPPOnly):
	idx = 1;
	if os.path.isfile(filePath):
		print("File Does Exist")
		mapFile = open(filePath, 'r')
		### Determine if need XML updates
		### Extract XML and expected file structure
		myDom = parse(mapFile)
		mapFile.close()
		myMap = directoryStructure(myDom)
		if updateCPPOnly:
			print("Only Updating Paths")
			return myMap["PATHS"]
		dirPath = myMap["TOP"].replace('\\','/')
		#Establish the actual file structure
		results = []
		#print("Path:" +dirPath)
		for root, dirs, files in os.walk(dirPath):
			fileList = []
			root = root.replace('\\','/')
			for name in files:
				if name.endswith(".cpp"):
					fileList.append((name,idx,'Y'))
					idx = idx + 1
			results.append((root,fileList))
		if (myMap["PATHS"] != results):
			results = addNewFiles(myMap["PATHS"],results, myMap["IdxMax"]+1)   
			buildXMLFile(filePath,dirPath,results)
	else:
		print("File Doesn't exist")
		updateXMLOnly = True
		#mapFile = open(filePath, 'w')
		dirPath = os.path.dirname(filePath)
		myFiles = []
		results = []
		idx = 1
		for root, dirs, files in os.walk(dirPath):
			myFiles = []
			for name in files:
				if name.endswith(".cpp"):
					myFiles.append((name,idx,'Y'))
					idx = idx + 1
			results.append((root.replace('\\','/'),myFiles))
		#print(results)  
		buildXMLFile(filePath,dirPath,results)
	return results
	
def replaceAllSetAlarm(filePath,idx,outCSV):
    if not os.path.exists(filePath):
    	print("File Does not Exist: "+filePath)
    	return
    desFile = open(filePath,'r')
    srcRep = "Set_Alarm()"
    desRep = "Set_Alarm(#)"
    prevLine = ""
    lineNumber = 0
    srcInput = ""
    fileIdx = 1;
    isChanged = False
    for line in desFile:
    	lineNumber +=1
    	m = re.search("Alarm_Manager_Class::Set_Alarm *?\(.*?\)",line)
    	if (m != None):
    		#Calculate the new set alarm code
    		setAlarmNum = ((idx&0xFFFFF) << 16) | (fileIdx &0xFFFF)
    		srcRep = m.group(0)
    		#Are we actually changing something?
    		if srcRep != "Alarm_Manager_Class::Set_Alarm("+str(setAlarmNum)+")":
    			#print("Compare: " + srcRep + "against " + "Set_Alarm("+str(setAlarmNum)+")"
    			isChanged = True
    		srcInput +=line.replace(srcRep,"Alarm_Manager_Class::Set_Alarm("+str(setAlarmNum)+")")
    		outCSV.writerow([setAlarmNum,filePath,lineNumber,prevLine.rstrip('\r\n')])
    		fileIdx += 1
    	else:
    		srcInput += line
    	prevLine = line
    desFile.close()
    #If we did change something then we need to revise the file otherwise let it be.
    if (isChanged):
    	desFile = open(filePath,'w')
    	desFile.write(srcInput)
    	desFile.close()
    	print("Updated: " + filePath)
    else:
    	print("No Change: " + filePath)
	
def processFiles(fileMap):
	outCSV = csv.writer(open("./myfile.csv","w"), delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
	for dirs, files in fileMap:
		for myFile, idx, isExamined in files:
			if isExamined.upper() == 'Y':
				filePath = dirs + "/"+myFile
				replaceAllSetAlarm(filePath,idx,outCSV)

					
if __name__ == "__main__":
	print("Executing Set_Alarm() Find and Replace")
	#startPath = './dir.txt'
	#updateCPPOnly = False
	parser = OptionParser()
	parser.add_option("-f", "--file", dest="startPath", default="./dir.txt",
                  help="Directory File Path, default: ./dir.txt")
	parser.add_option("-d",
                  action="store_true", dest="updateXMLOnly", default=False,
                  help="Only Generate and/or update the directory map")
	parser.add_option("-c", 
                  action="store_true", dest="updateCPPOnly", default=False,
                  help="Only update .cpp files in directory map, do not update directory map")                  
	(options, args) = parser.parse_args()
	startPath = options.startPath
	updateXMLOnly = options.updateXMLOnly
	updateCPPOnly = options.updateCPPOnly
	#print("Options: " + str(updateXMLOnly) + ", " + str(updateCPPOnly) + ", " + startPath)
	if not os.path.isfile(startPath):
		print("XML does not exist prior therefore only generate XML on this execution, need to rerun to modify .cpp files")
		updateXMLOnly = True
	if updateXMLOnly and updateCPPOnly:
		print("Can not only update XML and only update CPP at same time")
		exit()
	fileMap = genFileMap(startPath,updateCPPOnly)
	if not updateXMLOnly:
		processFiles(fileMap)
		
# Check to see if file map exists... if not create one
# Determine highest file map number
# Update file map, for missing files.  Increment based on highest file map number


# Create new CSV file per run
# Search through files in file map
##  Determine if file needs updates.  Criteria Empty Set_Alarm, Set_Alarm with none matching file number
##  Per file find and replace Set_Alarm with incrementing number and combination of filename
##  Generate update to CSV regardless if we changed anything in the file
