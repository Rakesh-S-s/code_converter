using System;

// Node structure for the linked list
public class Node
{
    public int data;
    public Node next;
}

// Function to create a new node with given data
public static Node createNode(int data)
{
    Node newNode = new Node();
    newNode.data = data;
    newNode.next = null;
    return newNode;
}

// Function to insert a node at the beginning of the list
public static void insertAtBeginning(ref Node head, int data)
{
    Node newNode = createNode(data);
    newNode.next = head;
    head = newNode;
}

// Function to insert a node at the end of the list
public static void insertAtEnd(ref Node head, int data)
{
    Node newNode = createNode(data);
    if (head == null)
    {
        head = newNode;
        return;
    }
    Node temp = head;
    while (temp.next != null)
    {
        temp = temp.next;
    }
    temp.next = newNode;
}

// Function to delete a node with given key
public static void deleteNode(ref Node head, int key)
{
    Node temp = head, prev = null;

    // If head node itself holds the key to be deleted
    if (temp != null && temp.data == key)
    {
        head = temp.next;
        return;
    }

    // Search for the key to be deleted
    while (temp != null && temp.data != key)
    {
        prev = temp;
        temp = temp.next;
    }

    // If key was not found
    if (temp == null) return;

    // Unlink the node from the list
    prev.next = temp.next;
}

// Function to display the linked list
public static void displayList(Node head)
{
    Node temp = head;
    Console.Write("Linked list: ");
    while (temp != null)
    {
        Console.Write($"{temp.data} -> ");
        temp = temp.next;
    }
    Console.WriteLine("NULL");
}

// Predefined input to initialize the linked list
public static void initializeList(ref Node head)
{
    insertAtEnd(ref head, 10);
    insertAtEnd(ref head, 20);
    insertAtEnd(ref head, 30);
    insertAtEnd(ref head, 40);
    insertAtEnd(ref head, 50);
}

public static void Main(string[] args)
{
    Node head = null;

    // Initialize the linked list with pre-built input
    initializeList(ref head);

    // Display the initial list
    Console.Write("Initial ");
    displayList(head);

    // Perform some operations
    Console.WriteLine("\nInserting 5 at the beginning:\n");
    insertAtBeginning(ref head, 5);
    displayList(head);

    Console.WriteLine("\nInserting 60 at the end:\n");
    insertAtEnd(ref head, 60);
    displayList(head);

    Console.WriteLine("\nDeleting node with value 30:\n");
    deleteNode(ref head, 30);
    displayList(head);

    Console.WriteLine("\nDeleting node with value 5 (beginning):\n");
    deleteNode(ref head, 5);
    displayList(head);

    Console.WriteLine("\nDeleting node with value 60 (end):\n");
    deleteNode(ref head, 60);
    displayList(head);
}
