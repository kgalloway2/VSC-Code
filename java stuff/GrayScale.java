import java.io.File;
import javax.imageio.ImageIO;
import java.awt.*;  
import java.awt.image.BufferedImage;

public class GrayScale {
    String image;

    public GrayScale(String input_image) {
        image = input_image;
    }
    
    public double[][] convertToGrayScale() {
        BufferedImage old_image;
        double[][] grayArray = new double[1][1];
        try {
           File input = new File("C:/Users/kgtrm/Desktop/Files/Pictures/julia_thing/", image);
           old_image = ImageIO.read(input);
           int width = old_image.getWidth();
           int height = old_image.getHeight();
           grayArray = new double[height][width];
           
           
           for(int i=0; i<height; i++) {
           
              for(int j=0; j<width; j++) {
              
                 Color c = new Color(old_image.getRGB(j, i));
                 int red = (int)(c.getRed()); //  * 0.299);
                 int green = (int)(c.getGreen()); //  * 0.587);
                 int blue = (int)(c.getBlue()); //  *0.114);
                 double newColor = (red + green + blue) / 3;
                 grayArray[i][j] = newColor;
                 // old_image.setRGB(j,i,newColor.getRGB());
              }
           }
        
            // File output = new File("C:/Users/kgtrm/Documents/VSC Code/test_images/", "grayscale1.jpg");
            // ImageIO.write(old_image, "jpg", output);
            
           
        } catch (Exception e) {
            System.out.println("Unable to convert image to grayscale.");
            e.printStackTrace();
        }
        // return "grayscale1.jpg";
        return grayArray;
     }
    
}
