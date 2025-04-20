
import java.util.Random;

public class VehicleGenerator {
    public static Vehicle generateValue() {
        Random random = new Random();
        Vehicle myVehicle = new Vehicle(
                (byte) 201, // hexadecimalNumber1: Range: 200-201
                (byte) 10,  // hexadecimalNumber2: Range: 9-10
                (byte) 171, // hexadecimalNumber3: Range: 170-171
                (byte) 8,   // hexadecimalNumber4: Range: 7-8
                random.nextDouble() * 100.0,  // hizX: Range: 0.0 to 100.0
                random.nextDouble() * 100.0,  // hizY: Range: 0.0 to 100.0
                random.nextDouble() * 100.0,  // hizZ: Range: 0.0 to 100.0
                random.nextDouble() * 1000.0, // hedefX: Range: 0.0 to 1000.0
                random.nextDouble() * 1000.0, // hedefY: Range: 0.0 to 1000.0
                random.nextDouble() * 1000.0, // hedefZ: Range: 0.0 to 1000.0
                1,
                2,
                System.currentTimeMillis() // zaman: Current system time in milliseconds
        );

        return myVehicle;
    }
}

