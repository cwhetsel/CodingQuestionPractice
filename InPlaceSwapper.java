/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codingpracticeproblems;

import java.util.List;

/**
 *Question: Can you write a function to swap two numbers in place (without temporary variables)
 * Time To complete: 15 minutes 
 * 9/19/17
 * @author Christopher
 */
public class InPlaceSwapper {
    public void inPlaceSwap(int[] list, int first, int second) {
        if(list == null) {
            System.out.println("List is null");
            return; 
        }
        if(first < 0 || second < 0 || first > list.length-1 || second > list.length-1) {
            System.out.println("Bad indices");
            return;
        }
        if(first == second) {
            return; 
        }
        //Use algebra. You have 3 varibales and 2 knowns at anyone time. That means you can always find out the last variable
        //First, do first + second = sum and put it into the first position. 
        //then to put the first number into the second position, first = sum - second 
        //finally to get the second number back and in the first position, second = sum - first
        list[first] = list[second] + list[first]; 
        list[second] = list[first] - list[second];
        list[first] = list[first] - list[second]; 
        
        
    }
}
