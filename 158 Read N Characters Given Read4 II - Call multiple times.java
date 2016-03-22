public class _158 {

    char[] src;
    int sp = 0;

    private boolean eof = false;
    private char[] buf = new char[4];
    private int p = 0; // position of unconsumed chars in buf
    private int r = 0; // how many chars read from read4

    public int read4(char[] buf) {
        int len = Math.max(0, Math.min(src.length - sp, 4));
        System.arraycopy(src, sp, buf, 0, len);
        sp += len;
        return len;
    }

    public int read(char[] output, int n) {
        int i = 0;
        int len = Math.min(n, r - p);
        System.arraycopy(buf, p, output, i, len);
        i += len;
        p += len;

        for (; i < n && !eof;) {
            r = read4(buf);
            if (r < 4)
                eof = true;
            len = Math.min(n - i, r);
            System.arraycopy(buf, 0, output, i, len);
            i += len;
            p = len;
        }
        return i;
    }

    public _158() {
        src = "abcdefg".toCharArray();

        char[] output = new char[1000];
        int r = 1;
        while (r != 0) {
            r = read(output, 3);
            System.out.println(r + ": " + String.valueOf(output).substring(0, r));
        }
    }

    public static void main(String[] args) {
        new _158();
    }
}
