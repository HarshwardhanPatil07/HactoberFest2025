class Node{
public:
    int key;
    int val;
    Node *next;
    Node *prev;

    Node(int key, int val) : key(key), val(val), next(nullptr), prev(nullptr) {}
};

class LRUCache {
private:
    int cap;
    unordered_map<int, Node*> cache;
    Node *oldest;
    Node *latest;

    void insert(Node *node){
        Node *next = latest;
        Node *prev = latest->prev;

        prev->next = next->prev = node;
        node->prev = prev;
        node->next = next;
    }

    void remove(Node *node){
        Node *prev = node->prev;
        Node *next = node->next;
        prev->next = next;
        next->prev = prev;
    }

public:
    LRUCache(int capacity) {
        this->cap = capacity;
        cache.clear();
        oldest = new Node(-1, -1);
        latest = new Node(-1, -1);
        oldest->next = latest;
        latest->prev = oldest;
    }
    
    int get(int key) {
        if(cache.find(key) != cache.end()){
            Node *node = cache[key];
            remove(node);
            insert(node);
            return node->val;
        }

        return -1;
    }
    
    void put(int key, int value) {
        if(cache.find(key) != cache.end()){
            remove(cache[key]);
        }

        Node *newNode = new Node(key, value);
        cache[key] = newNode;
        insert(newNode);

        if(cache.size() > cap){
            Node *lru = oldest->next;
            remove(lru);
            cache.erase(lru->key);
            delete lru;
        }
    }

    ~LRUCache(){
        Node *curr = oldest;
        while(curr != nullptr){
            Node *next = curr->next;
            delete curr;
            curr = next;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
