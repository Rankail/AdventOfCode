import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;

public class AoC_04_2 {

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Path.of("i.txt"));
        int n = 0;
        for (String line : lines) {
            List<Integer> r = Arrays.asList(line.split("-|,")).stream().map(e -> Integer.parseInt(e)).toList();
            if ((r.get(0) <= r.get(2) && r.get(2) <= r.get(1))
                    || (r.get(0) <= r.get(3) && r.get(3) <= r.get(1))
                    || (r.get(2) <= r.get(0) && r.get(0) <= r.get(3))
                    || (r.get(2) <= r.get(1) && r.get(1) <= r.get(3))) {
                n++;
            }
        }
        System.out.println(n);
    }

}