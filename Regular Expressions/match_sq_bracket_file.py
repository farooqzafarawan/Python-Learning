import re
import os

outDir = r'D:\PROJECTS\CWC\MDM Customer\SQLSERVER\CWC_AcuitSparkEDW\StoreProcedures'
srcSQL = os.path.join(outDir,'INSERT_SP.sql')

regex = r"(?:CREATE PROCEDURE)\s+\[(dbo)\]\.(?=\[([\w]+)\])"

procDict = {}
curProcList = []
procName = 'DB_Setting'
with open(srcSQL,'r') as fSQL:
    #sqlText = str(fSQL.readlines())
    for sqlText in fSQL:
        print(sqlText)
        matches = re.finditer(regex, sqlText, re.MULTILINE)
        
        for match in matches:
            procDict[procName]=curProcList[0:-6]
            #print(match, match.group(1), match.group(2))
            procName = match.group(2)

            curProcList.clear()
            
        if procName not in procDict.keys():
            spFile = os.path.join(outDir, procName+'_SP.sql')
            fsp = open(spFile,'w')
        
        fsp.write(sqlText)
        curProcList.append(sqlText)

SPList = [match.group(2) for match in matches]    

for matchNum, match in enumerate(matches, start=1):    
    print (f"Match {matchNum} was found at {match.start()}-{match.end()}: {match.group()}")
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        print (f"Group {groupNum} found at {match.start(groupNum)}-{match.end(groupNum)}: {match.group(groupNum)}" )
