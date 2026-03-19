class Solution {
    public double findMaxAverage(int[] nums, int k) {
        // Calculate the sum of the first 'k' elements
        int sum = 0;
        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }

        // Initialize the maximum average with the average of the first 'k' elements
        double max_avg = (double) sum / k;

        // Slide the window over the array
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k]; // Update the sum by adding the new element and subtracting the element that's left out of the window
            double avg = (double) sum / k;
            max_avg = Math.max(max_avg, avg); // Update the maximum average if the current average is higher
        }

        return max_avg;
    }
}
