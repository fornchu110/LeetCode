#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
# 要求將url加密後能用解密還原, 也就是做加密映射
# 而不映射也是一種映射
class Codec:
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

