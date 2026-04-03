import java.io.BufferedInputStream;
import java.util.Arrays;
import java.util.Locale;

public class Solution {
    static final double INF = 1e100;

    static class FastScanner {
        private final byte[] buffer = new byte[1 << 16];
        private int len;
        private int ptr;

        int read() throws Exception {
            if (ptr >= len) {
                len = System.in.read(buffer);
                ptr = 0;
            }
            return len < 0 ? -1 : buffer[ptr++];
        }

        int nextInt() throws Exception {
            int c;
            do c = read(); while (c <= 32);
            int s = 1;
            if (c == '-') {
                s = -1;
                c = read();
            }
            int v = 0;
            while (c > 32) {
                v = v * 10 + c - '0';
                c = read();
            }
            return v * s;
        }
    }

    static double dist(int x, int hx, int hy) {
        return Math.hypot(x - hx, hy);
    }

    // Write your code here
    public static void main(String args[]) throws Exception {
        Locale.setDefault(Locale.US);
        System.setIn(new BufferedInputStream(System.in));
        FastScanner fs = new FastScanner();
        int n;
        try {
            n = fs.nextInt();
        } catch (Exception e) {
            return;
        }
        int k = fs.nextInt();
        if (n == 0) {
            fs.nextInt();
            fs.nextInt();
            System.out.printf("%.6f%n", 0.0);
            return;
        }

        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = fs.nextInt();
        int hx = fs.nextInt(), hy = fs.nextInt();
        int[] x = a.clone();
        Arrays.sort(x);

        double[] d = new double[n];
        for (int i = 0; i < n; i++) d[i] = dist(x[i], hx, hy);

        double[] nl = new double[n], nr = new double[n], yl = new double[n], yr = new double[n], yh = new double[n];
        Arrays.fill(nl, INF);
        Arrays.fill(nr, INF);
        Arrays.fill(yl, INF);
        Arrays.fill(yr, INF);
        Arrays.fill(yh, INF);

        if (k == n + 1) {
            for (int i = 0; i < n; i++) yl[i] = yr[i] = d[i];
        } else {
            int s = Arrays.binarySearch(x, a[k - 1]);
            nl[s] = nr[s] = 0;
        }

        for (int len = 1; len <= n; len++) {
            int size = n - len + 1;
            for (int l = 0; l < size; l++) {
                int r = l + len - 1;
                yh[l] = Math.min(yh[l], Math.min(nl[l] + d[l], nr[l] + d[r]));
            }
            if (len == n) break;

            double[] nnl = new double[size - 1], nnr = new double[size - 1], nyl = new double[size - 1], nyr = new double[size - 1], nyh = new double[size - 1];
            Arrays.fill(nnl, INF);
            Arrays.fill(nnr, INF);
            Arrays.fill(nyl, INF);
            Arrays.fill(nyr, INF);
            Arrays.fill(nyh, INF);

            for (int l = 0; l < size; l++) {
                int r = l + len - 1;
                if (l > 0) {
                    double dl = x[l] - x[l - 1], sl = x[r] - x[l - 1];
                    nnl[l - 1] = Math.min(nnl[l - 1], Math.min(nl[l] + dl, nr[l] + sl));
                    nyl[l - 1] = Math.min(nyl[l - 1], Math.min(Math.min(yl[l] + dl, yr[l] + sl), yh[l] + d[l - 1]));
                }
                if (r + 1 < n) {
                    double dr = x[r + 1] - x[r], sr = x[r + 1] - x[l];
                    nnr[l] = Math.min(nnr[l], Math.min(nr[l] + dr, nl[l] + sr));
                    nyr[l] = Math.min(nyr[l], Math.min(Math.min(yr[l] + dr, yl[l] + sr), yh[l] + d[r + 1]));
                }
            }
            nl = nnl;
            nr = nnr;
            yl = nyl;
            yr = nyr;
            yh = nyh;
        }

        System.out.printf("%.6f%n", Math.min(yh[0], Math.min(yl[0], yr[0])));
    }
}
