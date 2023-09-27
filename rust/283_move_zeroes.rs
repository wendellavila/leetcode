impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        /// Keeps a reference to the position currently
        /// being checked (left_index) and a reference to
        /// the position right before the last zero inclusion
        /// at the end (right_index)
        let mut left_index = 0;
        let mut right_index = nums.len() - 1;

        while left_index < right_index {
            if nums[left_index] == 0 {
                for i in left_index..right_index {
                    nums[i] = nums[i+1];
                }
                nums[right_index] = 0;
                right_index -= 1;
            }
            // second if can't be an else clause
            // it also needs to be run when first if
            // updates value in nums[left_index]
            if nums[left_index] != 0 {
                left_index += 1;
            }
        }
    }
}
