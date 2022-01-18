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
    //given a value go through list and return boolean if exists in list
    contain(value) {
        if (!this.head) {
            console.log("Nothing in list! Doesn't contain anything!")
            return false
        }
        var runner = this.head
        while (runner) {
            if (runner.value == value) {
                console.log(`Value is: ${runner.value}`)
                return true
            }
            runner = runner.next
        }
        //if through whole list and not found
        return false
    }

    removeFromFront() {
        if (this.head) {
            var next = this.head.next
            this.head.next = null
            this.head = next
        }
    }



}

const sll = new SLList();
sll.addToFront(1)
sll.addToFront(2)
sll.addToFront(3)
sll.addToFront(4)
console.log(sll.contain(4))
// sll.removeFromFront()
sll.printValue()