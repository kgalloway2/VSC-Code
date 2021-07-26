import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class SwingTemplate extends JFrame {
    public SwingTemplate() {
        Container cp = getContentPane();

        cp.setLayout(new FlowLayout());

        Button btn = new Button("Button");
        cp.add(btn);

        btn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent evt) {
                System.out.println("You pressed the button.");
            }
        });

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        setTitle("......");
        setSize(300, 150);
        setVisible(true);

    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new SwingTemplate();
            }
        });
    }
}
