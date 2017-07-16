import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.io.UnsupportedEncodingException;

/**
 * Created by Jonni on 7/14/2017.
 */
public class OutRedirect {
    private ByteArrayOutputStream baos;
    private PrintStream ps;
    private PrintStream old;

    public OutRedirect() {
        this.baos = new ByteArrayOutputStream();
        this.ps = new PrintStream(baos);
        this.old = System.out;
        System.setOut(this.ps);
    }

    public String getOutput() {
        System.out.flush();
        String s = null;
        try {
            s = this.baos.toString("UTF-8");
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        System.setOut(old);
        return s;
    }

    public PrintStream getStream() {
        return this.ps;
    }
}
