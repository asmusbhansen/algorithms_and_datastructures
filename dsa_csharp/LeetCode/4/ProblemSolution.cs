using DsaCsharp.MergeSort;
using System.Linq;
using System.Net.Mime;

namespace DsaCsharp.LeetCode.Four;

public class FourSolution
{

    public void Test()
    {        
        MergeSort<int> mergeSort = new MergeSort<int>();
        int[] nums1 = [1,6,3,7,4];
        int[] nums2 = [6,3,1,88,];

        nums1 = mergeSort.Sort(nums1.ToList()).ToArray();
        nums2 = mergeSort.Sort(nums2.ToList()).ToArray();

        Console.WriteLine($"nums1 = [{string.Join<int>(",", nums1)}]");
        Console.WriteLine($"nums2 = [{string.Join<int>(",", nums2)}]");

        double median = FindMedianSortedArrays(nums1, nums2);
        Console.WriteLine($"Median: {median}");
        
    }

    public void Merge(int[] itemsSorted, int[] items, int idxBegin, int idxMid, int idxEnd)
    { 
        int i = idxBegin;
        int j = idxMid;

        for (int k = idxBegin; k < idxEnd; k++) {

            bool rightExists = j < idxEnd;
            bool leftExists = i < idxMid;
 
            bool assignLeft = false;
            bool assignRight = false;

            if(leftExists)
            {
                if(rightExists)
                {
                    bool leftSmaller = items[i].CompareTo(items[j]) < 0;
                    if(leftSmaller) assignLeft = true;
                }
                else
                {
                    assignLeft = true;
                }
            }

            if(rightExists)
            {
                assignRight = true;
            }

            if(assignLeft)
            {
                itemsSorted[k] = items[i];
                i = i + 1;
            }
            else if (assignRight)
            {
                itemsSorted[k] = items[j];
                j = j + 1;
            }
        }
    }

    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {

        int[] nums = nums1.Concat(nums2).ToArray();
        int idxBegin = 0, idxMid = nums1.Length, idxEnd = nums1.Length + nums2.Length;
        int[] numsSorted = (int[])nums.Clone();

        Merge(numsSorted, nums, idxBegin, idxMid, idxEnd);

        Console.WriteLine($"numsSorted = [{string.Join<int>(",", numsSorted)}], length = {numsSorted.Length}");

        if(numsSorted.Length % 2 == 0)
        {
            return (double)(numsSorted[numsSorted.Length/2-1]+numsSorted[numsSorted.Length/2])/2;
        }
        else return (double)numsSorted[numsSorted.Length/2];
    }

}