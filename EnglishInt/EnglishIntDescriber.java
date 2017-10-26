/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codingpracticeproblems;

import java.util.HashMap;

/* Question: Given any integer, print an English phrase that describes the integer
   10/3/17
    Time: 40 min 
    Complexity: O(nlogn + llogl)

    We will assume we are given a 32 bit signed intger and not a long. Thus, the maximum value of the int is 2^31
    or about 2 billion. So, we do not have to worry about numbers greater than the billions. 
    THe basic form of how to express a number in English is the same up to every third power of ten. 
    e.g. 10 = ten, 1010 = one thousand ten, 1,101,101= one million one hundred one thousand one hunderd 1
    So we shall evaluate the billions, millions, thousands, and hunders in the same way and just 
    add the appropriate power of ten to their descriptor. 
*/
public class EnglishIntDescriber {
    private static HashMap<Integer, String> descriptors;
    
    public static String describeInt(int num) {
        initDescriptors();
        String word = "";
        if(num < 0) {
            word = "Negative ";
            num *= -1; 
        }
        if(num >= 1000000000) {
            int div = (num/1000000000);
            word += convertToWords(div) + " Billion " + describeInt(num%1000000000);
            //word = word.split("Zero")[0];
        }
        else if(num >= 1000000) {
            int div = (num/1000000);
            word += convertToWords(div) + " Million " + describeInt(num%1000000);
        }
        else if(num >= 1000) {
            int div = (num/1000);
            word += convertToWords(div) + " Thousand " + describeInt(num%1000);
        }
        else if(num > 0){
            word += convertToWords(num);
        }
        else {
            return " Zero";
        }
        if(word != null) 
            word = word.split("Zero")[0];
        return word;
    }
    private static String convertToWords(int num) {
        String word;
        if(num >= 100) {
            int div = (num/100);
            word = convertToWords(div) + " Hundred " + convertToWords(num%100);
        }
        else if(num >=20) {
            int div = num - (num%10);
            word = descriptors.get(div) + " " + convertToWords(num%10);
        }
        else {
            word = descriptors.getOrDefault(num, " " + num);
        }
        return word;
    }
    private static void initDescriptors() {
        if(descriptors != null) {
            return;
        }
        descriptors = new HashMap<>();
        descriptors.put(1, "One");
        descriptors.put(2, "Two");
        descriptors.put(3, "Three");
        descriptors.put(4, "Four");
        descriptors.put(5, "Five");
        descriptors.put(6, "Six");
        descriptors.put(7, "Seven");
        descriptors.put(8, "Eight");
        descriptors.put(9, "Nine");
        descriptors.put(10, "Ten");
        descriptors.put(11, "Eleven");
        descriptors.put(12, "Twelve");
        descriptors.put(13, "Thirteen");
        descriptors.put(14, "Fourteen");
        descriptors.put(15, "Fifteen");
        descriptors.put(16, "Sixteen");
        descriptors.put(17, "Seventeen");
        descriptors.put(18, "Eighteen");
        descriptors.put(19, "Nineteen");
        descriptors.put(20, "Twenty");
        descriptors.put(30, "Thirty");
        descriptors.put(40, "Fourty");
        descriptors.put(50, "Fifty");
        descriptors.put(60, "Sixty");
        descriptors.put(70, "Seventy");
        descriptors.put(80, "Eighty");
        descriptors.put(90, "Ninety");
    }
}
