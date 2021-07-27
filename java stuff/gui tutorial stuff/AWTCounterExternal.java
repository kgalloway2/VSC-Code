import java.awt.*;
import java.awt.event.*;

public class AWTCounterExternal extends Frame {
    private Label lblCount;
    private TextField tfCount;
    private Button btnCount;
    private int count = 0;

    public AWTCounterExternal() {
        setLayout(new FlowLayout());

        lblCount = new Label("Counter");
        add(lblCount);

        tfCount = new TextField(count + "", 10);
        tfCount.setEditable(false);
        add(tfCount);

        btnCount= new Button("Count");
        add(btnCount);

        MyExternalBtnListener listener = new MyExternalBtnListener();
        btnCount.addActionListener(listener);

        setTitle("AWT Counter");
        setSize(250, 100);
        setVisible(true);
    }

    public static void main(String[] args) {
        new AWTCounterExternal();
    }
}

// note that here we add the classes for event handlers outside of our class
// so they are considered external

class MyExternalBtnListener implements ActionListener {
    @Override
    public void actionPerformed(ActionEvent evt) {
        System.out.println("You clocked the button!");
        // ++count;
        // tfCount.setText(count +"");
        // but they can't access those!
    }
}