import java.awt.*;
import java.awt.event.*;

public class KeyEventDemo extends Frame {
    private TextField tfInput;
    private TextArea taDisplay;

    public KeyEventDemo() {
        setLayout(new FlowLayout());

        add(new Label("Enter Text: "));
        tfInput = new TextField(10);
        add(tfInput);
        taDisplay = new TextArea(5, 40); // 5 rows, 40 columns
        add(taDisplay);

        tfInput.addKeyListener(new MyKeyListener());

        addWindowListener(new MyWindowListener());

        setTitle("KeyEvent Demo");
        setSize(400, 200);
        setVisible(true);

    }

    public static void main(String[] args) {
        new KeyEventDemo();
    }

    public class MyKeyListener implements KeyListener {
        @Override
        public void keyTyped(KeyEvent evt) {
            taDisplay.append("You have typed " + evt.getKeyChar() + "\n");
        }
        // again not used but needed for compilation
        @Override public void keyPressed(KeyEvent evt) { }
        @Override public void keyReleased(KeyEvent evt) { }

    }

    public class MyWindowListener implements WindowListener {
        @Override
        public void windowClosing(WindowEvent evt) {
            System.exit(0);
        }
        @Override public void windowOpened(WindowEvent evt) {}
        @Override public void windowClosed(WindowEvent evt) {}
        @Override public void windowIconified(WindowEvent evt) {}
        @Override public void windowDeiconified(WindowEvent evt) {}
        @Override public void windowActivated(WindowEvent evt) {}
        @Override public void windowDeactivated(WindowEvent evt) {}

    }
}
