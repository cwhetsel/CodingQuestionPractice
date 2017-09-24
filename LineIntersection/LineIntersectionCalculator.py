''' Question: Given two straight line segments, represented as a start point and an end point, compute the point of intersection
 * Time: 40 minutes 
 * 9/21/17 
 * Complexity O(1)
 * 
 * 
 * Use Basic algebra to extand the segments and find the intercept. Equation for a line is y = mx + b where m is the change dx/dy and b is the x intercept. 
 * If you have two line equations, you can find the x value they intercept at by (b2-b1)/(m1-m2). 
 * Then plug that value into one of the equations to get the y value. 
 * They will only not intercept if their slopes are equal or if the point of intersection is not in range of the line segments.
 * @author Christopher 
 '''

class LineIntersectionCalculator():
    @staticmethod
    def findIntersect(s1: "tuple: start point of line1", e1: "tuple:start end point of line2", s2, e2):
        #make sure that the x cororident of the start point in smaller than the end. 
        if(s1[0] > e1[0]):
            swap = s1
            s1 = e1
            e1 = swap
        if(s2[0] > e2[0]):
            swap = s2
            s2 = e2
            e2 = swap
        
        #two vertical lines. the x coordinates are equal 
        if(s1[0] == e1[0] and s2[0] == e2[0]):
            #the same vertical line
            if(s1[0] == s2[0] and checkVerticalIntersect(s1, e1, s2, e2) ):
                print("The lines are parallel and intersect. Thus, there are infinite solutions \n")
                return findIntersectParallelV(s1, e1, s2, e2)
            elif(s1[0] == s2[0]):
                print("The line segments are from the same line but do not overlap, thus have no solutions \n")
                return None    
            else:
                print("The line segments are parallel vertical lines, thus have no solutions \n")
                return None   
        elif(s1[0] == e1[0]):
            #one vertical line
            m2 = (e2[1] - s2[1])/(e2[0] - s2[0])
            b2 = s2[1] - (m2*s2[0])
            y = (m2 * s1[0]) + b2
            #check to make sure the intersect is in the range of the line segments
            if(checkIntersect(y, s2, e2) and checkIntersectVert(y, s1[1], e1[1])):
                return s1[0], y
            else:
                print("The line segments have no intersection in this range. Their intersection is (%f, %f) \n", s1[0],y)
                return None
        elif(s2[0] == e2[0]):
            #one vertical line
            m1 = (e1[1] - s1[1])/(e1[0] - s1[0])
            b1 = s1[1] - (m1*s1[0])
            y = (m1 * s2[0]) + b1
            #check to make sure the intersect is in the range of the line segments
            if(checkIntersect(y, s1, e1) and checkIntersectVert(y, s2[1], e2[1])):
                return s2[0], y
            else:
                print("The line segments have no intersection in this range. Their intersection is (%f, %f) \n", s2[0],y)
                return None

            
        
        #calc slopes
        m1 = (e1[1] - s1[1])/(e1[0] - s1[0])
        m2 = (e2[1] - s2[1])/(e2[0] - s2[0])

        b1 = s1[1] - (m1*s1[0])
        b2 = s2[1] - (m2*s2[0])

        #check if lines are parallel
        if(m1 == m2):
            if(b1 == b2):
                if(e1[0] < s2[0] or s1[0] > e[2]):
                    print("The line segments are from the same line but do not overlap, thus have no solutions \n")
                    return None
                else:
                    print("The line segments are from the same line and overlap, thus have infinite solutions \n")
                    return findIntersectParallelH(s1, e1, s2, e2)
            else:
                print("The line segments are parallel and do not intersect \n")
                return None

        #calculate x value for intercept 
        x = (b2-b1)/(m1-m2)
        
        #find y value for the x value
        y = (m1*x) + b1 

        #check that the intersect is on the line segments and not outside of their domain
        if(checkIntersect((x,y), s1, e1) and checkIntersect((x,y), s2, e2)):
            return x, y
        else:
            print("The line segments have no intersection in this range. Their intersection is (%f, %f) \n", x,y)
            return None

    @staticmethod
    def checkIntersect(intersect, start, end):
        #if intersect x value is smaller thatn the start of the range or larger than the end we return false
        if(intersect[0] < start[0] or intersect[0] > end[0]):
            return False
        else:
            return True
        
    @staticmethod
    def checkIntersectVert(intersect, start, end):
        #make the start y smaller
        if(start > end):
            swap = start
            start = end
            end = start
            #if intersect y value is smaller thatn the start of the range or larger than the end we return false
        if(intersect < start or intersect > end):
            return False
        else:
            return True

    @staticmethod
    def checkVerticalIntersect(s1, e1, s2, e2):
        # checks if two vertical line segments from the same line intersect 
        if(e1[1] > s1[1]):
            sy1 = e1[1]
            ey1 = s1[1]
        else:
            sy1 = s1[1]
            ey1 = e1[1]
        if(e2[1] > s2[1]):
            sy2 = e2[1]
            ey2 = s2[1]
        else:
            sy2 = s2[1]
            ey2 = e2[1]
        
        if(ey1 < sy2 or sy1 > ey2):
            return False
        return True

points = (0.0, 0.0, 2.0, 4.0, -2.0, -2.0, 4.0, 2.0)
print(LineIntersectionCalculator.findIntersect(points[0:2], points[2:4], points[4:6], points[6:8]))
