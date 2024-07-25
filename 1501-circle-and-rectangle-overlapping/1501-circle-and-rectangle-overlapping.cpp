class Solution {
public:
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        // Find the closest point to the circle within the rectangle
        int closestX = (xCenter < x1) ? x1 : (xCenter > x2) ? x2 : xCenter;
        int closestY = (yCenter < y1) ? y1 : (yCenter > y2) ? y2 : yCenter;
        
        // Calculate the distance between the circle's center and this closest point
        int distanceX = xCenter - closestX;
        int distanceY = yCenter - closestY;
        
        // If the distance is less than the radius, an overlap exists
        return (distanceX * distanceX + distanceY * distanceY) <= (radius * radius);
    }
};
