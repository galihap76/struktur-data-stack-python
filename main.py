# Mendefinisikan kelas bernama "Stack"
class Stack:
    # Konstruktor kelas Stack
    def __init__(self):
        # Membuat atribut "items" yang merupakan daftar kosong
        self.items = []

    # Metode untuk memeriksa apakah stack kosong
    def is_empty(self):
        # Mengembalikan True jika panjang daftar (items) adalah 0, jika tidak, mengembalikan False
        return len(self.items) == 0

    # Metode untuk menambahkan elemen ke dalam stack
    def push(self, item):
        # Menambahkan elemen "item" ke akhir daftar (items)
        self.items.append(item)

    # Metode untuk mengeluarkan elemen teratas dari stack
    def pop(self):
        # Memeriksa apakah stack tidak kosong
        if not self.is_empty():
            # Menghapus dan mengembalikan elemen terakhir dari daftar (items)
            return self.items.pop()
        else:
            # Jika stack kosong, raise (lemparkan) IndexError dengan pesan "Stack is empty"
            raise IndexError("Stack is empty")

    # Metode untuk melihat elemen teratas dari stack tanpa mengeluarkannya
    def peek(self):
        # Memeriksa apakah stack tidak kosong
        if not self.is_empty():
            # Mengembalikan elemen terakhir dari daftar (items)
            return self.items[-1]
        else:
            # Jika stack kosong, raise (lemparkan) IndexError dengan pesan "Stack is empty"
            raise IndexError("Stack is empty")

    # Metode untuk menghitung jumlah elemen dalam stack
    def size(self):
        # Mengembalikan panjang daftar (items)
        return len(self.items)



# Membuat objek dari kelas Stack
stack = Stack()

# Memanggil metode "push" pada objek "stack" dengan nilai 10
stack.push(10)

# Memanggil metode "push" pada objek "stack" dengan nilai 20
stack.push(20)

# Memanggil metode "push" pada objek "stack" dengan nilai 30
stack.push(30)

print("Stack size:", stack.size())  # Output: 3
print("Top item:", stack.peek())    # Output: 30

popped_item = stack.pop()
print("Popped item:", popped_item)  # Output: 30

print("Is stack empty?", stack.is_empty())  # Output: False
