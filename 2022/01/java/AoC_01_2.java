import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class AoC_01_2 {

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Path.of("i.txt"));
        ArrayList<Integer> maxs = new ArrayList<>();
        int partial_sum = 0;
        for (String line : lines) {
            if (line.isEmpty()) {
                maxs.add(partial_sum);
                partial_sum = 0;
                continue;
            }
            partial_sum += Integer.parseInt(line);
        }
        maxs.sort((a, b) -> b - a);
        System.out.println(maxs.get(0) + maxs.get(1) + maxs.get(2));
    }

}
