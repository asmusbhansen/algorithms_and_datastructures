using DsaCsharp.CountingSort;

namespace DsaCsharp.LeetCode.SevenFive;

public class SevenFiveSolution {

    public void Test() 
    {
        /*
        int[] nums = [2,0,2,1,1,0];//[2,0,2,1,1,0];

        Console.WriteLine($"nums = [{string.Join<int>(",", nums)}]");

        CountingSort<int> countingSort = new CountingSort<int>();
        nums = countingSort.Sort(nums).ToArray();

        Console.WriteLine($"nums = [{string.Join<int>(",", nums)}]");
        */

        //SortColors(nums);
        int arr_length = 100;
        for(int l = 0; l < 10; l++)
        {
            int[] testNums = new int[arr_length]; 

            Random randNum = new Random();
            for (int i = 0; i < testNums.Length; i++)
            {
                testNums[i] = randNum.Next(0, arr_length);
            }

            CountingSort<int> countingSort = new CountingSort<int>();

            Console.WriteLine($"testNums = [{string.Join<int>(",", testNums)}], Is sorted: {IsSorted(testNums)}");
            testNums = countingSort.Sort(testNums).ToArray();

            Console.WriteLine($"testNums = [{string.Join<int>(",", testNums)}], Is sorted: {IsSorted(testNums)}");
        }
        
    }

    public bool IsSorted(int[] nums)
    {
        for(int i = 0; i < nums.Length-1; i++)
        {
            if(nums[i] > nums[i+1]) return false;
        }
        return true;
    }

    private int NumBins;
    private int MinItem;
    private int MaxItem;
    
    public void SortColors(int[] nums) {
    
        if(nums.Length == 0)
        {
            return;
        }

        NumBins = ComputeNumBins(nums);

        IList<int> frequencies = new List<int>(new int[NumBins]);

        // Count frequencies
        foreach(var item in nums){
            frequencies[item-MinItem]++;
        }

        // Order
        int count = 0;
        for(int i = 0; i < frequencies.Count; i++){
            while(frequencies[i] > 0)
            {
               
                nums[count] = i + MinItem;
                
                frequencies[i]--;
                count++;
            }
        }
    }

    public int ComputeNumBins(int[] nums)
    {
        MaxItem = nums[0];
        MinItem = nums[0];

        foreach(var item in nums)
        {
            if(item.CompareTo(MaxItem) == 1)
            {
                MaxItem = item;
            }
            else if(item.CompareTo(MinItem) == -1)
            {
                MinItem = item;
            }
        }
        return MaxItem - MinItem + 1;
    }
}