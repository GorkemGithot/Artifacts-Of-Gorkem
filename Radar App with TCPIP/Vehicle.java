
import java.io.Serializable;

public class Vehicle implements Serializable {
    private static final long serialVersionUID = 1L;

    public byte hexadecimalNumber1;
    public byte hexadecimalNumber2;
    public byte hexadecimalNumber3;
    public byte hexadecimalNumber4;
    public double hizX;
    public double hizY;
    public double hizZ;
    public int enlem;
    public int boylam;
    public double hedefX;
    public double hedefY;
    public double hedefZ;
    public long zaman;
    public int counter = 1;

    public Vehicle(byte hexadecimalNumber1, byte hexadecimalNumber2, byte hexadecimalNumber3, byte hexadecimalNumber4,
                   double hizX, double hizY, double hizZ,
                   double hedefX, double hedefY, double hedefZ,
                   int enlem, int boylam,
                   long zaman) {
        this.hexadecimalNumber1 = hexadecimalNumber1;
        this.hexadecimalNumber2 = hexadecimalNumber2;
        this.hexadecimalNumber3 = hexadecimalNumber3;
        this.hexadecimalNumber4 = hexadecimalNumber4;
        this.hizX = hizX;
        this.hizY = hizY;
        this.hizZ = hizZ;
        this.enlem = enlem;
        this.boylam = boylam;
        this.hedefX = hedefX;
        this.hedefY = hedefY;
        this.hedefZ = hedefZ;
        this.zaman = zaman;
    }

    



    public byte getHexadecimalNumber1() {
        return hexadecimalNumber1;
    }

    public byte getHexadecimalNumber2() {
        return hexadecimalNumber2;
    }

    public byte getHexadecimalNumber3() {
        return hexadecimalNumber3;
    }

    public byte getHexadecimalNumber4() {
        return hexadecimalNumber4;
    }

    public double getHizX() {
        return hizX;
    }

    public double getHizY() {
        return hizY;
    }

    public double getHizZ() {
        return hizZ;
    }

    public double getHedefX() {
        return hedefX;
    }

    public double getHedefY() {
        return hedefY;
    }

    public double getHedefZ() {
        return hedefZ;
    }

    public int getEnlem() {
        return enlem;
    }

    public int getBoylam() {
        return boylam;
    }

    public long getZaman() {
        return zaman;
    }

    public int getCounter() {
        return counter;
    }
}
