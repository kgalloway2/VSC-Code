import javax.swing.*;

public class guiTests {
    
    public guiTests() {

    }

    private static void placeComponents(JPanel panel) {
        // Layouts will be discussed later. Set to null for now
        panel.setLayout(null);

        // create a label
        JLabel userLabel = new JLabel("User");
        /* This method specififes the location and size
         * of component. setBounds(x, y, width, height)
         * here (x, y) are coordinates from the top ledt
         * corner and remaining two arguments are the width
         * and height of the component.
         */

        userLabel.setBounds(10, 20, 80, 25);
        panel.add(userLabel);

        // Creating text ield where user is supposed to enter user name.
        JTextField userText = new JTextField(20);
        userText.setBounds(100, 20, 165, 25);
        panel.add(userText);

        // Same process for password label and text field.
        JLabel passwordLabel = new JLabel("Password");
        passwordLabel.setBounds(10, 50, 80, 25);
        panel.add(passwordLabel);

        /* This is similar to text field but it hides the user
         * entered data and displays dots instead to protect
         * the password like we normally see on login screens.
         */

        JPasswordField passwordText = new JPasswordField(20);
        passwordText.setBounds(100, 50, 165, 25);
        panel.add(passwordText);

        // Creating login button
        JButton loginButton = new JButton("Login");
        loginButton.setBounds(10, 80, 80, 25);
        panel.add(loginButton);
    
    
    }

    public static void main(String[] args) {
        // create an instance of JFrame
        JFrame frame = new JFrame("My First Swing Example");
        // set the width and height
        frame.setSize(350, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        /* Create a panel. This is the same as a div tag in HTML
         * We can create several panels and add them to specific
         * positions in a JFrame. Inside panels, we can add text
         * fields, buttons, and other components.
         */

        JPanel panel1 = new JPanel();
        // add the panel to the frame
        frame.add(panel1);
        /* call user defined method for adding components
         * to the panel.
         */

        placeComponents(panel1);

        // set the frame visibility to true
        frame.setVisible(true);
    }

    

}
