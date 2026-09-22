class Solution:
    def sortSentence(self, s) -> str:
        n=s.split()
        
        
        for i in range(0,len(n)):
            for j in range(0,len(n)-1-i):
                if int(n[j][-1])>int(n[j+1][-1]) :
                    n[j],n[j+1]=n[j+1],n[j]
        for m in range(len(n)):
            n[m]=n[m][:-1]
        return " ".join(n)