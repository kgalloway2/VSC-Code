import java.awt.Image;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.awt.*;  
import javax.swing.JFrame;
import java.awt.image.BufferedImage;

public class picToASCII extends Canvas{
    String image;

    public picToASCII(String input_image) {
        image = input_image;
    }
    
    public void paint(Graphics g) {
        try {
            BufferedImage bi = ImageIO.read(new File("C:/Users/kgtrm/Desktop/Files/Pictures/julia_thing/", image));
            // Image newResizedImage = bi.getScaledInstance(256, 256, Image.SCALE_SMOOTH); 
            g.drawImage(bi, 0, 0, this);
        } catch (IOException e) {
            String workingDir = System.getProperty("user.dir");
            System.out.println("Current working directory : " + workingDir);
            e.printStackTrace();
        }     
    }


    public static void main(String[] args){
        String picture = "grookey.png";
        int height = 0;
        int width = 0;
        try {
            BufferedImage bi = ImageIO.read(new File("C:/Users/kgtrm/Desktop/Files/Pictures/julia_thing/", picture));
            height = bi.getHeight();
            width = bi.getWidth();
        }
        catch (IOException e) {
            String workingDir = System.getProperty("user.dir");
            System.out.println("Current working directory : " + workingDir);
            e.printStackTrace();
        }

        // view original picture
        System.out.println("Displaying original picture.");
        Canvas m = new picToASCII(picture);  
        JFrame f = new JFrame();  
        f.add(m);  
        f.setSize(width, height);  
        f.setVisible(true);  
        System.out.println("Original picture displayed.");

        // change picture to grayscale
        System.out.println("Converting image to grayscale.");
        GrayScale grayMethod = new GrayScale(picture);
        double[][] newPicture = grayMethod.convertToGrayScale();
        System.out.println("Image converted to grayscale.");

        // change grayscale to ascii
        System.out.println("Converting grayscale to ascii.");
        grayToASCII ASCIIMethod = new grayToASCII(newPicture);
        String ASCIIPicture = ASCIIMethod.converter();
        System.out.println("Converted grayscale to ascii.");

        // view new picture
        System.out.println("Displaying new picture.");
        JFrame g = new JFrame();  
        TextArea ascii;  
        ascii = new TextArea("");  
        ascii.setFont(new Font("monospaced", Font.PLAIN, 1));
        String currentLine;
        for (int i = 0; i < height; i++) {
            currentLine = "";
            for (int j = 0; j < 3 * width; j++) {
                currentLine += String.valueOf(ASCIIPicture.charAt(i * 3 * width + j));
            }
            ascii.append("\n");
            ascii.append(currentLine);
        }
        g.add(ascii);
        g.setSize(3 * width, 3 * height); 
        g.setVisible(true);
        System.out.println("New picture displayed!");
        
    }

}