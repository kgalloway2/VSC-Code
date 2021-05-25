public class grayToASCII {
    double[][] oldArray;
    String stringPicture;
    String ASCIIChars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8SB@$";

    public grayToASCII(double[][] grayArray) {
        oldArray = grayArray;
    }

    public char getASCIIValue(double grayscaleValue) {
        int key = (int) (grayscaleValue / 4);
        char character = ASCIIChars.charAt(key);
        return character;
    }

    public String converter() {
        int height = oldArray.length;
        int width = oldArray[0].length;

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                char value = getASCIIValue(oldArray[i][j]);
                stringPicture += value;
                stringPicture += value;
                stringPicture += value;
            }
        }
        return stringPicture;
    }
}
