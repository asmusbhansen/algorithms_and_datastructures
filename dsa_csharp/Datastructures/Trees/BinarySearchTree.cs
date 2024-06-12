using System.Collections;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics.CodeAnalysis;
using System.Drawing;
using System.Reflection.Metadata.Ecma335;
using System.Security.Cryptography.X509Certificates;

namespace DsaCsharp.BinarySearchTree;

public class BinarySearchTree<TKey, TValue> : IDictionary<TKey, TValue> where TKey : IComparable
{
    INodeFactory<TKey, TValue> NodeFactory;
 
    public BinarySearchTree(INodeFactory<TKey, TValue> nodeFactory)
    {
        NodeFactory = nodeFactory;
    }

    private INode<TKey, TValue>? root;

    public int Size()
    {
        return Size(root);
    }
    public int Size(INode<TKey,TValue> node)
    {
        if (node == null)
        {
            return 0;
        }
        else
        {
            return node.Size;
        }
    }

    public TValue this[TKey key] { get => Get(key); set => Add(key, value);}

    public ICollection<TKey> Keys { get => GetSortedKeys(); }

    public ICollection<TKey> GetSortedKeys()
    { 
        return InorderTraversal(root).Select(e => e.Key).ToList();

    }

    public List<TValue> GetValuesSortedByKey()
    {
        return InorderTraversal(root).Select(e => e.Value).ToList();
    }

    public IList<INode<TKey, TValue>> InorderTraversal(INode<TKey, TValue> node)
    {
        List<INode<TKey, TValue>> nodes = new List<INode<TKey, TValue>>();

        if(node == null)
        {
            return nodes;
        }    

        //First add all keys to the left of the node since they are smaller
        nodes.AddRange(InorderTraversal(node.Left));
        // Second add the current node key
        nodes.Add(node);
        //Third add all keys to the right of the node since they are larger
        nodes.AddRange(InorderTraversal(node.Right));

        return nodes;
    }

    public IList<INode<TKey, TValue>> InorderTraversal()
    {
        return InorderTraversal(root);
    }

    public ICollection<TValue> Values => GetValuesSortedByKey(); 

    public int Count => Size();

    public bool IsReadOnly => throw new NotImplementedException();

    public void Add(KeyValuePair<TKey, TValue> item)
    {
        Add(item.Key, item.Value);
    }

    public void Add(TKey key, TValue value)
    {
        INode<TKey, TValue> nodeNew = NodeFactory.Create(key, value, 1);
        Add(nodeNew);
    }

    public void Add(INode<TKey, TValue> nodeAdd)
    {
        root = Add(root, nodeAdd);
    }

    public INode<TKey, TValue> Add(INode<TKey, TValue> node, INode<TKey, TValue> nodeAdd)
    {
        if (node == null)
        {
            return nodeAdd;
        }

        int compare = nodeAdd.Key.CompareTo(node.Key);

        if (compare < 0)
        {
            node.Left = Add(node.Left, nodeAdd.Key, nodeAdd.Value);
        }
        else if (compare > 0)
        {
            node.Right = Add(node.Right, nodeAdd.Key, nodeAdd.Value);
        }
        else
        {
            node.Value = nodeAdd.Value;
        }
        node.Size = Size(node.Left) + Size(node.Right) + 1;
        return node;
    }

    public INode<TKey, TValue> Add(INode<TKey, TValue> node, TKey key, TValue value)
    {
        if (node == null)
        {
            return NodeFactory.Create(key, value, 1);
        }

        int compare = key.CompareTo(node.Key);

        if (compare < 0)
        {
            node.Left = Add(node.Left, key, value);
        }
        else if (compare > 0)
        {
            node.Right = Add(node.Right, key, value);
        }
        else
        {
            node.Value = value;
        }
        node.Size = Size(node.Left) + Size(node.Right) + 1;
        return node;
    }

    public void Clear()
    {
        throw new NotImplementedException();
    }

    public bool Contains(KeyValuePair<TKey, TValue> item)
    {
        throw new NotImplementedException();
    }

    public bool ContainsKey(TKey key)
    {
        throw new NotImplementedException();
    }

    public void CopyTo(KeyValuePair<TKey, TValue>[] array, int arrayIndex)
    {
        throw new NotImplementedException();
    }

    public IEnumerator<KeyValuePair<TKey, TValue>> GetEnumerator()
    {
        throw new NotImplementedException();
    }

    public INode<TKey, TValue> Remove(INode<TKey, TValue> node, TKey key)
    {
        if (node == null) return null;

        int compare = key.CompareTo(node.Key);

        if (compare < 0)
        {
            node.Left = Remove(node.Left, key);
        }
        else if (compare > 0)
        {
            node.Right = Remove(node.Right, key);
        }
        else
        {
            if(node.Right == null) return node.Left;
            if(node.Left == null) return node.Right;
            INode<TKey, TValue> tempNode = node;
            // Overwrite node with the successor
            node = Min(tempNode.Right);
            
            node.Right = RemoveMin(tempNode.Right);
            node.Left = tempNode.Left;
        }
        node.Size = Size(node.Left) + Size(node.Right) + 1;
        return node;

    }

    public bool Remove(TKey key)
    {
        root = Remove(root, key);

        //Console.WriteLine($"-- Removing key {key} - Keys: [{string.Join<TKey>(",", Keys)}], Values: [{string.Join<TValue>(",", Values)}]");
        return true;
    }

    public bool Remove(KeyValuePair<TKey, TValue> item)
    {
        throw new NotImplementedException();
    }

    public INode<TKey, TValue> RemoveMin(INode<TKey, TValue> node)
    {
        if(node.Left == null) return node.Right;

        node.Left = RemoveMin(node.Left);
        node.Size = Size(node.Left) + Size(node.Right) + 1;
        return node;
    }
    public void RemoveMin()
    {
        root = RemoveMin(root);
    }

    public INode<TKey, TValue> Min(INode<TKey, TValue> node)
    {
        if (node.Left == null) return node;
        return Min(node.Left);
    }

    public INode<TKey, TValue> Min()
    {
        return Min(root);
    }

    public bool TryGetValue(INode<TKey, TValue> node, TKey key, [MaybeNullWhen(false)] out TValue value)
    {
        if (node == null)
        {
            value = default(TValue);
            return false;
        }

        //Console.WriteLine($"Getting key = {key} - Currently at node key {node.Key}, root key: {root.Key}");

        int compare = key.CompareTo(node.Key);

        if (compare < 0)
        {
            return TryGetValue(node.Left, key, out value);
        }
        else if (compare > 0)
        {
            return TryGetValue(node.Right, key, out value);
        }
        else
        {
            //Console.WriteLine($"Found key = {key}, value = {node.Value}");
            value = node.Value;
            return true;
        }
    }

    public bool TryGetValue(TKey key, [MaybeNullWhen(false)] out TValue value)
    {
        return TryGetValue(root, key, out value);
    }

    public TValue Get(TKey key)
    {
        TValue value = default(TValue);
        bool result = TryGetValue(root, key, out value);
        if (result)
        {
            return value;
        }
        else
        {
            throw new KeyNotFoundException();
        }
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        throw new NotImplementedException();
    }
}


public interface INode<TKey, TValue> where TKey : IComparable
{
    public TKey Key { get; set; }
    public TValue Value { get; set; }
    public int Size { get; set; }
    public INode<TKey, TValue>? Left { get; set;}
    public INode<TKey, TValue>? Right { get; set;}
    public string ToString();
}

public class Node<TKey, TValue> : INode<TKey, TValue> where TKey : IComparable
{
    public TKey Key { get; set; }
    public TValue Value { get; set; }
    public int Size { get; set; } = 0;
    public INode<TKey, TValue>? Left {get; set;} = null;
    public INode<TKey, TValue>? Right {get; set;} = null;
    public Node(TKey key, TValue value, int size=1)
    {
        Key = key;
        Value = value;
        Size = size;
    }

    public string ToString()
    {
        return $"Key: " + Key + ", Value: " + Value;
    }
}

public interface INodeFactory<TKey, TValue> where TKey : IComparable
{
    public INode<TKey, TValue> Create(TKey key, TValue value, int size);
}

public class NodeFactory<TKey, TValue> : INodeFactory<TKey, TValue> where TKey : IComparable
{
    public INode<TKey, TValue> Create(TKey key, TValue value, int size)
    {
        return new Node<TKey, TValue>(key, value, size);
    }
}
