public class situationGenerator{
    String characterOne;
    String characterTwo;
    String situation;

    public situationGenerator(String[] characters, String[] situations) {
       int indexOne = (int) (Math.random() * characters.length);
       int indexTwo = (int) (Math.random() * characters.length);
       int indexThree = (int) (Math.random() * situations.length);

       characterOne = characters[indexOne];
       characterTwo = characters[indexTwo];
       situation = situations[indexThree];
    }

    public void displaySituation() {
       String title = characterOne.concat(" and ").concat(characterTwo).concat(" in \"").concat(situation).concat("\"");
       System.out.println(title);
    }

    public static void main(String[] args) {
        String[] characters = {"Edward Elric", "Alphonse Elric", "Roy Mustang", "Winry Rockbell", "Scar", "May Chang", "Lin Yao", "Homunculi", "Solf J. Kimblee", "Shou Tucker", "Father Cornello", "Barry the Chopper", "Van Hohenheim", "Izumi Curtis", "Tim Marcoh", "Roy Mustang\'s squadron", "State Military", "Yoki", "Chimera", "Pinako Rockbell", "Trisha Elric", "Slicer Brothers", "Rose Thomas"};
        String[] situations = {"friends to lovers", "slow burn", "rescue missions", "bed sharing", "teamwork", "fluff", "hurt/comfort", "huddling for warmth", "mutual pining"};
        situationGenerator newSituation = new situationGenerator(characters, situations);
        newSituation.displaySituation();
    }

}