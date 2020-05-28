"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。


"""

class Solution:
    def generate(self, numRows: int):
        lines = []
        for row_num in range(numRows):
            row = []
            if row_num == 0:
                row.append(1)
            else:
                row.append(1)
                for i in range(row_num // 2):
                    # 计算上一行对应位置数量和
                    row.append(lines[row_num-1][i]+lines[row_num-1][i+1])
                if row_num % 2 == 0:
                    row.extend(reversed(row[0:-1]))
                else:
                    row.extend(reversed(row))
            lines.append(row)
        return lines

    def generate2(self, numRows: int):
        """
        
        前一行首尾添0 形成两个列表 然后本行等于这两个列表逐位相加
        """
        if numRows == 0: 
            return []

        res = [[1]]
        while len(res) < numRows:
            newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)      
        return res



if __name__ == "__main__":
    test = 5
    s1 = Solution()
    print(s1.generate(test))