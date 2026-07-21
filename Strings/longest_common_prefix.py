class Solution:
def longestCommonPrefix(self,strs):
if not strs:
return ""
prefix=strs[0]
prefix=strs[1:]:
while prefix!=s[:len(prefix]:
prefix=prefix[:-1]
if prefix =="":
return ""
return prefix
