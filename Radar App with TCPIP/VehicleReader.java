
import java.nio.ByteBuffer;
import java.nio.ByteOrder;

public class VehicleReader {
    public boolean myFunc(Vehicle vehicle) {
 
        byte hexadecimalNumber1 = (byte) 201;
        byte hexadecimalNumber2 = (byte) 10;
        byte hexadecimalNumber3 = (byte) 171;
        byte hexadecimalNumber4 = (byte) 8;

 
        if (vehicle.hexadecimalNumber1 == hexadecimalNumber1 &&
                vehicle.hexadecimalNumber2 == hexadecimalNumber2 &&
                vehicle.hexadecimalNumber3 == hexadecimalNumber3 &&
                vehicle.hexadecimalNumber4 == hexadecimalNumber4) {

           
            System.out.println("Araç: " + vehicle.counter);
            System.out.println("Hexadecimal Number 1: " + String.format("%02x", hexadecimalNumber1));
            System.out.println("Hexadecimal Number 2: " + String.format("%02x", hexadecimalNumber2));
            System.out.println("Hexadecimal Number 3: " + String.format("%02x", hexadecimalNumber3));
            System.out.println("Hız X: " + vehicle.hizX);
            System.out.println("Hız Y: " + vehicle.hizY);
            System.out.println("Hız Z: " + vehicle.hizZ);
            System.out.println("Hedef X: " + vehicle.hedefX);
            System.out.println("Hedef Y: " + vehicle.hedefY);
            System.out.println("Hedef Z: " + vehicle.hedefZ);

            
            byte[] littleEndianBytesForEnlem = ByteBuffer.allocate(4)
                    .order(ByteOrder.LITTLE_ENDIAN)
                    .putInt(vehicle.enlem)
                    .array();

            byte[] bigEndianBytesForEnlem = ByteBuffer.allocate(4)
                    .order(ByteOrder.BIG_ENDIAN)
                    .putInt(vehicle.enlem)
                    .array();

            byte[] littleEndianBytesForBoylam = ByteBuffer.allocate(4)
                    .order(ByteOrder.LITTLE_ENDIAN)
                    .putInt(vehicle.boylam)
                    .array();

            byte[] bigEndianBytesForBoylam = ByteBuffer.allocate(4)
                    .order(ByteOrder.BIG_ENDIAN)
                    .putInt(vehicle.boylam)
                    .array();

            System.out.println("Little Endian:");
            System.out.print("Enlem: ");
            for (byte b : littleEndianBytesForEnlem) {
                System.out.printf("%02x ", b);
            }
            System.out.println();

            System.out.print("Boylam: ");
            for (byte b : littleEndianBytesForBoylam) {
                System.out.printf("%02x ", b);
            }
            System.out.println();

            System.out.println("Big Endian:");
            System.out.print("Enlem: ");
            for (byte b : bigEndianBytesForEnlem) {
                System.out.printf("%02x ", b);
            }
            System.out.println();

            System.out.print("Boylam: ");
            for (byte b : bigEndianBytesForBoylam) {
                System.out.printf("%02x ", b);
            }
            System.out.println();

            System.out.println("Zaman: " + vehicle.zaman);

           
            System.out.println("Hexadecimal Number 4: " + String.format("%02x", hexadecimalNumber4));

            System.out.println();
            System.out.println();

      
            return true;
        } else {
         
            System.out.println("İstenilen araç bulunamadı...");

          
            return false;
        }
    }
}
