import java.awt.*;
import java.awt.event.*;

public class AWTPanelDemo extends Frame{
    private Button[] btnNumbers;
    private Button btnHash, btnStar;
    private TextField tfDisplay;

    public AWTPanelDemo() {
        Panel panelDisplay = new Panel(new FlowLayout());
        tfDisplay = new TextField("0", 20);
        panelDisplay.add(tfDisplay);

        Panel panelButtons = new Panel(new GridLayout(4, 3));
        btnNumbers = new Button[10];
        for (int i = 1; i <= 9; i++) {
            btnNumbers[i] = new Button(String.valueOf(i));
            panelButtons.add(btnNumbers[i]);
        }
        btnStar = new Button("*");
        panelButtons.add(btnStar);
        btnNumbers[0] = new Button("0");
        panelButtons.add(btnNumbers[0]);
        btnHash = new Button("#");
        panelButtons.add(btnHash);

        setLayout(new BorderLayout());
        add(panelDisplay, BorderLayout.NORTH);
        add(panelButtons, BorderLayout.CENTER);

        setTitle("BorderLayoutDemo");
        setSize(200, 200);
        setVisible(true);

    }

    public static void main(String[] args) {
        new AWTPanelDemo();
    }
}
