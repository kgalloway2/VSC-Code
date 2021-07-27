import java.awt.*;
import java.awt.event.*;


public class WindowEventDemo extends Frame {
    
    private TextField tfCount;
    private Button btnCount;
    private int count = 0;

    // constructor
    public WindowEventDemo() {
        setLayout(new FlowLayout());

        add(new Label("Counter"));

        tfCount = new TextField("0", 10);
        tfCount.setEditable(false);
        add(tfCount);

        btnCount = new Button("Count");
        add(btnCount);

        btnCount.addActionListener(new BtnCountListener());

        addWindowListener(new MyWindowListener());

        setTitle("WindowEvent Demo");
        setSize(300, 100);
        setVisible(true);
    }

    public static void main(String[] args) {
        new WindowEventDemo();
    }

    // define an inner class to handle ActionEvent of btnCount
    private class BtnCountListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent evt) {
            ++count;
            tfCount.setText(count + "");
        }
    }

    private class MyWindowListener implements WindowListener {
        @Override
        public void windowClosing(WindowEvent evt) {
            System.exit(0);
        }
        // the following are not used but are needed to compile
        @Override public void windowOpened(WindowEvent evt) {}
        @Override public void windowClosed(WindowEvent evt) {}
        // the following are for debugging
        @Override public void windowIconified(WindowEvent evt) {System.out.println("Window Iconified"); }
        @Override public void windowDeiconified(WindowEvent evt) {System.out.println("Window Deiconified"); }
        @Override public void windowActivated(WindowEvent evt) {System.out.println("Window Activated"); }
        @Override public void windowDeactivated(WindowEvent evt) {System.out.println("Window Deactivated"); }

    }
}
