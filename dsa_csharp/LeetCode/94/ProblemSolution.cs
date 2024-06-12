using DsaCsharp.BinarySearchTree;

namespace DsaCsharp.LeetCode.NineFour;

public class NineFourSolution
{
    public void Test()
    {        
        IList<INode<int,int>> nodes= new List<INode<int, int>>(){new Node<int,int>(key : 1, value : 3),
                                                                 new Node<int,int>(key : 5, value : 4),
                                                                 new Node<int,int>(key : 3, value : 5)};

        BinarySearchTree<int,int> binarySearchTree = new BinarySearchTree<int, int>(nodeFactory : new NodeFactory<int,int>());

        foreach(var node in nodes)
        {
            binarySearchTree.Add(node);
             Console.WriteLine($"Inserted node {node.ToString()}");
        }
        IList<INode<int,int>> nodesOrdered = binarySearchTree.InorderTraversal();
        foreach(var node in nodesOrdered){
            Console.WriteLine($"Got node {node.ToString()}");
        }

    }
}