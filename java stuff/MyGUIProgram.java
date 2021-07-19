import java.awt.Frame;
import java.awt.*;

public class MyGUIProgram extends Frame{
    // private variables

    // Constructor to setup the GUI components and event handlers
    public MyGUIProgram() {
        Label MyLabel = new Label("Test string.", Label.CENTER);
        this.add(MyLabel);

    }


    // The entry main() method
    public static void main(String[] args) {
        Frame testFrame = new MyGUIProgram();
        testFrame.setVisible(true);
        
    }
}
