
package com.example.gorkem;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;

public class Reader {
    public boolean myFunc(Vehicle vehicle) {
        
        byte hexadecimalNumber1 = (byte) 201;
        byte hexadecimalNumber2 = (byte) 10;
        byte hexadecimalNumber3 = (byte) 171;
        byte hexadecimalNumber4 = (byte) 8;

        if (vehicle.getHexadecimalNumber1() == hexadecimalNumber1 &&
                vehicle.getHexadecimalNumber2() == hexadecimalNumber2 &&
                vehicle.getHexadecimalNumber3() == hexadecimalNumber3 &&
                vehicle.getHexadecimalNumber4() == hexadecimalNumber4) {

            
            System.out.println("Araç: "+ vehicle.getCounter());
            System.out.println("Hexadecimal Number 1: " + String.format("%02x", hexadecimalNumber1));
            System.out.println("Hexadecimal Number 2: " + String.format("%02x", hexadecimalNumber2));
            System.out.println("Hexadecimal Number 3: " + String.format("%02x", hexadecimalNumber3));
            System.out.println("Hız X: " + vehicle.getHizX());
            System.out.println("Hız Y: " + vehicle.getHizY());
            System.out.println("Hız Z: " + vehicle.getHizZ());
            System.out.println("Hedef X: " + vehicle.getHedefX());
            System.out.println("Hedef Y: " + vehicle.getHedefY());
            System.out.println("Hedef Z: " + vehicle.getHedefZ());

            // Little Endian ve Big Endian dönüşümleri
            byte[] littleEndianBytesForEnlem = ByteBuffer.allocate(4)
                    .order(ByteOrder.LITTLE_ENDIAN)
                    .putInt(vehicle.getEnlem())
                    .array();

            byte[] bigEndianBytesForEnlem = ByteBuffer.allocate(4)
                    .order(ByteOrder.BIG_ENDIAN)
                    .putInt(vehicle.getEnlem())
                    .array();

            byte[] littleEndianBytesForBoylam = ByteBuffer.allocate(4)
                    .order(ByteOrder.LITTLE_ENDIAN)
                    .putInt(vehicle.getBoylam())
                    .array();

            byte[] bigEndianBytesForBoylam = ByteBuffer.allocate(4)
                    .order(ByteOrder.BIG_ENDIAN)
                    .putInt(vehicle.getBoylam())
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

            System.out.println("Zaman: " + vehicle.getZaman());

            // Hexadecimal Number 4'ü yazdırma
            System.out.println("Hexadecimal Number 4: " + String.format("%02x", hexadecimalNumber4));

            System.out.println();
            System.out.println();
            System.out.println();
            return true;
        } else {
            
            System.out.println("Istenilen bulunamadı...");
            return false;
        }
    }
}
