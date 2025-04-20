import java.io.IOException;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class server {
    public static void main(String[] args) {
        final int PORT = 9876;
        ServerSocket serverSocket = null;

        try {
            serverSocket = new ServerSocket(PORT);
            System.out.println("Sunucu başlatıldı. Bağlantılar bekleniyor...");

            while (true) {
                Socket socket = serverSocket.accept();
                System.out.println("Yeni istemci bağlantısı: " + socket);

                try {
                    ObjectOutputStream objectOutputStream = new ObjectOutputStream(socket.getOutputStream());
                    // Sonsuz döngü içinde araç üretimi ve istemciye gönderimi
                    int myCounter=1;
                    while (true) {
                        Vehicle vehicle = VehicleGenerator.generateValue();
                        vehicle.counter=myCounter;
                        objectOutputStream.writeObject(vehicle);
                        objectOutputStream.flush(); // Veriyi hemen göndermek için flush() kullanın
                        System.out.println("Araç istemciye gönderildi.");
                        Thread.sleep(1000); // 1 saniye bekle
                        myCounter+=1;
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                    break; // Hata durumunda iç döngüyü sonlandır
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            // Sunucu soketini kapat
            if (serverSocket != null && !serverSocket.isClosed()) {
                try {
                    serverSocket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}