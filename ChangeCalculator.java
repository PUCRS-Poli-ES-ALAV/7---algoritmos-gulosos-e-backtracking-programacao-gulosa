import java.util.ArrayList;
import java.util.List;

public class ChangeCalculator {

    static double[] coins = {1, 0.25, 0.10, 0.05, 0.01};

    public static List<String> change(double x) {
        double amount = x;
        List<String> changeList = new ArrayList<>();

        for (double coin : coins) {
            if (amount <= 0) break;

            int count = 0;
            while (amount >= coin) {
                amount -= coin;
                count++;
            }
            changeList.add("(" + count + ", " + coin + ")");
            System.out.println(amount);

        }

        return changeList;
    }

    public static void main(String[] args) {
        System.out.println(change(2.4));
    }
}
