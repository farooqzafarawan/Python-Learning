import re

regex = r"(?:CREATE PROCEDURE)\s+\[dbo\]\.(?=\[([\w]+)\])"

test_str = ("SET ANSI_NULLS ON\n"
	"GO\n"
	"SET QUOTED_IDENTIFIER ON\n"
	"GO\n\n"
	"CREATE PROCEDURE  [dbo].[SP_DimAccount_DWH] (@Process_ID int)\n"
	"AS\n"
	"-- exec [dbo].[SP_DimAccount_DWH]  1\n"
	"/************************************************************************************************************************************\n"
	"Drop/Create temporary table")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):    
    print (f"Match {matchNum} was found at {match.start()}-{match.end()}: {match.group()}")
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print (f"Group {groupNum} found at {match.start(groupNum)}-{match.end(groupNum)}: {match.group(groupNum)}" )
