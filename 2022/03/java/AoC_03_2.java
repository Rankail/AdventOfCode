import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class AoC_03_2 {

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Path.of("i.txt"));
        int n = 0;
        for (int i = 0; i < lines.size(); i += 3) {
            List<String> s1 = new ArrayList<>(Arrays.asList(lines.get(i).split("")));
            List<String> s2 = new ArrayList<>(Arrays.asList(lines.get(i + 1).split("")));
            List<String> s3 = new ArrayList<>(Arrays.asList(lines.get(i + 2).split("")));
            s1.retainAll(s2);
            s1.retainAll(s3);
            if (s1.size() > 0) {
                int c = (int) s1.get(0).charAt(0);
                if (c < 97) {
                    n += c - 65 + 27;
                } else {
                    n += c - 96;
                }
            }
        }
        System.out.println(n);
    }

}
