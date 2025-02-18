import java.util.Scanner;

public class Assign1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Name Collector
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        
        // Age collection with validation
        int age;
        while (true) {
            System.out.print("Enter your age: ");
            if (scanner.hasNextInt()) {
                age = scanner.nextInt();
                if (age > 0) break;
            } else {
                scanner.next(); // Clear invalid input
            }
            System.out.println("Invalid age. Please enter a positive integer.");
        }
        
        // GPA Collection with Validation
        double gpa;
        while (true) {
            System.out.print("Enter your GPA (0.0 - 4.0): ");
            if (scanner.hasNextDouble()) {
                gpa = scanner.nextDouble();
                if (gpa >= 0.0 && gpa <= 4.0) break;
            } else {
                scanner.next(); // Clear invalid input
            }
            System.out.println("Invalid GPA. Please enter a value between 0.0 and 4.0.");
        }
        
        // Collect Completed Credits
        System.out.print("Enter the number of completed credits: ");
        int completedCredits = scanner.nextInt();
        int remainingCredits = 120 - completedCredits;
        
        // Collect Study Hours for 5 Subjects
        int totalWeeklyHours = 0;
        for (int i = 1; i <= 5; i++) {
            System.out.print("Enter the hours you study per week for subject " + i + ": ");
            totalWeeklyHours += scanner.nextInt();
        }
        
        // To Perform the Calculations
        double avgStudyHoursPerDay = totalWeeklyHours / 7.0;
        int totalStudyHoursPerSemester = totalWeeklyHours * 16;
        
        // Display Output
        System.out.println("\n--- Student Summary ---");
        System.out.printf("Name: %s\n", name);
        System.out.printf("Age: %d\n", age);
        System.out.printf("GPA: %.2f\n", gpa);
        System.out.printf("Completed Credits: %d\n", completedCredits);
        System.out.printf("Remaining Credits: %d\n", remainingCredits);
        System.out.printf("\nAverage Study Hours Per Day: %.2f\n", avgStudyHoursPerDay);
        System.out.printf("Total Study Hours Per Semester: %d\n", totalStudyHoursPerSemester);
        
        scanner.close();
    }
}