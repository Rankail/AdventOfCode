import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class AoC_02_1 {

    public static void main(String[] args) throws IOException {
        List<String> lines = Files.readAllLines(Path.of("i.txt"));
        int sum = 0;
        for (String line : lines) {
            sum += switch (line) {
                case "A X" -> 4;
                case "B X" -> 1;
                case "C X" -> 7;
                case "A Y" -> 8;
                case "B Y" -> 5;
                case "C Y" -> 2;
                case "A Z" -> 3;
                case "B Z" -> 9;
                case "C Z" -> 6;
                default -> 100000000;
            };
        }
        System.out.println(sum);
    }

}
