using System.Collections.ObjectModel;
using System.Security.Cryptography;
using System.Threading.Tasks.Dataflow;

namespace DsaCsharp.LeetCode.EightFourSix;

public static class EightFourSixSolution
{
    public static void Test()
    {

        int[] hand = [1,2,3,6,2,3,4,7,8];
        int groupSize = 3;

        bool result = IsNStraightHand(hand, groupSize);
        Console.WriteLine($"Hand can be divided into K consecutive groups: {result}");
    }

    public static bool IsNStraightHand(int[] hand, int groupSize) {

        IDictionary<int, int> dictionary = new SortedDictionary<int,int>();

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
            //Console.WriteLine($"Card {num} has frequency {dictionary[num]}");
        }

        while(dictionary.Count > 0)
        {
            if(dictionary.Count < groupSize)
            {
                return false;
            }
            int[] keys = dictionary.Keys.ToArray();
            // Take out the lowest key, check that keys k is dict[groupSize]-kdict[0]=groupSize
            //Console.WriteLine($"{keys[0]}, {keys[groupSize-1]}, diff = {keys[groupSize-1]-keys[0]}");

            if(keys[groupSize-1]-keys[0] == groupSize - 1)
            {
                List<int> numGroup = [];
                for(int i = 0; i < groupSize; i++)
                {
                    numGroup.Add(keys[i]);
                    
                    int numCount = dictionary[keys[i]];
                    //Console.WriteLine($"Decreasing num {keys[i]} from {numCount} to {numCount-1}");
                    numCount -= 1;
                    dictionary[keys[i]] = numCount;
                    if (numCount == 0)
                    {
                        dictionary.Remove(keys[i]);
                        //Console.WriteLine($"Deleting num {keys[i]} from dictionary");
                    }
                }

                Console.WriteLine($"Subgroup: [{string.Join<int>(",", numGroup)}]");
            }
            else
            {
                return false;
            }
        }
        
        return true;
    }
}