// singly linked lists
class Node {
    constructor(value) {
        this.value = value
        this.next = null
    }
}

class SLList {
    constructor() {
        this.head = null
    }
    addToFront(value) {
        var newNode = new Node(value)
        newNode.next = this.head
        this.head = newNode
    }
    addToBack(value) {
        var newNode = new Node(value)
        if (this.head == null) {
            this.head = newNode
            return
        }
        var runner = this.head
        while (runner.next) {
            runner = runner.next
        }
        runner.next = newNode
    }
    printValue() {
        if (this.head == null) {
            console.log("Nothing in list")
        } else {
            var runner = this.head
            var str = ""
            while (runner) {
                str += `${runner.value}` + " --> "
                runner = runner.next
            }
            str += "null"
            console.log(str)
        }
    }
}

const sll = new SLList();
sll.addToFront(1)
sll.addToFront(2)
sll.addToFront(3)
sll.addToFront(4)
sll.printValue()