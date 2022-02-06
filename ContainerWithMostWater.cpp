class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int area = 0;
        while(left<right)
        {
            int lower = std::min(height[left],height[right]);
            int new_area = (right-left) * lower;
            if(new_area>area)
            {
                area = new_area;
            }
            if(height[left]>height[right])
            {
                right--;
            }
            else
            {
                left++;
            }
                
        }
        return area;
    }
};