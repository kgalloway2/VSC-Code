// currently working for the single chord I have put in. It can display an example

// tool tips if you want
// swing supports "undo" look into this


import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.UIManager;
import java.util.Hashtable;
// import java.util.Arrays;
// import java.util.Vector;
import java.util.ArrayList;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.FileWriter;
import java.io.IOException;
import javax.swing.filechooser.FileNameExtensionFilter;


public class tabWriter extends JFrame{
    private JTextArea tab;
    private JList<String> savedLicks;
    private JTextArea lickDisplay;
    private JButton addLickToTab;
    private JButton deleteLickFromTab;
    private JButton addLickToList;
    private JButton displayLickButton;
    private JList<String> chords;
    private JList<String> mods;

    private Hashtable<String, String[]> lickMatcher;
    private String[] baseChords = {"A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"};
    private String[] chordMods = {"Maj", "min", "Maj7", "7", "min7", "sus4"};
    
    private Hashtable<String, String[]> chordMatcher = new Hashtable<String, String[]>();
    private ArrayList<String> chordNames = ReadFile("chordNames.txt");
    
    private ArrayList<String> chordFingerings = ReadFile("chordFingerings.txt");
    private String emptyMeasure = "e|--------------\nB|--------------\nG|--------------\nD|--------------\nA|--------------\nE|--------------";
    private String emptyStaff = "e|-\nB|-\nG|-\nD|-\nA|-\nE|-";
    private ArrayList<Integer> lengthsOfAddedLicks;


    public tabWriter() {
        // setup needed lists and dictionaries
        // this creates components needed in the lick create section below
        chords = new JList<String>(baseChords);
        
        mods = new JList<String>(chordMods);

        chordMatcher = new Hashtable<String, String[]>();        
        for (int i = 0; i <= chordNames.size() - 1; i++) {
            String[] currentFingeringList = chordFingerings.get(i).split(",");
            chordMatcher.put(chordNames.get(i), currentFingeringList);
        }
        
        lengthsOfAddedLicks = new ArrayList<Integer>();

        lickMatcher = new Hashtable<String, String[]>();
        ArrayList<String> tempLickList = new ArrayList<String>();
        int count = 1;
        for (String lick : ReadFile("licks.txt")) {
            String[] currentLick = lick.split(",");
            String currentLickName = "lick" + String.valueOf(count);
            lickMatcher.put(currentLickName, currentLick);
            tempLickList.add(currentLickName);
            count++;
        }
        DefaultListModel<String> JListLicks = new DefaultListModel<>();
        for (String lick :tempLickList) {
            JListLicks.addElement(lick);
        }
        savedLicks = new JList<String>(JListLicks);


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
        JMenuItem openItem = new JMenuItem("Open Tab File");
        openItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent evt) {
                FileNameExtensionFilter filter = new FileNameExtensionFilter("Text Files", "txt");               
                JFileChooser fileOpen = new JFileChooser("C:/Users/kgtrm/Desktop/Files/Sheet Music");
                fileOpen.setFileFilter(filter);
                fileOpen.showOpenDialog(null);
                String textArea = "";
                for (String line : ReadFile(fileOpen.getSelectedFile().getAbsolutePath())) {
                    textArea = textArea.concat(line + "\n");
                }
                tab.setText(textArea);
            }
        });
        JMenuItem saveItem = new JMenuItem("Save Tab File");
        saveItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent evt) {
                FileNameExtensionFilter filter = new FileNameExtensionFilter("Only .txt files", "txt");               
                JFileChooser fileSave = new JFileChooser("C:/Users/kgtrm/Desktop/Files/Sheet Music");
                fileSave.setAcceptAllFileFilterUsed(false);
                fileSave.addChoosableFileFilter(filter);
                fileSave.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
                fileSave.showSaveDialog(null);

                String path = fileSave.getSelectedFile().getAbsolutePath();

                try {
                    FileWriter fr = new FileWriter(path, true);
                    fr.write(tab.getText());
                    fr.close();
                } catch (IOException e) {

                }
            }
        });
        fileMenu.add(openItem);
        fileMenu.add(saveItem);
        
        // add menu to menuBar to frame
        menuBar.add(fileMenu);
        setJMenuBar(menuBar);
        
        // tab display panel and components
        // tab display components
        tab = new JTextArea(emptyStaff, 30, 100);
        tab.setFont(new Font("Monospaced", Font.PLAIN, 11));
        JScrollPane tabScroll = new JScrollPane(tab);

        // tab display panel
        JPanel tabPanel = new JPanel();
        tabPanel.add(tabScroll);
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
                    newTab = newTab.replace("\n","|\n");
                    tab.append(newTab);
                } else {
                    for (int i = 0; i <= 5; i++) {
                        lines[currentLength - 6 + i] = lines[currentLength - 6 + i].concat(newLines[i].substring(2)+"|");
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

        addLickToList = new JButton("Add Lick to List");
        addLickToList.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent evt) {
                String lickName = "lick" + String.valueOf(savedLicks.getModel().getSize() + 1);
                // add lick name to list
                JListLicks.addElement(lickName);
                
                // add lick to current list of licks
                String[] lickList = lickDisplay.getText().split("\n");
                lickMatcher.put(lickName, lickList);
                
                // add lick to file
                String lickString = lickList[0];
                for (int i = 1; i <= 5; i++) {
                    lickString = lickString.concat("," + lickList[i]);
                }
                File lickFile = new File("licks.txt");
                try {
                    FileWriter fr = new FileWriter(lickFile, true);
                    BufferedWriter br = new BufferedWriter(fr);
                    br.write("\n" + lickString);
                    br.close();
                    fr.close();
                } catch (IOException e) {

                }
                
            }
        });

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
                String[] currentChord = chordMatcher.get(chords.getSelectedValue().concat(mods.getSelectedValue()));               
                String[] currentLick = lickMatcher.get(savedLicks.getSelectedValue());
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
        setSize(1080, 580);
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

    public String createChord(String[] chord, String[] shape) {
        // for (int i = 0; i <= 5; i++) {
        //     System.out.println(shape[i]);
        // }
        ArrayList<String> result = new ArrayList<String>();
        for (String i : shape) {
            result.add(i);
        }
        for (int i = 0; i <= 5; i++) {
            result.set(i, result.get(i).replace("p", chord[i]));
        }
        String resultString = "";
        for (String i : result) {
            resultString += i + "\n";
        }
        return resultString;
    }

    public ArrayList<String> ReadFile(String fileString) {
        ArrayList<String> fileList = new ArrayList<String>();
        try {
            File currentFile = new File(fileString);
            Scanner reader = new Scanner(currentFile);
            while (reader.hasNextLine()) {
                fileList.add(reader.nextLine());
            } 
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occured.");
            e.printStackTrace();
        } 
        return fileList;
    }

}