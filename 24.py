def isAnagram(str1, str2):
    s1 = sorted(list(str1), key=str.lower)
    s2 = sorted(list(str2), key=str.lower)
    if len(s1) != len(s2):
        print "Length difference"
        return False
    if s1 == s2:
        return True
    else:
        return False

print "Enter two strings and I'll tell you if they are anagrams:"
str1 = str(raw_input("Enter the first string: "))
str2 = str(raw_input("Enter the second string: "))

if isAnagram(str1, str2):
    print '"{}" and "{}" are anagrams.'.format(str1, str2)
else:
    print '"{}" and "{}" are not anagrams.'.format(str1, str2)