import java.util.Scanner;

public class abc {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a nubmer: ");
        int n = input.nextInt();
        int k = 2;
        int lastSum = 0;
        while (n != 0) {
            if (k > 0) {
                lastSum = lastSum + (n % 10);
                k--;
            }
            n = n / 10;

        }
        System.out.println("Last sum: " + lastSum);
    }
}
