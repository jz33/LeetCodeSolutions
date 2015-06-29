/*
04 Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
*/
function ListNode(val){
    this.val = val;
    this.next = null;
}
// Returns a random integer between min (included) and max (excluded)
// Using Math.round() will give you a non-uniform distribution!
var ranInt = function(min, max){
    return Math.floor(Math.random() * (max - min)) + min;
}

var newList = function(size){
    if(size < 1) return null;
    var head = new ListNode(0);
    var p = head;
    p.val = ranInt(1,10);
    for(var i = 1;i<size;i++){
        p.next = new ListNode(ranInt(0,size));
        p = p.next;
    }
    return head;
}

var printList = function(l){
    while(l !== null){
        process.stdout.write(l.val+" ");
        l = l.next;
    }
    console.log();
}

var addTwoNumbers = function(l1, l2){
    if (l1 === null) return l2;
    if (l2 === null) return l1;
    
    var head = new ListNode(0);
    var p = head;
    var s = 0;
    while(l1 !== null || l2 !== null){
        s = parseInt(s / 10);
        if(l1 !== null){
            s += l1.val;
            l1 = l1.next;
        }
        if(l2 !== null){
            s += l2.val;
            l2 = l2.next;
        }
        p.next = new ListNode(s % 10);
        p = p.next;
    }
    if(s > 9){
        p.next = new ListNode(1);
    }
    return head.next;
}

l1 = newList(4);
l2 = newList(6);
printList(l1);
printList(l2);
l3 = addTwoNumbers(l1,l2);
printList(l3);


