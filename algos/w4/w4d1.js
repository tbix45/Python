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

    removeFromBack() {
        if (!this.head) {
            console.log("List is empty cant remove from back")
            return
        } else {
            var runner = this.head
            while (runner.next.next) {
                runner = runner.next
            }
            runner.next = null
            return
        }
    }

    moveMinToFront() {
        if (!this.head) {
            console.log("List to short to move Min to front")
            return this
        }
        var runner = this.head
        var walker = this.head
        var min = this.head

        while (runner.next) {
            if (runner.next.value < min.value) {
                min = runner.next
                walker = runner
            }
            runner = runner.next
        }
        if (min.value == this.head.value) {
            console.log("Min already at front")
            return this
        }
        walker.next = min.next
        min.next = this.head
        this.head = min
        console.log("Min value is", min.value)
        return this
    }
    moveMaxToBack() {
        if (!this.head) {
            console.log("Nothing to move to back!")
        }
        var runner = this.head
        var max = this.head
        var walker = this.head
        while (runner.next) {
            if (runner.next.value > max.value) {
                max = runner.next
                walker = runner
            }
            runner = runner.next
        }
        if (max == this.head) {
            runner.next = max
            this.head = this.head.next
            runner.next.next = null
            return
        }
        walker.next = max.next
        runner.next = max
        max.next = null
        console.log("Max value is:", max.value)
        return
    }

    prependValue(value, loc) {

    }
    appendValue(value, loc) {

    }

}

const sll = new SLList();
sll.addToFront(3)
sll.addToFront(2)
sll.addToFront(1)
sll.addToFront(4)
sll.addToFront(2)
// console.log(sll.contain(4))
sll.printValue()
console.log("==============================")
// sll.removeFromBack()
sll.moveMaxToBack()
// sll.moveMinToFront()
sll.printValue()
console.log("==============================")
