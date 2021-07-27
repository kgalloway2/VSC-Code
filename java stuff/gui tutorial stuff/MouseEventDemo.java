import java.awt.*;
import java.awt.event.*;


public class MouseEventDemo extends Frame{
    private TextField tfMouseX;
    private TextField tfMouseY;

    public MouseEventDemo() {
        setLayout(new FlowLayout());

        add(new Label("X-click: "));

        tfMouseX = new TextField(10);
        tfMouseX.setEditable(false);
        add(tfMouseX);

        add(new Label("Y-Click: "));

        tfMouseY = new TextField(10);
        tfMouseY.setEditable(false);
        add(tfMouseY);

        addMouseListener(new MyMouseListener());

        addWindowListener(new MyWindowListener());

        setTitle("MouseEvent Demo");
        setSize(350, 100);
        setVisible(true);
    }

    public static void main(String[] args) {
        new MouseEventDemo();
    }

    private class MyMouseListener implements MouseListener {
        @Override
        public void mouseClicked(MouseEvent evt) {
            tfMouseX.setText(evt.getX() + "");
            tfMouseY.setText(evt.getY() + "");
        }

        // not used but needed to compile
        @Override public void mousePressed(MouseEvent evt) {}
        @Override public void mouseReleased(MouseEvent evt) {}
        @Override public void mouseEntered(MouseEvent evt) {}
        @Override public void mouseExited(MouseEvent evt) {}
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
