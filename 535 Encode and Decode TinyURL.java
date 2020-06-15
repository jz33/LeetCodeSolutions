/*
535. Encode and Decode TinyURL
https://leetcode.com/problems/encode-and-decode-tinyurl/

Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service.
There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
*/
public class Codec {
    Map<Integer, String> m_map = new HashMap<>();
    int m_id = 0;
        
    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        m_id++;
        m_map.put(m_id, longUrl);
        return "http:/tinyurl.com/" + m_id;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        int id = Integer.parseInt(shortUrl.replace("http:/tinyurl.com/", ""));
        return m_map.get(id);
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));
