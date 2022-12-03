import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class AoC_01_1 {

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Path.of("i.txt"));
        int max = 0;
        int partial_sum = 0;
        for (String line : lines) {
            if (line.isEmpty()) {
                partial_sum = 0;
                continue;
            }
            partial_sum += Integer.parseInt(line);
            max = Math.max(max, partial_sum);
        }
        System.out.println(max);
    }
}