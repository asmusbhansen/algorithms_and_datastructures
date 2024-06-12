
namespace DsaCsharp.Sort;

public interface ISort<TItem> where TItem : IComparable
{
    public IList<TItem> Sort(IList<TItem> input);
}