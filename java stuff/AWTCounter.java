import java.awt.*;
import java.awt.event.*;

public class AWTCounter extends Frame{
    private Label lblCount;
    private TextField tfCount;
    private Button btnCount;
    private int count = 0;

    // constructor
    public AWTCounter() {
        setLayout(new FlowLayout());

        lblCount = new Label("Counter");
        add(lblCount);

        tfCount = new TextField(count + "", 10);
        tfCount.setEditable(false);
        add(tfCount);

        btnCount = new Button("Count");
        add(btnCount);

        BtnCountListener listener = new BtnCountListener();
        btnCount.addActionListener(listener);

        setTitle("AWT Counter");
        setSize(300,100);

        setVisible(true);
    }

    public static void main(String[] args) {
        new AWTCounter();
    }

    // also need another class to handle the "Count" button-click
    private class BtnCountListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent evt) {
            ++count;
            tfCount.setText(count + "");
        }
    }
}
