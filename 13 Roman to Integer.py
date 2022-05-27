class Solution:
    def romanToInt(self, s):
        result = 0
        dictu = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dictu1 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        n = len(s)
        a = 0
        b = a + 1
        while b <= n - 1:
            x = s[a] + s[b]
            if x in dictu1:
                result += dictu1[x]
                a += 2
            else:
                result += dictu[s[a]]
                a += 1
            b = a + 1
        if a == n - 1:
            result += dictu[s[n-1]]
        return result
