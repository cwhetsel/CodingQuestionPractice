''' Question: Given two straight line segments, represented as a start point and an end point, compute the point of intersection
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
 '''

class LineIntersectionCalculator():
    @staticmethod
    def findIntersect(s1: "tuple: start point of line1", e1: "tuple:start end point of line2", s2, e2):
        #two vertical lines
        if(s1[0] == e1[0] and s2[0] == e2[0]):
            print("The lines are parallel and do not intersect \n")
            return None
        elif(s1[0] == e1[0]):
            #one vertical line
            m2 = (e2[1] - s2[1])/(e2[0] - s2[0])
            b2 = s2[1] - (m2*s2[0])
            y = (m2 * s1[0]) + b2
            return s1[0], y
        elif(s2[0] == e2[0]):
            #one vertical line
            m1 = (e1[1] - s1[1])/(e1[0] - s1[0])
            b1 = s1[1] - (m1*s1[0])
            y = (m1 * s2[0]) + b1
            return s2[0], y
            
        
        #calc slopes
        m1 = (e1[1] - s1[1])/(e1[0] - s1[0])
        m2 = (e2[1] - s2[1])/(e2[0] - s2[0])

        b1 = s1[1] - (m1*s1[0])
        b2 = s2[1] - (m2*s2[0])

        if(m1 == m2):
            if(b1 == b2):
                print("The lines are the same and thus have infinite solutions \n")
                return s1
            elif(s1 in e1 and s2 in e2):
                print("The input is two points and not line segments  \n")
                return None
            else:
                print("The lines are parallel and do not intersect \n")
                return None

        #calculate x value for intercept 
        x = (b2-b1)/(m1-m2)
        
        #find y value for the x value
        y = (m1*x) + b1 

        return x, y

points = (0.0, 0.0, 2.0, 4.0, -2.0, -2.0, 4.0, 2.0)
print(LineIntersectionCalculator.findIntersect(points[0:2], points[2:4], points[4:6], points[6:8]))
