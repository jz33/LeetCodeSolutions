class ListNode<K,V> {
    public ListNode next;
    public ListNode prev;
    public K key;
    public V val;
    
    public ListNode() {
        
    }

    public ListNode(K key, V val) {
        this.key = key;
        this.val = val;
    }
}

class DoubleLinkedList<K,V> {
    public ListNode<K,V> head = new ListNode();
    public ListNode<K,V> tail = new ListNode();
    
    public DoubleLinkedList() {
        head.next = tail;
        tail.prev = head;
    }
    
    public void append(ListNode node) {
        ListNode prev = tail.prev;
        prev.next = node;
        node.prev = prev;
        tail.prev = node;
        node.next = tail;
    }
    
    public void remove(ListNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        node.prev = null;
        node.next = null;
    }
}

class LRUCache {
    private HashMap<Integer, ListNode<Integer, Integer>> keyToNode = new HashMap();
    private DoubleLinkedList<Integer, Integer> dll = new DoubleLinkedList();
    private int capacity = 1;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
    }
    
    public int get(int key) {
        ListNode<Integer, Integer> node = keyToNode.get(key);
        if (node == null) {
            return -1;
        }
        
        dll.remove(node);
        dll.append(node);
        return node.val; 
    }
    
    public void put(int key, int value) {
        ListNode<Integer, Integer> node = keyToNode.get(key);
        if (node == null) {
            if (keyToNode.size() == capacity) {
                // Re-use least recently used node
                node = dll.head.next;
                dll.remove(node);
                keyToNode.remove(node.key);
                
                node.key = key;
                node.val = value;
            } else {
                node = new ListNode<Integer, Integer>(key, value);
            }
            keyToNode.put(key, node);
        } else {
            node.val = value;
            dll.remove(node);
        }
        dll.append(node);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
