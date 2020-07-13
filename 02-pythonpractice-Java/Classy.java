// You can use this class to represent how classy someone
// or something is.
// "Classy" is interchangable with "fancy".
// If you add fancy-looking items, you will increase
// your "classiness".
// Create a function in "Classy" that takes a string as
// input and adds it to the "items" list.
// Another method should calculate the "classiness"
// value based on the items.
// The following items have classiness points associated
// with them:
// "tophat" = 2
// "bowtie" = 4
// "monocle" = 5
// Everything else has 0 points.
// Use the test cases below to guide you!

import java.util.ArrayList;
import java.util.List;

public class Classy {
    ArrayList <String> items = new ArrayList <String>();
    public void addItem(String s){
        items.add(s);
    }
    public int classiness(){
        int k = 0;
        String s ="";
        switch(s){
            case "tophat": 
              k = k + 2;
              break;
            case "bowtie":
              k = k + 4;
              break;
            case "monocle":
              k = k + 5;
            default:
              k = k + 0;
        }
        return k;
    }


}

