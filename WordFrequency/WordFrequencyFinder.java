/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codingpracticeproblems;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.HashMap;

/**
 * Question: Design a method to find the frequency of occurences of any given word in a book. What if we were running this agorithm multiple times?
 * 
 * 9/20/19
 * 
 * First thought: read every word in the "book" or text file and compare if it is the word we are counting. 
 * If we are running it multiple times, depending on how many times, it may be worth counting every word in the book on the first 
 * go through. Then any subsequent time the method is called, it can be looked up in a hash table in constant time. 
 * 
 * @author Christopher
 */
public class WordFrequencyFinder {
    private HashMap<String, Integer> frequencies;
    
    
    public WordFrequencyFinder(String filename) {
        frequencies = new HashMap();
        findFrequencies(filename);
    }
    
    private void findFrequencies(String filename) {
        if(filename == null) {
            return;
        }
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                for(String word: line.split("\\s+")) {
                    word = word.toLowerCase();
                    if(word.endsWith(".")) {
                        word = word.substring(0, word.length()-1);
                    }
                    Integer freq;
                    if((freq = frequencies.get(word)) != null) {
                        frequencies.replace(word, ++freq);
                    }
                    else {
                        frequencies.put(word, 1);
                    }
                }
            }
        }
        catch(Exception ex) {
            System.out.println(ex.getMessage());
            return;
        }
    }
    
    public Integer getFrequencies(String word) {
        if(word != null && frequencies != null) {
            word = word.trim();
            word = word.toLowerCase();
            if(!word.equals("")) {
                return frequencies.getOrDefault(word, 0);
            }
        } 
        return 0; 
    }
}
