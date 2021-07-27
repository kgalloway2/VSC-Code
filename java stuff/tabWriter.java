// currently working for the single chord I have put in. It can display an example
// add functionality for adding lick to list button
// add save function
// swing has file chooser
// tool tips if you want
// swing supports "undo" look into this
// a menu bar maybe for loading and saving files

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.UIManager;
import java.util.Hashtable;
import java.util.Arrays;
import java.util.ArrayList;


public class tabWriter extends JFrame{
    private JTextArea tab;
    private JList<String> savedLicks;
    private JTextArea lickDisplay;
    private JButton addLickToTab;
    private JButton deleteLickFromTab;
    private JLabel labLickName;
    private JTextField lickNameEntry;
    private JButton addLickToList;
    private JButton displayLickButton;
    private JList<String> chords;
    private JList<String> mods;
    // there may need to be one big dictionary later with keys of chord names and values of shapes
    private Hashtable<String, Integer> lickMatcher;
    private String[][] licks = {{"lick1", "e-------------","B-------p-----","G-----p---p---","D---p-------p-","A-p-----------","E-------------"},
                                {"lick2", "e---------------","B-p-------p-----","G-----p-------p-","D---p-------p---","A-p-----p-------","E---------------"},
                                {"lick3", "e-------------","B-----p-----p-","G---p-----p---","D-------------","A-p-----------","E-------p-----"}};
    private String[] baseChords = {"A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"};
    private String[] chordMods = {"Maj", "min", "Maj7", "7", "min7", "sus4"};
    private Hashtable<String, char[]> chordMatcher = new Hashtable<String, char[]>();
    private String[] chordNames = {"AMaj","Amin","AMaj7","A7","Amin7","Asus4","A#Maj","A#min","A#Maj7","A#7","A#min7","A#sus4",
                                    "BMaj","Bmin","BMaj7","B7","Bmin7","Bsus4","CMaj","Cmin","CMaj7","C7","Cmin7","Csus4","C#Maj",
                                    "C#min","C#Maj7","C#7","C#min7","C#sus4","DMaj","Dmin","DMaj7","D7","Dmin7","Dsus4","D#Maj",
                                    "D#min","D#Maj7","D#7","D#min7","D#sus4","EMaj","Emin","EMaj7","E7","Emin7","Esus4","FMaj",
                                    "Fmin","FMaj7","F7","Fmin7","Fsus4","F#Maj","F#min","F#Maj7","F#7","F#min7","F#sus4","GMaj",
                                    "Gmin","GMaj7","G7","Gmin7","Gsus4","G#Maj","G#min","G#Maj7","G#7","G#min7","G#sus4"};
    private char[][] chordFingerings = {{'0','2','2','2','0','0'},{'0','1','2','2','0','0'},{'0','2','1','2','0','0'},{'0','2','0','2','0','0'},
    {'0','1','0','2','0','0'},{'0','3','2','2','0','0'},{'1','3','3','3','1','1'},{'1','2','3','3','1','1'},
    {'1','3','2','3','1','1'},{'1','3','1','3','1','1'},{'1','2','1','3','1','1'},{'1','4','3','3','1','1'},
    {'2','4','4','4','2','2'},{'2','3','4','4','2','2'},{'2','4','3','4','2','2'},{'2','0','2','1','2','0'},
    {'2','3','2','4','2','2'},{'2','5','4','4','2','2'},{'0','1','0','2','3','0'},{'0','1','0','1','3','0'},
    {'0','0','0','2','3','0'},{'0','1','3','2','3','0'},{'0','1','3','1','3','0'},{'1','1','0','3','3','0'},
    {'4','6','6','6','4','4'},{'4','5','6','6','4','4'},{'4','6','5','6','4','4'},{'4','6','4','6','4','4'},
    {'4','5','4','6','4','4'},{'4','7','6','6','4','4'},{'2','3','2','0','0','2'},{'1','3','2','0','0','1'},
    {'2','2','2','0','0','2'},{'2','1','2','0','0','2'},{'1','1','2','0','0','1'},{'3','3','2','0','0','2'},
    {'3','4','3','1','1','3'},{'2','4','3','1','1','2'},{'3','3','3','1','1','3'},{'3','2','3','1','1','3'},
    {'2','2','3','1','1','3'},{'4','4','3','1','1','3'},{'0','0','1','2','2','0'},{'0','0','0','2','2','0'},
    {'0','0','1','1','2','0'},{'0','0','1','0','2','0'},{'0','0','0','0','2','0'},{'0','0','2','2','2','0'},
    {'1','1','2','3','3','1'},{'1','1','1','3','3','1'},{'0','1','2','2','3','1'},{'1','3','2','1','3','1'},
    {'1','1','1','1','3','1'},{'1','1','3','3','3','1'},{'2','2','3','4','4','2'},{'2','2','2','4','4','2'},
    {'2','2','3','3','4','2'},{'2','2','3','2','4','2'},{'2','2','2','2','4','2'},{'2','2','4','4','4','2'},
    {'3','0','0','0','2','3'},{'3','3','3','5','5','3'},{'2','0','0','0','2','3'},{'1','0','0','0','2','3'},
    {'3','3','3','3','5','3'},{'3','1','0','0','3','3'},{'4','4','5','6','6','4'},{'4','4','4','6','6','4'},
    {'4','4','5','5','6','4'},{'4','4','5','4','6','4'},{'4','4','4','4','6','4'},{'4','4','6','6','6','4'}};
    private String emptyMeasure = "e--------------\nB--------------\nG--------------\nD--------------\nA--------------\nE--------------";
    private String emptyStaff = "e-\nB-\nG-\nD-\nA-\nE-";
    private ArrayList<Integer> lengthsOfAddedLicks;


    public tabWriter() {
        // setup needed lists and dictionaries
        // this creates components needed in the lick create section below
        chords = new JList<String>(baseChords);
        
        mods = new JList<String>(chordMods);
        
        lickMatcher = new Hashtable<String, Integer>();
        String[] tempLickVector = new String[3];
        for (int i = 0; i <= 2; i++) {
            lickMatcher.put(licks[i][0], i);
            tempLickVector[i] = licks[i][0];
        }
        savedLicks = new JList<String>(tempLickVector);
        
        for (int i = 0; i <= chordNames.length - 1; i++) {
            chordMatcher.put(chordNames[i], chordFingerings[i]);
        }
        lengthsOfAddedLicks = new ArrayList<Integer>();

        // frame layout
        Container cp = getContentPane();
        cp.setLayout(new FlowLayout());
        try {
            UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
        } catch (Exception e) {

        }
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // menu bar
        JMenuBar menuBar = new JMenuBar();
        JMenu fileMenu = new JMenu("File");

        // add items to file menu
        fileMenu.add(new JMenuItem("Open Tab File"));
        fileMenu.add(new JMenuItem("Save This Tab"));
        
        // add menu to menuBar to frame
        menuBar.add(fileMenu);
        setJMenuBar(menuBar);
        
        // tab display panel and components
        // tab display components
        tab = new JTextArea(emptyStaff, 30, 100);
        tab.setFont(new Font("Monospaced", Font.PLAIN, 11));

        // tab display panel
        JPanel tabPanel = new JPanel();
        tabPanel.add(tab);
        cp.add(tabPanel);

        // lick editor panel
        JPanel lickPanel = new JPanel();
        lickPanel.setLayout(new BorderLayout(10,10));
        cp.add(lickPanel);

        // lick display panel and components
        //lick display components
        addLickToTab = new JButton("Add Lick to Tab");
        addLickToTab.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent evt) {
                //current stuff
                String beforeTab = tab.getText();
                String[] lines = beforeTab.split("\n");
                int currentLength = lines.length;
                // System.out.println(currentLength);
                int currentLineLength = lines[currentLength - 1].length();
                // System.out.println(currentLineLength);

                // stuff to add
                String newTab = lickDisplay.getText();
                String[] newLines = newTab.split("\n");
                int newLineLength = newLines[0].length();
                if (currentLineLength + newLineLength >= 80) {
                    tab.append("\n");
                    tab.append(newTab);
                } else {
                    for (int i = 0; i <= 5; i++) {
                        lines[currentLength - 6 + i] = lines[currentLength - 6 + i].concat(newLines[i].substring(1));
                        // System.out.println("changed line to ");
                        // System.out.println(lines[currentLength - 6 + i]);
                    }
                    String afterTab = "";
                    
                    for (String i : lines) {
                        afterTab = afterTab.concat(i + "\n");
                    }
                    // System.out.println(afterTab);
                    tab.setText(afterTab);
                }
                lengthsOfAddedLicks.add(newLineLength);
            }
        });

        deleteLickFromTab = new JButton("Delete Last Lick");
        deleteLickFromTab.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent evt) {
                //current stuff
                String beforeTab = tab.getText();
                String[] lines = beforeTab.split("\n");
                int currentLength = lines.length;
                int currentLineLength = lines[currentLength - 1].length();
                int lengthToDelete = lengthsOfAddedLicks.get(lengthsOfAddedLicks.size() - 1) - 2;
                String afterTab = "";

                if (currentLineLength - lengthToDelete < 5) {
                    if (currentLength <= 7) {
                        afterTab = emptyStaff;
                    } else {
                        for (int i = 0; i <= currentLength - 8; i++) {
                            afterTab = afterTab.concat(lines[i] + "\n");
                        }
                    }
                    
                } else {
                    for (int i = 0; i <= 5; i++) {
                        lines[currentLength - 6 + i] = lines[currentLength - 6 + i].substring(0, currentLineLength - lengthToDelete - 1);
                    } 
                    for (String i : lines) {
                        afterTab = afterTab.concat(i + "\n");
                    }
                }

                tab.setText(afterTab);
                lengthsOfAddedLicks.remove(lengthsOfAddedLicks.size() - 1);
            }
        });

        labLickName = new JLabel("Enter New Lick Name:");
        lickNameEntry = new JTextField();
        addLickToList = new JButton("Add Lick to List");

        lickDisplay = new JTextArea(emptyMeasure,10,20);
        lickDisplay.setFont(new Font("Monospaced", Font.PLAIN, 11));
        
        // lick display subpanel1
        JPanel lickDisplaySubpanel1 = new JPanel();
        lickDisplaySubpanel1.setLayout(new BorderLayout(3, 3));
        lickDisplaySubpanel1.add(lickDisplay, BorderLayout.NORTH);
        lickDisplaySubpanel1.add(addLickToTab, BorderLayout.WEST);
        lickDisplaySubpanel1.add(deleteLickFromTab, BorderLayout.EAST);

        // lick display subpanel2
        JPanel lickDisplaySubpanel2 = new JPanel();
        lickDisplaySubpanel2.setLayout(new BorderLayout(3, 3));
        lickDisplaySubpanel2.add(labLickName, BorderLayout.WEST);
        lickDisplaySubpanel2.add(lickNameEntry, BorderLayout.CENTER);
        lickDisplaySubpanel2.add(addLickToList, BorderLayout.SOUTH);

        // lick display panel
        JPanel lickDisplayPanel = new JPanel();
        lickDisplayPanel.setLayout(new BoxLayout(lickDisplayPanel, BoxLayout.Y_AXIS));
        lickDisplayPanel.add(lickDisplaySubpanel1);
        lickDisplayPanel.add(Box.createRigidArea(new Dimension(0, 15))); // spacing 
        lickDisplayPanel.add(lickDisplaySubpanel2);
        lickDisplayPanel.setSize(20, 300);
        lickPanel.add(lickDisplayPanel, BorderLayout.SOUTH);


        // lick create panel and components
        // lick create components
        // some components were maded in setup section above
        displayLickButton = new JButton("Show Selected Lick");
        displayLickButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent evt) {
                char[] currentChord = chordMatcher.get(chords.getSelectedValue().concat(mods.getSelectedValue()));
                // System.out.println(savedLicks.getSelectedItem());
                
                // System.out.println(lickMatcher.get(savedLicks.getSelectedItem()));
                // System.out.println(licks[lickMatcher.get(savedLicks.getSelectedItem())][0]);

                String[] currentLick = Arrays.copyOfRange(licks[lickMatcher.get(savedLicks.getSelectedValue())], 1, 7);
                // for (int i = 0; i <= 5; i++) {
                //     System.out.println(currentLick[i]);
                // }
                lickDisplay.setText(createChord(currentChord, currentLick));
            }
        });

        // lick create panel
        JPanel chordModPanel = new JPanel();
        JScrollPane scrollChords = new JScrollPane();
        scrollChords.setViewportView(chords);
        JScrollPane scrollMods = new JScrollPane();
        scrollMods.setViewportView(mods);
        JScrollPane scrollSavedLicks = new JScrollPane();
        scrollSavedLicks.setViewportView(savedLicks);
        chordModPanel.setLayout(new BorderLayout(3, 3));
        chordModPanel.setSize(200, 300);
        chordModPanel.add(scrollChords, BorderLayout.WEST);
        scrollChords.setPreferredSize(new Dimension(100,100));
        chordModPanel.add(scrollMods, BorderLayout.CENTER);
        scrollMods.setPreferredSize(new Dimension(100,100));
        chordModPanel.add(scrollSavedLicks, BorderLayout.EAST);
        scrollSavedLicks.setPreferredSize(new Dimension(100,100));
        chordModPanel.add(displayLickButton, BorderLayout.SOUTH);
        lickPanel.add(chordModPanel, BorderLayout.NORTH);

        // declare display info for frame
        setTitle("Tab Editor");
        setSize(1080, 540);
        setVisible(true);

    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new tabWriter();
            }
        });
    }

    public String createChord(char[] chord, String[] shape) {
        // for (int i = 0; i <= 5; i++) {
        //     System.out.println(shape[i]);
        // }
        ArrayList<String> result = new ArrayList<String>();
        for (String i : shape) {
            result.add(i);
        }
        for (int i = 0; i <= 5; i++) {
            result.set(i, result.get(i).replace('p', chord[i]));
        }
        String resultString = "";
        for (String i : result) {
            resultString += i + "\n";
        }
        return resultString;
    }
}
