import java.awt.*;
import java.awt.event.*;

public class MouseMotionDemo extends Frame {
    private TextField tfMouseClickX;
    private TextField tfMouseClickY;
    private TextField tfMousePositionX;
    private TextField tfMousePositionY;

    public MouseMotionDemo() {
        setLayout(new FlowLayout());

        add(new Label("X-Click: "));
        tfMouseClickX = new TextField(10);
        tfMouseClickX.setEditable(false);
        add(tfMouseClickX);
        add(new Label("Y-Click: "));
        tfMouseClickY = new TextField(10);
        tfMouseClickY.setEditable(false);
        add(tfMouseClickY);

        add(new Label("X-Position: "));
        tfMousePositionX = new TextField(10);
        tfMousePositionX.setEditable(false);
        add(tfMousePositionX);
        add(new Label("Y-Position: "));
        tfMousePositionY = new TextField(10);
        tfMousePositionY.setEditable(false);
        add(tfMousePositionY);

        MyMouseListener listener = new MyMouseListener();
        addMouseListener(listener);
        addMouseMotionListener(listener);

        addWindowListener(new MyWindowListener());

        setTitle("MouseMotion Demo");
        setSize(400, 120);
        setVisible(true);
    }

    public static void main(String[] args) {
        new MouseMotionDemo();
    }

    // define an inner class for both the mouse click and motion
    // recall taht java classes can extend only one class, but implement many interfaces
    private class MyMouseListener implements MouseListener, MouseMotionListener {
        @Override 
        public void mouseClicked(MouseEvent evt) {
            tfMouseClickX.setText(evt.getX() + "");
            tfMouseClickY.setText(evt.getY() + "");
        }

        // not used but needed for compilation
        @Override public void mousePressed(MouseEvent evt) { }
        @Override public void mouseReleased(MouseEvent evt) { }
        @Override public void mouseEntered(MouseEvent evt) { }
        @Override public void mouseExited(MouseEvent evt) { }

        // the following are for the motion of the mouse
        @Override
        public void mouseMoved(MouseEvent evt) {
            tfMousePositionX.setText(evt.getX() + "");
            tfMousePositionY.setText(evt.getY() + "");
        }

        // again not used but needed for compilation
        @Override public void mouseDragged(MouseEvent evt) { }

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
