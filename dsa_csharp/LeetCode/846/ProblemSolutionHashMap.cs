using System.Collections.ObjectModel;
using System.Security.Cryptography;
using System.Threading.Tasks.Dataflow;

using DsaCsharp.BinarySearchTree;

namespace DsaCsharp.LeetCode.EightFourSixHashMap;

public static class EightFourSixHashMapSolution
{
    public static void Test()
    {

        int[] hand = [9,13,15,23,22,25,4,4,29,15,8,23,12,19,24,17,18,11,22,24,17,17,10,23,21,18,14,18,7,6,3,6,19,11,16,11,12,13,8,26,17,20,13,19,22,21,27,9,20,15,20,27,8,13,25,23,22,15,9,14,20,10,6,5,14,12,7,16,21,18,21,24,23,10,21,16,18,16,18,5,20,19,20,10,14,26,2,9,19,12,28,17,5,7,25,22,16,17,21,11];//[1,2,3,6,2,3,4,7,8];//[1,2,3,4,5];//[8,10,12];//
        int groupSize = 10;

        bool result = IsNStraightHand(hand, groupSize);
        Console.WriteLine($"Hand can be divided into K consecutive groups: {result}");
    }

    public static bool IsNStraightHand(int[] hand, int groupSize) {
        // Create dictionary
        IDictionary<int, int> dictionary = new Dictionary<int,int>();

        //Sort hand
        Array.Sort(hand);

        if(hand.Length % groupSize != 0) {return false;}

        foreach(int num in hand)
        {
            int numCount;
            bool foundNum = dictionary.TryGetValue(num, out numCount);

            if(foundNum)
            {
                dictionary[num] = numCount + 1;
            }     
            else
            {
                dictionary.Add(num, 1);
            }       
        }


        while(dictionary.Count > 0)
        {         
            if(dictionary.Count < groupSize)
            {
                return false;
            }

            int[] keys = dictionary.Keys.ToArray();

            // Take out the lowest(First) key, check that keys k is dict[groupSize]-kdict[0]=groupSize
            if(keys[groupSize-1]-keys[0] == groupSize - 1)
            {
                for(int i = 0; i < groupSize; i++)
                {
                    Console.WriteLine($"Getting key {keys[i]} from dictionary. i = {i}");   
                    int numCount = dictionary[keys[i]];
                    Console.WriteLine($"Decreasing num {keys[i]} from {numCount} to {numCount-1}");
                    numCount -= 1;
                    dictionary[keys[i]] = numCount;
                    if (numCount <= 0)
                    {
                        dictionary.Remove(keys[i]);
                        Console.WriteLine($"Deleting num {keys[i]} from dictionary");
                    }
                }

                //Console.WriteLine($"Subgroup: [{string.Join<int>(",", numGroup)}]");
            }
            else
            {
                return false;
            }
        }

        return true;
    }
}