
using System.Numerics;
using DsaCsharp.Sort;

namespace DsaCsharp.CountingSort;

public class CountingSort<TItem> : ISort<TItem> where TItem : IComparable
{
    /*
    This implementations is not memory efficient if the number maximum value is much larger than the number of unqiue values 
    */

    private int NumBins;
    private int MinItem;
    private int MaxItem;

    public CountingSort(int numBins = -1)
    {
        NumBins = numBins;
    }

    public IList<TItem> Sort(IList<TItem> items)
    {
        throw new NotImplementedException();
        
    }

    public IList<int> Sort(IList<int> items)
    {
        if(items.Count == 0)
        {
            return items;
        }

        // If a bin number is not provided, compute it
        if (NumBins == -1)
        {
            NumBins = ComputeNumBins(items);
            Console.WriteLine($"NumBins: {NumBins}");
        }

        IList<int> frequencies = new List<int>(new int[NumBins]);

        // Count frequencies
        foreach(var item in items){
            frequencies[item]++;
        }

        Console.WriteLine($"frequencies = [{string.Join<int>(",", frequencies)}]");

        // Accumulate frequencies
        for(int i = 1; i < NumBins; i++){
            frequencies[i] = frequencies[i] + frequencies[i-1];
        }

        Console.WriteLine($"frequencies acummulated = [{string.Join<int>(",", frequencies)}]");

        // Order
        IList<int> itemsSorted = new List<int>(new int[items.Count]);
        for(int i = items.Count-1; i >= 0; i--){
            Console.WriteLine($"i = {i}, items[i] = {items[i]}, MinItem = {MinItem}, MaxItem = {MaxItem}, NumBins = {NumBins}, frequencies count: {frequencies.Count}");
            
            if(frequencies[items[i]] > 0)
            {
                itemsSorted[frequencies[items[i]]-1] = items[i];
                frequencies[items[i]]--;
                Console.WriteLine($"itemsSorted = [{string.Join<int>(",", itemsSorted)}]");
            }
            
        }
        return itemsSorted;
    }

    public int ComputeNumBins(IList<int> items)
        {
            MaxItem = items[0];
            MinItem = items[0];

            foreach(var item in items)
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
            return MaxItem + 1;
        }

}