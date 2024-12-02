
package com.example.gorkem;

import java.util.Random;

import java.time.*;

public class Main {
    public static void main(String[] args) {
        LocalDate ld = LocalDate.of(1970, 1, 1);
        Reader myReader = new Reader();
        int mycounter=0;
        while (true) {
            Vehicle newVehicle = generateValue();
            newVehicle.counter=mycounter;
            boolean myBool = myReader.myFunc(newVehicle);
            if (myBool) {
                try {
                    Thread.sleep(3000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                mycounter+=1;
            }
        }
    }

    public static Vehicle generateValue() {
        Random random = new Random();
        Vehicle myVehicle = new Vehicle(
                (byte) (201), 
                (byte) (10),  
                (byte) (171), 
                (byte) (8),   
                random.nextDouble() * 100.0,      
                random.nextDouble() * 100.0,      
                random.nextDouble() * 100.0,      
                random.nextDouble() * 1000.0,     
                random.nextDouble() * 1000.0,     
                random.nextDouble() * 1000.0,     
                1,
                2,
                System.currentTimeMillis()       
        );

        return myVehicle;
    }
}
