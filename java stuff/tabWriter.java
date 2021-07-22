// currently working for the single chord I have put in. It can display an example
// still need to add all chords, fix font in everything

import java.awt.*;
import java.awt.event.*;
import java.util.Hashtable;
import java.util.Arrays;
import java.util.ArrayList;

public class tabWriter extends Frame{
    private TextArea tab;
    private List savedLicks;
    private TextArea lickDisplay;
    private Button addLick;
    private Button displayLickButton;
    private List chords;
    private List mods;
    // there may need to be one big dictionary later with keys of chord names and values of shapes
    private Hashtable<String, Integer> lickMatcher;
    private String[][] licks = {{"lick1", "e--------------","B--------p-----","G------p---p---","D----p-------p-","A--p-----------","E--------------"},
                                {"lick2", "e----------------","B--p-------p-----","G------p-------p-","D----p-------p---","A--p-----p-------","E----------------"},
                                {"lick3", "e--------------","B------p-----p-","G----p-----p---","D--------------","A--p-----------","E--------p-----"}};
    private String[] baseChords = {"A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"};
    private String[] chordMods = {"Maj", "min", "Maj7", "7", "min7", "sus4"};
    private Hashtable<String, char[]> chordMatcher = new Hashtable<String, char[]>();
    private String emptyMeasure = "e--------------\nB--------------\nG--------------\nD--------------\nA--------------\nE--------------";


    public tabWriter() {
        setLayout(new GridLayout(0, 3));
        tab = new TextArea(emptyMeasure, 30, 50);
        Panel tabPanel = new Panel();
        tabPanel.add(tab);
        tabPanel.setSize(300,500);
        add(tabPanel);

        addLick = new Button("Add Lick");
        addLick.addActionListener(new ActionListener() {
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
            }
        });

        lickDisplay = new TextArea(emptyMeasure,10,30);
        Panel lickDisplayPanel = new Panel();
        lickDisplayPanel.add(lickDisplay);
        lickDisplayPanel.add(addLick);
        lickDisplayPanel.setSize(50, 300);
        add(lickDisplayPanel);

        // create needed lists
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
        char[] temp = {'0','3','2','0','1','0'};
        chordMatcher.put("CMaj", temp);

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

        Panel chordModPanel = new Panel();
        chordModPanel.setLayout(new GridLayout(3,0));
        chordModPanel.add(chords);
        chordModPanel.add(mods);
        chordModPanel.add(savedLicks);
        chordModPanel.add(displayLickButton);
        add(chordModPanel);


        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent evt) {
                System.exit(0);
            }
        });

        setTitle("Tab Editor");
        setSize(1200, 600);
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
