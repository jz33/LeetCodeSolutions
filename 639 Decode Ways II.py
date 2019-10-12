class Solution:
    def numDecodings(self, src: str) -> int:
        if len(src) == 0:
            return 0
        if src[0] == '0':
            return 0      
        if len(src) == 1:
            return 9 if src[0] == '*' else 1
        
        # Use only 3 slots array, because we only care about i, i-1, i-2
        dp = [1, 0, 1]
        dp[0] = 9 if src[0] == '*' else 1

        j = 0
        for i in range(1, len(src)):
            j = (j + 1) % 3
            
            if src[i] == '0':
                if src[i-1] == '*':
                    # * => [1, 2]
                    dp[j] = dp[j-2] * 2
                elif src[i-1] == '1' or src[i-1] == '2':
                    dp[j] = dp[j-2]           
                else:
                    # 0, 3 - 9
                    return 0   

            elif src[i] == '*':
                # At least, src(...i) can be composed by src(...i-1) + [1-9]
                dp[j] = dp[j-1] * 9

                if src[i-1] == '*':
                    # ** can be 15 different composes, [11-19] + [21-26]
                    dp[j] += dp[j-2] * 15
                elif src[i-1] == '1':
                    # [11-19]
                    dp[j] += dp[j-2] * 9
                elif src[i-1] == '2':
                    # * => [21-26]
                    dp[j] += dp[j-2] * 6
                # else: 0, 3-9
                    
            else: # 1-9
                # At least, src(...i) can be composed by src(...i-1) + src[i]
                dp[j] = dp[j-1]
                
                int_i = int(src[i])
                if src[i-1] == '*':
                    if int_i <= 6:
                        # * => [1,2]
                        dp[j] += dp[j-2] * 2
                    else:
                        dp[j] += dp[j-2]
                        
                elif src[i-1] != '0': # [1-9]
                    int2 = int(src[i-1:i+1])
                    if int2 <= 26:
                        dp[j] += dp[j-2]
            
            dp[j] = dp[j] % (10**9+7)
                
        return dp[j] 
