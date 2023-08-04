class Hashtable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]  # Initialize empty list for each bucket

    def _hash_function(self, key):
        """Hash function to convert key into an index"""
        return hash(key) % self.size

    def _linear_probing(self, index, i):
        """Linear probing to resolve collisions"""
        return (index + i) % self.size

    def _quadratic_probing(self, index, i):
        """Quadratic probing to resolve collisions"""
        return (index + i ** 2) % self.size

    def _separate_chaining(self, index):
        """Separate chaining to resolve collisions"""
        return index

    def insert(self, key, value, method='linear'):
        """Insert a key-value pair into the hashtable"""
        index = self._hash_function(key)
        if not self.hash_table[index]:  # If bucket is empty, directly insert
            self.hash_table[index].append((key, value))
        else:  # If collision occurs, resolve using specified method
            i = 1
            while True:
                # Use linear probing, quadratic probing, or separate chaining
                if method == 'linear':
                    new_index = self._linear_probing(index, i)
                elif method == 'quadratic':
                    new_index = self._quadratic_probing(index, i)
                elif method == 'chaining':
                    self.hash_table[index].append((key, value))
                    break
                else:
                    raise ValueError('Invalid collision resolution method')

                if not self.hash_table[new_index]:  # If bucket is empty, insert
                    self.hash_table[new_index].append((key, value))
                    break
                i += 1

    def get(self, key):
        """Get the value associated with a key from the hashtable"""
        index = self._hash_function(key)
        if not self.hash_table[index]:
            raise KeyError('Key not found in hashtable')
        else:
            for k, v in self.hash_table[index]:
                if k == key:
                    return v
            raise KeyError('Key not found in hashtable')

    def remove(self, key):
        """Remove a key-value pair from the hashtable"""
        index = self._hash_function(key)
        if not self.hash_table[index]:
            raise KeyError('Key not found in hashtable')
        else:
            for i, (k, v) in enumerate(self.hash_table[index]):
                if k == key:
                    del self.hash_table[index][i]
                    return
            raise KeyError('Key not found in hashtable')

    def __repr__(self):
        """Representation of the hashtable"""
        return str(self.hash_table)


# Create a hashtable with size 5
hash_table = Hashtable(5)
# Insert key-value pairs using linear probing
hash_table.insert(25, 15, method='linear')
hash_table.insert(10, 22, method='linear')
hash_table.insert(1, 33, method='linear')

# Display the hashtable
print("Hashtable with linear probing:")
print(hash_table)

# Insert key-value pairs using quadratic probing
hash_table = Hashtable(5)  # Reset the hashtable
hash_table.insert(15, 10, method='quadratic')
hash_table.insert(30, 22, method='quadratic')
hash_table.insert(30, 13, method='quadratic')

# Display the hashtable
print("\nHashtable with quadratic probing:")
print(hash_table)

# Insert key-value pairs using separate chaining
hash_table = Hashtable(5)  # Reset the hashtable
hash_table.insert(36, 11, method='chaining')
hash_table.insert(30, 22, method='chaining')
hash_table.insert(30, 34, method='chaining')

# Display the hashtable
print("\nHashtable with separate chaining:")
print(hash_table)