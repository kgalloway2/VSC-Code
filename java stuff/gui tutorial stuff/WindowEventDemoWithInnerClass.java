import java.awt.*;
import java.awt.event.*;

public class WindowEventDemoWithInnerClass extends Frame {
    private TextField tfCount;
    private Button btnCount;
    private int count = 0;

    public WindowEventDemoWithInnerClass() {
        setLayout(new FlowLayout());
        add(new Label("Counter"));
        tfCount = new TextField("0", 10);
        tfCount.setEditable(false);
        add(tfCount);

        btnCount = new Button("Count");
        add(btnCount);
        btnCount.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent evt) {
                ++count;
                tfCount.setText(count + "");;
            }
        });

        // we can also do our winow listener anonymously
        addWindowListener(new WindowListener() {
            @Override
            public void windowClosing(WindowEvent evt) {
                System.exit(0);
            }
            public void windowOpened(WindowEvent evt) { }
            public void windowClosed(WindowEvent evt) { }
            public void windowIconified(WindowEvent evt) { }
            public void windowDeiconified(WindowEvent evt) { }
            public void windowActivated(WindowEvent evt) { }
            public void windowDeactivated(WindowEvent evt) { }

        });

        setTitle("WindowEvent Demo");
        setSize(250, 100);
        setVisible(true);
    }

    public static void main(String[] args) {
        new WindowEventDemoWithInnerClass();
    }
}