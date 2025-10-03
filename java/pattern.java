import java.util.Scanner;

public class PatternChooser {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Choose: 1) Pyramid. 2) Hollow Diamond. 3) Floyd.");
        int choice = sc.nextInt();
        System.out.print("Enter size (e.g., 5): ");
        int n = sc.nextInt();

        switch (choice) {
            case 1:
                for (int i = 1; i <= n; i++) {
                    for (int s = 0; s < n - i; s++) System.out.print(" ");
                    for (int j = 0; j < 2 * i - 1; j++) System.out.print("*");
                    System.out.println();
                }
                break;
            case 2:
                for (int i = 1; i <= n; i++) {
                    for (int s = 0; s < n - i; s++) System.out.print(" ");
                    for (int j = 1; j <= 2 * i - 1; j++) {
                        System.out.print((j == 1 || j == 2 * i - 1) ? "*" : " ");
                    }
                    System.out.println();
                }
                for (int i = n - 1; i >= 1; i--) {
                    for (int s = 0; s < n - i; s++) System.out.print(" ");
                    for (int j = 1; j <= 2 * i - 1; j++) {
                        System.out.print((j == 1 || j == 2 * i - 1) ? "*" : " ");
                    }
                    System.out.println();
                }
                break;
            case 3:
                int num = 1;
                for (int i = 1; i <= n; i++) {
                    for (int j = 1; j <= i; j++) {
                        System.out.print(num++ + " ");
                    }
                    System.out.println();
                }
                break;
            default:
                System.out.println("Invalid choice.");
        }
        sc.close();
    }
}
