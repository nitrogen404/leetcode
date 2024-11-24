public class BoilerPressureCheck {

    public static void main(String[] args) {
        int boiler_pressure = 1050;
        if (boiler_pressure > 1000) {
            System.out.println("Alarm: Boiler Pressure: TOO HIGH");
        } else if (boiler_pressure < 100) {
            System.out.println("Boiler Pressure: TOO LOW");
        } else {
            System.out.println("Boiler Pressure: within normal limits");
        }
    }
}
