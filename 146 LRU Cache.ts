/**
146. LRU Cache
https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
*/

/**
 * Not Node (which is defined in Node.js),
 * not ListNode (which is defined inside Leetcode)
 */
interface MyNode {
  key?: number;
  value?: number;
  prev?: MyNode;
  next?: MyNode;
}

class DoubleLinkedList {
  // 2 virtual nodes act as head and tail
  private head: MyNode = {};
  private tail: MyNode = {};

  constructor() {
    this.connect(this.head, this.tail);
  }

  /**
   * Connect 2 nodes, nodeA -> nodeB
   */
  private connect(nodeA: MyNode, nodeB: MyNode) {
    nodeA.next = nodeB;
    nodeB.prev = nodeA;
  }

  /**
   * Append a new node to end of the list
   */
  append(node: MyNode): void {
    this.connect(this.tail.prev!, node);
    this.connect(node, this.tail);
  }

  /**
   * Remove a node from the list
   */
  pop(node: MyNode): MyNode {
    this.connect(node.prev!, node.next!);
    node.prev = undefined;
    node.next = undefined;
    return node;
  }

  /**
   * Pop first node.
   * This size of the list must be at least 1
   */
  popHead(): MyNode {
    return this.pop(this.head.next!);
  }
}

class LRUCache {
  private keyToNodes: Map<number, MyNode> = new Map<number, MyNode>();
  private dll: DoubleLinkedList = new DoubleLinkedList();

  constructor(private capacity: number) {}

  get(key: number): number {
    const node = this.keyToNodes.get(key);
    if (node) {
      this.dll.pop(node);
      this.dll.append(node);
      return node.value!;
    } else {
      return -1;
    }
  }

  put(key: number, value: number): void {
    const node = this.keyToNodes.get(key);
    if (node) {
      node.value = value;
      this.dll.pop(node);
      this.dll.append(node);
    } else {
      if (this.keyToNodes.size === this.capacity) {
        const oldHead = this.dll.popHead();
        this.keyToNodes.delete(oldHead.key!);
      }
      const newNode: MyNode = { key, value };
      this.keyToNodes.set(key, newNode);
      this.dll.append(newNode);
    }
  }
}

const lRUCache: LRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1); // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2); // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1); // return -1 (not found)
lRUCache.get(3); // return 3
lRUCache.get(4); // return 4
