def longestPalindromicSubstring(s):
    low=0
    high=0
    start=0
    maxlength=1
    n=len(s)

    for i in range(1,n):
        low=i-1
        high=i

        while low>=0 and high<n and s[low]==s[high]:
            if high-low+1 > maxlength:
                maxlength=high-low+1
                start=low
            low-=1
            high+=1

        low=i-1
        high=i+1  

        while low>=0 and high<n and s[low]==s[high]:
            if high-low+1 > maxlength:
                maxlength=high-low+1
                start=low
            low-=1
            high+=1

    print(s[start:start+maxlength])

longestPalindromicSubstring('sdvracecarkbmh')              
            
