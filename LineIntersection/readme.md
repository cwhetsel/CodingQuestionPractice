# Question: Given two straight line segments, represented as a start point and an end point, compute the point of intersection
### Time: 25 minutes 
### 9/21/17 
### Complexity O(1)

___

 * Basic algebra. Equation for a line is y = mx + b where m is the change dx/dy and b is the x intercept. 
 * If you have two line equations, you can find the x value they intercept at by (b2-b1)/(m1-m2). 
 * Then plug that value into one of the equations to get the y value. 
 * They will only not intercept if their slopes are equal. 
 * @author Christopher 
