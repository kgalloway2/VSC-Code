import javax.swing.UIManager;
  
public class lookandfeels {    
    public static void main(String[] a)
    {
        UIManager.LookAndFeelInfo[] looks = UIManager.getInstalledLookAndFeels();
        for (UIManager.LookAndFeelInfo look : looks) {
            System.out.println(look.getClassName());
        }
    }
}

// javax.swing.plaf.metal.MetalLookAndFeel
// javax.swing.plaf.nimbus.NimbusLookAndFeel
// com.sun.java.swing.plaf.motif.MotifLookAndFeel
// com.sun.java.swing.plaf.windows.WindowsLookAndFeel
// com.sun.java.swing.plaf.windows.WindowsClassicLookAndFeel