// currently working for the single chord I have put in. It can display an example
// still need to work on sizing of panels and layout, this should wait until all buttons are added
// add functionality for adding lick to list button
// add save function

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Hashtable;
import java.util.Arrays;
import java.util.ArrayList;


public class tabWriter extends Frame{
    private TextArea tab;
    private List savedLicks;
    private TextArea lickDisplay;
    private Button addLickToTab;
    private Button deleteLickFromTab;
    private Label labLickName;
    private TextField lickNameEntry;
    private Button addLickToList;
    private Button displayLickButton;
    private List chords;
    private List mods;
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
        chords = new List(13);
        for (String i : baseChords) {
            chords.add(i);
        }
        mods = new List(6);
        for (String i : chordMods) {
            mods.add(i);
        }
        lickMatcher = new Hashtable<String, Integer>();
        savedLicks = new List(3);
        for (int i = 0; i <= 2; i++) {
            lickMatcher.put(licks[i][0], i);
            savedLicks.add(licks[i][0]);
        }

        for (int i = 0; i <= chordNames.length - 1; i++) {
            chordMatcher.put(chordNames[i], chordFingerings[i]);
        }
        lengthsOfAddedLicks = new ArrayList<Integer>();

        // frame layout
        setLayout(new BoxLayout(this, BoxLayout.X_AXIS));
        // window listener to close window
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent evt) {
                System.exit(0);
            }
        });
        
        // tab display panel and components
        // tab display components
        tab = new TextArea(emptyStaff, 30, 80);
        tab.setFont(new Font("Monospaced", Font.PLAIN, 11));

        // tab display panel
        Panel tabPanel = new Panel();
        tabPanel.add(tab);
        tabPanel.setSize(600,500);
        add(tabPanel);

        // lick display panel and components
        //lick display components
        addLickToTab = new Button("Add Lick to Tab");
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

        deleteLickFromTab = new Button("Delete Last Lick");
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

        labLickName = new Label("Enter New Lick Name:");
        lickNameEntry = new TextField();
        addLickToList = new Button("Add Lick to List");

        lickDisplay = new TextArea(emptyMeasure,10,20);
        lickDisplay.setFont(new Font("Monospaced", Font.PLAIN, 11));
        
        // lick display panel
        Panel lickDisplayPanel = new Panel();
        lickDisplayPanel.setLayout(new BoxLayout(lickDisplayPanel, BoxLayout.Y_AXIS));
        lickDisplayPanel.add(lickDisplay);
        lickDisplayPanel.add(addLickToTab);
        lickDisplayPanel.add(deleteLickFromTab);
        lickDisplayPanel.add(labLickName);
        lickDisplayPanel.add(lickNameEntry);
        lickDisplayPanel.add(addLickToList);
        lickDisplayPanel.setSize(20, 300);
        add(lickDisplayPanel);


        // lick create panel and components
        // lick create components
        // some components were maded in setup section above
        displayLickButton = new Button("Show Selected Lick");
        displayLickButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent evt) {
                char[] currentChord = chordMatcher.get(chords.getSelectedItem().concat(mods.getSelectedItem()));
                // System.out.println(savedLicks.getSelectedItem());
                // System.out.println(lickMatcher.get(savedLicks.getSelectedItem()));
                // System.out.println(licks[lickMatcher.get(savedLicks.getSelectedItem())][0]);

                String[] currentLick = Arrays.copyOfRange(licks[lickMatcher.get(savedLicks.getSelectedItem())], 1, 7);
                // for (int i = 0; i <= 5; i++) {
                //     System.out.println(currentLick[i]);
                // }
                lickDisplay.setText(createChord(currentChord, currentLick));
            }
        });

        // lick create panel
        Panel chordModPanel = new Panel();
        chordModPanel.setLayout(new BoxLayout(chordModPanel, BoxLayout.Y_AXIS));
        chordModPanel.setSize(20, 300);
        chordModPanel.add(chords);
        chordModPanel.add(mods);
        chordModPanel.add(savedLicks);
        chordModPanel.add(displayLickButton);
        add(chordModPanel);

        // declare display info for frame
        setTitle("Tab Editor");
        setSize(900, 600);
        setVisible(true);

    }

    public static void main(String[] args) {
        new tabWriter();
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
