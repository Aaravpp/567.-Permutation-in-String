Intuition:

We need to determine if any permutation of s1 exists in s2.
Instead of generating all permutations (which is very slow), we use the idea that:
Two strings are permutations of each other if their character frequencies match.

So, we:

Count frequencies of s1
Use a sliding window of size s1.length on s2
Compare frequency arrays

Approach:

1. Edge Case
  If s1.length > s2.length, return false
2. Frequency Arrays
  hashS: stores frequency of characters in s1
  hashW: stores frequency of current window in s2
3. Initialize First Window
  Fill both arrays for first windowLength characters
4. Sliding Window
  Maintain two pointers:
  i → start of window
  j → end of window
  For every step:
  Compare frequency arrays
  Remove left character (i)
  Move window forward
  Add new right character (j)
5. Optimization in Your Code
  You correctly added:
    if(j < s2.length)

    to avoid out-of-bounds access ✅

6. Return
  If any match → true
  Otherwise → false

Complexity: 
  Time complexity: O(n×26)≈O(n)
  Space complexity:O(1) (constant 26-size arrays)
