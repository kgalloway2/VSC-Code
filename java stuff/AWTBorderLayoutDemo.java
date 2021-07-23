import java.awt.*;
import java.awt.event.*;

public class AWTBorderLayoutDemo extends Frame{
    private Button btnNorth, btnSouth, btnCenter, btnEast, btnWest;

    public AWTBorderLayoutDemo() {
        setLayout(new BorderLayout(3, 3));
        
        btnNorth = new Button("Button North");
        add(btnNorth, BorderLayout.NORTH);
        btnSouth = new Button("Button South");
        add(btnSouth, BorderLayout.SOUTH);
        btnCenter = new Button("Button Center");
        add(btnCenter, BorderLayout.CENTER);
        btnEast = new Button("Button East");
        add(btnEast, BorderLayout.EAST);
        btnWest = new Button("Button West");
        add(btnWest, BorderLayout.WEST);


        setTitle("BorderLayout Demo");
        setSize(280, 150);
        setVisible(true);

    }

    public static void main(String[] args) {
        new AWTBorderLayoutDemo();
    }
}
