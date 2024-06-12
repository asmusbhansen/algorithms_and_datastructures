
using System.Globalization;
using System.Reflection.Metadata;
using DsaCsharp.Sort;

namespace DsaCsharp.MergeSort;

public class MergeSort<TItem> : ISort<TItem> where TItem : IComparable
{
    public IList<TItem> Sort(IList<TItem> items)
    {
        IList<TItem> itemsSorted = items.ToList();
        Split(items, itemsSorted, 0, itemsSorted.Count);
        return itemsSorted;
    }
    public void Split(IList<TItem> itemsSorted, IList<TItem> items, int idxBegin, int idxEnd)
    {

        if (idxEnd - idxBegin <= 1)
        {
            //Console.WriteLine("--- Returning! ---");
            return; // Arrays of length 1 is sorted by definition 
        } 

        int idxMid = (idxEnd + idxBegin) / 2;
        //Console.WriteLine($"Split - idxBegin: {idxBegin}, idxMid: {idxMid}, idxEnd: {idxEnd}");

        Split(items, itemsSorted, idxBegin, idxMid);
        Split(items, itemsSorted, idxMid, idxEnd);
        Merge(items, itemsSorted, idxBegin, idxMid, idxEnd);
    }

    public void Merge(IList<TItem> itemsSorted, IList<TItem> items, int idxBegin, int idxMid, int idxEnd)
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

}