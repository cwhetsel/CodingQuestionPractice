/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codingpracticeproblems;

import java.util.Map.Entry;
import java.util.Objects;

/**
 * Question: Giver two straight line segments, represented as a start point and an end point, compute the point of intersection
 * Time: 25 minutes 
 * 9/21/17 
 * Complexity O(1)
 * 
 * 
 * Basic algebra. Equation for a line is y = mx + b where m is the change dx/dy and b is the x intercept. 
 * If you have two line equations, you can find the x value they intercept at by (b2-b1)/(m1-m2). 
 * Then plug that value into one of the equations to get the y value. 
 * They will only not intercept if their slopes are equal. 
 * @author Christopher
 */
public class LineIntersectionCalculator {
    
    public static Entry findIntersection(Entry<Double, Double> s1, Entry<Double, Double> e1, Entry<Double, Double> s2, Entry<Double, Double> e2) {
        if(s1 == null || s2 == null || e1 == null || e2 == null) {
            System.out.println("One of the input points was null");
            return null;
        }
        //should also check if lines are horizonal, or if one of them is horizonal to avoid dividing my zero
        Entry<Double, Double> intersect = null; 
        //calculate slopes
        Double m1 = ((e1.getValue() - s1.getValue())/(e1.getKey() - s1.getKey()));
        Double m2 = ((e2.getValue() - s2.getValue())/(e2.getKey() - s2.getKey()));
        
        //calculate x intercepts
        Double b1 = s1.getValue() - (m1 * s1.getKey());
        Double b2 = s2.getValue() - (m2 * s2.getKey());
        
        
        if(Objects.equals(m1, m2)) {
            //if the slopes are equal and the intercepts are the same, then its the same line
            if(Objects.equals(b1, b2)) {
                System.out.println("Lines are the same, infinite intersection points");
                return s1; 
            }
            //they are parallel
            else {
                   System.out.println("Lines are parallel and do not intersect");
                return null;
            }
            
        }
        
        
        
        //calculate x value for intercept 
        Double x = (b2-b1)/(m1-m2);
        
        //find y value for the x value
        Double y = (m1*x) + b1; 
        
        return new java.util.AbstractMap.SimpleEntry<>(x, y);
    }
}
