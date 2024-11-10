class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    // Append a node to the end of the list
    append(value) {
        const newNode = new Node(value);
        if (!this.head) {
            this.head = newNode;
            return;
        }
        let current = this.head;
        while (current.next) {
            current = current.next;
        }
        current.next = newNode;
    }

    // Prepend a node to the start of the list
    prepend(value) {
        const newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
    }

    // Insert a node at a specified index
    insert(value, index) {
        if (index < 0) {
            console.log("Index must be non-negative.");
            return;
        }

        if (index === 0) {
            this.prepend(value);
            return;
        }

        const newNode = new Node(value);
        let current = this.head;
        let previous;
        let currentIndex = 0;

        while (current && currentIndex < index) {
            previous = current;
            current = current.next;
            currentIndex++;
        }

        if (previous) {
            newNode.next = current;
            previous.next = newNode;
        } else {
            console.log("Index out of range.");
        }
    }

    // Delete the first node with the specified value
    delete(value) {
        if (!this.head) {
            console.log("List is empty.");
            return;
        }

        // If head is the node to be deleted
        if (this.head.value === value) {
            this.head = this.head.next;
            return;
        }

        let current = this.head;
        let previous = null;

        while (current && current.value !== value) {
            previous = current;
            current = current.next;
        }

        if (current) {
            previous.next = current.next;
        } else {
            console.log("Value not found in the list.");
        }
    }

    // Find the first node with the specified value
    find(value) {
        let current = this.head;
        while (current) {
            if (current.value === value) {
                return current;
            }
            current = current.next;
        }
        return null;
    }

    // Display all values in the linked list
    display() {
        if (!this.head) {
            console.log("List is empty.");
            return;
        }
        let current = this.head;
        const values = [];
        while (current) {
            values.push(current.value);
            current = current.next;
        }
        console.log(values.join(" -> "));
    }
}

// Example usage:
const linkedList = new LinkedList();
linkedList.append(10);
linkedList.append(20);
linkedList.prepend(5);
linkedList.insert(15, 2); // Insert 15 at index 2
linkedList.display(); // Expected output: 5 -> 10 -> 15 -> 20

linkedList.delete(10); // Delete node with value 10
linkedList.display(); // Expected output: 5 -> 15 -> 20

const foundNode = linkedList.find(15);
console.log(foundNode ? "Node found: " + foundNode.value : "Node not found"); // Expected output: Node found: 15
