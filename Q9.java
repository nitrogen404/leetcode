import java.util.Scanner;

public class SumOfTenIntegers {

    public static void main(String[] args) {
        int totalSum = readAndSumIntegers();
        System.out.println("The sum is: " + totalSum);
    }

    public static int readAndSumIntegers() {
        Scanner scanner = new Scanner(System.in);
        int sum = 0;  
        for (int i = 1; i <= 10; i++) {
            System.out.print("Enter integer " + i + ": ");
            int input = scanner.nextInt();  
            sum += input; 
        }
        return sum; 
    }
}
