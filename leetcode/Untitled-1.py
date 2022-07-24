
def findLUSlength(strs) -> int:
    # 设计一个双重循环
    specialList = []
    i = 0
    n = len(strs)
    while i < n:
        flag = 1
        for j in range(n):
            if i == j:
                continue
            # 判断i 是否为j的子序列
            slow = fast = 0
            while slow < len(strs[i]) and fast < len(strs[j]):
                if strs[i][slow] == strs[j][fast]:
                    fast += 1
                slow += 1
            if fast == len(strs[i]):
                flag = 0
                break
        if flag == 1:
            specialList.append(strs[i])
        i+=1
    if len(specialList) == 0:
        return -1
    else:
        ans = -1
        for i in specialList:
            ans = max(ans, len(i))
        return ans

ans = findLUSlength(["aabbcc", "aabbcc","c"])