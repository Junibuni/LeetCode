class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        large_nums = ['', 'Thousand ', 'Million ', 'Billion ']

        result = ''
        cnt = 0
        while True:
            chunk = self.number2WordsInChunk(num % 1000)
            ln = large_nums[cnt]
            if chunk == '':
                ln = ''
            result = chunk + ln + result
            num = num // 1000
            if num == 0:
                break
            cnt += 1

        return result.strip()

    def number2WordsInChunk(self, num: int) -> str:
        digits = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        tens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tenths = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        results = ''
        if 99 < num:
            h, num = divmod(num, 100)
            results += digits[h] + ' Hundred '
        
        if num < 20 and 9 < num:
            results += tens[num % 10] + ' '
        else:
            t, num = divmod(num, 10)
            if 2 <= t:
                results += tenths[t] + ' '
            if num > 0:
                results += digits[num] + ' '
        return results