import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AoC_05_2 {

    public static void main(String[] args) throws IOException {
        String[] data = Files.readString(Path.of("i.txt")).split("\\r?\\n\\r?\\n");
        int count = (data[0].split("\\r?\\n")[0].length() + 1) / 4;
        StringBuilder[] stacks = new StringBuilder[count];
        for (int i = 0; i < count; i++) {
            stacks[i] = new StringBuilder();
        }
        String[] stackInput = data[0].split("\\r?\\n");
        for (int i = stackInput.length - 2; i >= 0; i--) {
            String s = stackInput[i];
            for (int j = 0; j < count; j++) {
                if (s.charAt(j * 4 + 1) != ' ') {
                    stacks[j].append(s.charAt(j * 4 + 1));
                }
            }
        }

        Pattern pat = Pattern.compile("move (\\d*) from (\\d*) to (\\d*)");
        String[] moves = data[1].split("\\r?\\n");
        for (int i = 0; i < moves.length; i++) {
            Matcher m = pat.matcher(moves[i]);
            m.find();
            int l = Integer.parseInt(m.group(1));
            int f = Integer.parseInt(m.group(2)) - 1;
            int t = Integer.parseInt(m.group(3)) - 1;

            stacks[t].append(stacks[f].substring(stacks[f].length() - l));
            stacks[f].setLength(stacks[f].length() - l);
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < count; i++) {
            sb.append(stacks[i].charAt(stacks[i].length() - 1));
        }
        System.out.println(sb.toString());
    }

}