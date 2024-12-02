
import java.io.IOException;
import java.io.ObjectInputStream;
import java.net.Socket;

public class client {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 9876);
            ObjectInputStream objectInputStream = new ObjectInputStream(socket.getInputStream())) {
            System.out.println("Server'a bağlanılıyor...");
            System.out.println();
            while (true) {
                try {
                    Vehicle receivedVehicle = (Vehicle) objectInputStream.readObject();
                    VehicleReader reader = new VehicleReader();
                    reader.myFunc(receivedVehicle);
                    System.out.println();
                } catch (ClassNotFoundException e) {
                    e.printStackTrace();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
