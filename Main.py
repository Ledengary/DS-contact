import math
import re
max_size = 129
main_id_counter = 0
contacts_size = 0
class Contact:
    def __init__(self, first_name, last_name, mobile_number, email_address, address, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.email_address = email_address
        self.address = address
        self.postal_code = postal_code

    def get_first_name(self):
        return self.first_name
    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name
    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_mobile_number(self):
        return self.mobile_number
    def set_mobile_number(self, mobile_number):
        self.mobile_number = mobile_number

    def get_email_address(self):
        return self.email_address
    def set_email_address(self, email_address):
        self.email_address = email_address

    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address

    def get_postal_code(self):
        return self.postal_code
    def set_postal_code(self, postal_code):
        self.postal_code = postal_code

    def to_string(self):
        return self.first_name + " " + self.last_name + " " + self.mobile_number + " " + self.email_address + " " + self.address + " " + self.postal_code


class Trie_node:
    def __init__(self):
        self.information = None
        self.flag = False
        self.sub_nodes = [None] * 26
        self.value = 0

    def is_leaf(self):
        return self.value != 0

    def is_free(self):
        for each_sub_node in self.sub_nodes:
            if each_sub_node is not None:
                return False
        return True

class Trie:
    def __init__(self):
        self.root = Trie_node()
        self.size = 0

    def _char_to_index(self, char):
        return ord(char) - ord('a')

    def _index_to_char(self, num):
        return ord(char) - ord('a')

    def insert(self, word, given_id):
        self.size += 1
        current = self.root
        length = len(word)
        for i in range(length):
            index = self._char_to_index(word[i])
            if current.sub_nodes[index]:
                current = current.sub_nodes[index]
            else:
                current.sub_nodes[index] = Trie_node()
                current = current.sub_nodes[index]
        current.information = given_id
        current.flag = True
        current.value = self.size

    def search(self, word):
        current = self.root
        length = len(word)
        for i in range(length):
            index = self._char_to_index(word[i])
            if current.sub_nodes[index] is None:
                return False
            current = current.sub_nodes[index]

        return current is not None and current.flag

    def get(self, word):
        current = self.root
        length = len(word)
        for i in range(length):
            index = self._char_to_index(word[i])
            if current.sub_nodes[index] is None:
                return -1
            current = current.sub_nodes[index]

        if current is not None and current.flag == True:
            return current
        else:
            return -1

    def delete(self, word):
        length = len(word)
        if length > 0:
            self._delete(self.root, word, 0, length)

    def _delete(self, current, key, level, length):
        if current:
            if level == length:
                if current.value:
                    current.value = 0
                return current.is_free()
            else:
                index = self._char_to_index(key[level])
                if self._delete(current.sub_nodes[index], key, level + 1, length):
                    current.sub_nodes[index] = None
                    return not current.is_leaf() and current.is_free()
        return False

    def pre_search(self, given_pre):
        before_chars = ""
        for each_char in given_pre:
            before_chars += str(each_char)
            current = self.root
            length = len(before_chars)
            for i in range(length):
                index = self._char_to_index(before_chars[i])
                if current.sub_nodes[index] is None:
                    return False
                current = current.sub_nodes[index]
            print("(" + before_chars + ")", "Suggestions:")
            print("===========================================================")
            if current.flag is True:
                print(before_chars)
            self._pre_search(current, before_chars)

    def _pre_search(self, current, word):
        for i in range(26):
            temp_word = word
            if current.sub_nodes[i] is not None:
                temp_word += str(chr(i + 97))
                if current.sub_nodes[i].flag is True:
                    print(temp_word)
                self._pre_search(current.sub_nodes[i], temp_word)

class Numeric_trie_node:
    def __init__(self):
        self.information = None
        self.flag = False
        self.sub_nodes = [None] * 10
        self.value = 0

    def is_leaf(self):
        return self.value != 0

    def is_free(self):
        for each_sub_node in self.sub_nodes:
            if each_sub_node is not None:
                return False
        return True

class Numberic_trie:
    def __init__(self):
        self.root = Trie_node()
        self.size = 0

    def _char_to_index(self, char):
        return int(char)

    def insert(self, word, given_id):
        self.size += 1
        current = self.root
        length = len(word)
        for i in range(length):
            index = self._char_to_index(word[i])
            if current.sub_nodes[index]:
                current = current.sub_nodes[index]
            else:
                current.sub_nodes[index] = Trie_node()
                current = current.sub_nodes[index]
        current.information = given_id
        current.flag = True
        current.value = self.size

    def search(self, word):
        current = self.root
        length = len(word)
        for i in range(length):
            index = self._char_to_index(word[i])
            if current.sub_nodes[index] is None:
                return False
            current = current.sub_nodes[index]

        return current is not None and current.flag

    def get(self, word):
        current = self.root
        length = len(word)
        for i in range(length):
            index = self._char_to_index(word[i])
            if current.sub_nodes[index] is None:
                return -1
            current = current.sub_nodes[index]

        if current is not None and current.flag == True:
            return current
        else:
            return -1

    def delete(self, word):
        length = len(word)
        if length > 0:
            self._delete(self.root, word, 0, length)

    def _delete(self, current, key, level, length):
        if current:
            if level == length:
                if current.value:
                    current.value = 0
                return current.is_free()
            else:
                index = self._char_to_index(key[level])
                if self._delete(current.sub_nodes[index], key, level + 1, length):
                    current.sub_nodes[index] = None
                    return not current.is_leaf() and current.is_free()
        return False

class array_list_node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.last = None

class array_list():
    def __init__(self):
        self.head = array_list_node()
        self.tail = array_list_node()
        self.size = 0

    def __len__(self):
        return self.size

    def getSize(self):
        return self.size

    def append(self, data):
        new_node = array_list_node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            before = self.tail
            self.tail = new_node
            new_node.last = before
            before.next = new_node
        self.size += 1

    def update(self, index, given_data):
        counter = 0
        current_node = self.head
        while current_node is not None:
            if counter == index:
                current_node.data = given_data
                break
            current_node = current_node.next
            counter += 1

    def display(self):
        the_list = [0 for x in range(self.getSize())]
        if self.getSize() == 0:
            return the_list
        counter = 0
        current_node = self.head
        while current_node is not None:
            the_list[counter] = current_node.data
            current_node = current_node.next
            counter += 1
        return the_list

    def delete(self, value):
        if self.head.data == value:
            self.deleteFirst()
        elif self.tail.data == value:
            self.deleteLast()
        else:
            self._delete(value)

    def deleteLast(self):
        if self.size != 0:
            if self.size ==1:
                self.head = None
                self.tail = None
            else:
                last_node = self.tail
                before = last_node.last
                before.next = None
                self.tail = before
            self.size -= 1

    def deleteFirst(self):
        if self.size != 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                next_node = self.head
                after = next_node.next
                after.last = None
                self.head = after
            self.size -= 1

    def _delete(self, value):
        current_node = self.head.next
        while current_node is not None:
            if current_node.data == value:
                last_node = current_node.last
                next_node = current_node.next
                last_node.next = next_node
                next_node.last = last_node
                self.size -= 1
                break
            current_node = current_node.next

class bst_node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

class binary_search_tree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.tree_array = array_list()

    def __len__(self):
        return self.size

    def insert(self, value):
        if self.root is None:
            self.root = bst_node(value)
            self.tree_array.append(value)
            self.size += 1
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if int(value.get_mobile_number()[2:]) < int(current_node.value.get_mobile_number()[2:]):
            if current_node.left_child is None:
                current_node.left_child = bst_node(value)
                current_node.left_child.parent = current_node
                self.tree_array.append(value)
                self.size += 1
            else:
                self._insert(value, current_node.left_child)
        elif int(value.get_mobile_number()[2:]) > int(current_node.value.get_mobile_number()[2:]):
            if current_node.right_child is None:
                current_node.right_child = bst_node(value)
                current_node.right_child.parent = current_node
                self.tree_array.append(value)
                self.size += 1
            else:
                self._insert(value, current_node.right_child)
        else:
            print("Value Already in Tree !")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node is not None:
            self._print_tree(current_node.left_child)
            print(current_node.value)
            self._print_tree(current_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node is None:
            return current_height
        left_child = self._height(current_node.left_child, current_height + 1)
        right_child = self._height(current_node.right_child, current_height + 1)
        return max(left_child, right_child)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value.get_mobile_number()[2:] < cur_node.value.get_mobile_number()[2:] and cur_node.left_child is not None:
            return self._find(value, cur_node.left_child)
        elif value.get_mobile_number()[2:] > cur_node.value.get_mobile_number()[2:] and cur_node.right_child is not None:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        ## -----
        # Improvements since prior lesson

        # Protect against deleting a node not found in the tree
        if node == None or self.find(node.value) == None:
            print("Node to be deleted not found in the tree!")
            return None

        ## -----

        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left_child != None:
                current = current.left_child
            return current

        # returns the number of children for the specified node
        def num_children(n):
            num_children = 0
            if n.left_child != None: num_children += 1
            if n.right_child != None: num_children += 1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # break operation into different cases based on the
        # structure of the tree & node to be deleted

        # CASE 1 (node has no children)
        if node_children == 0:

            # Added this if statement post-video, previously if you
            # deleted the root node it would delete entire tree.
            if node_parent != None:
                # remove reference to the node from the parent
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None

        # CASE 2 (node has a single child)
        if node_children == 1:

            # get the single child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            # Added this if statement post-video, previously if you
            # deleted the root node it would delete entire tree.
            if node_parent != None:
                # replace the node to be deleted with its child
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child

            # correct the parent pointer in node
            child.parent = node_parent

        # CASE 3 (node has two children)
        if node_children == 2:
            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value = successor.value

            # delete the inorder successor now that it's value was
            # copied into the other node
            self.delete_node(successor)

        self.tree_array.delete(node.value)
        self.size -= 1

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child is not None:
                return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child is not None:
                return self._search(value, current_node.right_child)
        else:
            return False

def hash_funcion(key):
    alpha = 7
    m = math.pow(2, alpha)
    a = (math.sqrt(5) - 1) / 2
    answer = math.floor(m * ((key * a) % 1))
    return answer

contacts_list = [0 for x in range(max_size)]
for i in range(max_size):
    raw_tree = binary_search_tree()
    contacts_list[i] = raw_tree

name_trie = Trie()
phone_trie = Numberic_trie()

def get_order_line(line):
    return "Please enter your Order's number: \n" + line

def search_for_contact(name):
    if name_trie.search(name) is True:
        found_trie = name_trie.get(name)
        return found_trie
    else:
        return -1

def search_for_contact_phone(number):
    print("Number :", number)
    if phone_trie.search(number) is True:
        found_trie = phone_trie.get(number)
        return found_trie
    else:
        return -1

def search_inside_bst(bst, name):
    for each in bst.tree_array.display():
        if each.get_first_name() + each.get_last_name() == name:
            return each

def search_inside_bst_phone(bst, phone):
    for each in bst.tree_array.display():
        if each.get_mobile_number() == phone:
            return each

def print_list(given_list):
    print('\n'*3)
    if contacts_size > 1:
        print("=========================== " + str(contacts_size) + " contacts ===============================")
    else:
        print("=========================== " + str(contacts_size) + " contact ================================")
    counter = 0
    is_empty = True
    for each in given_list:
        if len(each) != 0:
            line = ""
            for inner_each in each.tree_array.display():
                is_empty = False
                line += " / " + inner_each.get_first_name() + " " + inner_each.get_last_name()
            print(counter, line[3:])
        counter += 1
    if is_empty is True:
        print("LIST IS EMPTY !")
    print("======================================================================")

def add_new_contact(given_contact, main_id_counter):
    name_trie.insert(given_contact.get_first_name() + given_contact.get_last_name(), main_id_counter)
    phone_trie.insert(given_contact.get_mobile_number(), main_id_counter)
    print("HASHED TO :", int(hash_funcion(main_id_counter)), name_trie.get(given_contact.get_first_name() + given_contact.get_last_name()).information, phone_trie.get(given_contact.get_mobile_number()).information)
    contacts_list[int(hash_funcion(main_id_counter))].insert(given_contact)

def check_taken_name_or_phone(given_name, given_mobile):
    answer = False
    if name_trie.search(given_name) is True:
        print("Name is Taken !")
        answer = True
    if phone_trie.search(given_mobile) is True:
        print("Phone Number is Taken !")
        answer = True
    return answer

# contacts_list[hash_funcion(512)] = "reza"
# contacts_list[hash_funcion(357)] = "damn"
# contacts_list[hash_funcion(21)] = "hey"
# contacts_list[hash_funcion(222247)] = "alooo"
# print_list(contacts_list)
# print("=============================== DONE ============================")

# contact = Contact("Reza", "Khan Mohammadi", "09369510098", "rezanecessary@gmail.com", "Rasht", "4193833537")
# contacts_list[0] = contact

print("Welcome !")
first_run = True
while True:
    try:
        if first_run is True:
            first_run = False
        else:
            print('\n' * 3)
        print("________________ MAIN MENU __________________")
        print(get_order_line("1- Print All 2- Search 3- Add New Contact 4- Trie Search"))
        order = int(input())
        if order == 1:
            print_list(contacts_list)
        elif order == 2:
            print('\n' * 3)
            print("________________ SEARCH MENU __________________")
            print(get_order_line("1- Name 2- Phone Number 3- Back"))
            # this search menu contains name or phone number which the contact will be chosen and then you will be able
            # too change or delete it's information
            order = int(input())
            while True:
                if order == 1:
                    name = input("Please enter contact's name: ")
                    found_contact = search_for_contact(name.replace(" ", ""))
                    if found_contact != -1:
                        bst_found = contacts_list[int(hash_funcion(found_contact.information))]
                        found = search_inside_bst(bst_found, name.replace(" ", ""))
                        print(found.get_first_name(), found.get_last_name(), "FOUND !")
                        while True:
                            print(get_order_line("1- Edit Contact 2- Delete Contact 3- Back"))
                            order = int(input())
                            if order == 1:
                                print('\n' * 3)
                                print("________________ SEARCH MENU -> EDIT CONTACT __________________")
                                while True:
                                    print("1- First Name\n2- Last Name\n3- Mobile Number\n4- Email Address\n5- Address\n6- Postal Code")
                                    order = int(input())
                                    name = found.get_first_name() + found.get_last_name()
                                    if order >= 1 and order <= 6:
                                        if order == 1:
                                            old_fname = found.get_first_name()
                                            old_lname = found.get_last_name()
                                            new_update = input("Change (" + found.get_first_name() + ") to ==> ")
                                            new_fname = new_update
                                            new_lname = old_lname
                                            contact_id = name_trie.get(name).information
                                            name_trie.delete(name)
                                            name_trie.insert(new_fname + new_lname, contact_id)
                                            found.set_first_name(new_update)
                                        elif order == 2:
                                            old_fname = found.get_first_name()
                                            old_lname = found.get_last_name()
                                            new_update = input("Change (" + found.get_last_name() + ") to ==> ")
                                            new_fname = old_fname
                                            new_lname = new_update
                                            contact_id = name_trie.get(name).information
                                            name_trie.delete(name)
                                            name_trie.insert(new_fname + new_lname, contact_id)
                                            found.set_last_name(new_update)
                                        elif order == 3:
                                            contact_old_phone_number = found.get_mobile_number()
                                            new_update = input("Change (" + found.get_mobile_number() + ") to ==> ")
                                            contact_new_phone_number = new_update
                                            contact_id = phone_trie.get(contact_old_phone_number).information
                                            phone_trie.delete(contact_old_phone_number)
                                            phone_trie.insert(contact_new_phone_number, contact_id)
                                            found.set_mobile_number(new_update)
                                        elif order == 2:
                                            new_update = input("Change (" + found.get_email_address() + ") to ==> ")
                                            found.set_email_address(new_update)
                                        elif order == 2:
                                            new_update = input("Change (" + found.get_address() + ") to ==> ")
                                            found.set_address(new_update)
                                        elif order == 2:
                                            new_update = input("Change (" + found.get_postal_code() + ") to ==> ")
                                            found.set_postal_code(new_update)
                                        print("UPDATED !")
                                        break
                                    else:
                                        pass
                            elif order == 2:
                                print('\n' * 3)
                                print("________________ SEARCH MENU -> DELETE CONTACT __________________")
                                contact_fname = found.get_first_name()
                                contact_lname = found.get_last_name()
                                contact_id = name_trie.get(found.get_first_name() + found.get_last_name()).information
                                contact_phone_number = found.get_mobile_number()
                                name_trie.delete(contact_fname + contact_lname)
                                phone_trie.delete(contact_phone_number)
                                contacts_list[int(hash_funcion(contact_id))].delete_value(found)
                                print(contact_fname, contact_lname, "DELETED !")
                                contacts_size -= 1
                                break
                            elif order == 3:
                                break
                    else:
                        print(name, "not found !")
                    break
                elif order == 2:
                    phone = input("Please enter contact's Phone Number: ")
                    found_contact = search_for_contact_phone(phone)
                    if found_contact != -1:
                        bst_found = contacts_list[int(hash_funcion(found_contact.information))]
                        found = search_inside_bst_phone(bst_found, phone.replace(" ", ""))
                        print(found.get_first_name(), found.get_last_name(), "FOUND !")
                        while True:
                            print(get_order_line("1- Edit Contact 2- Delete Contact 3- Back"))
                            order = int(input())
                            if order == 1:
                                while True:
                                    print('\n' * 3)
                                    print("________________ SEARCH MENU -> EDIT CONTACT __________________")
                                    print("1- First Name\n2- Last Name\n3- Mobile Number\n4- Email Address\n5- Address\n6- Postal Code")
                                    order = int(input())
                                    phone = found.get_mobile_number()
                                    if order >= 1 and order <= 6:
                                        if order == 1:
                                            old_fname = found.get_first_name()
                                            old_lname = found.get_last_name()
                                            new_update = input("Change (" + found.get_first_name() + ") to ==> ")
                                            new_fname = new_update
                                            new_lname = old_lname
                                            contact_id = phone_trie.get(phone).information
                                            found.set_first_name(new_update)
                                            name_trie.delete(old_fname + old_fname)
                                            name_trie.insert(new_fname + new_lname, contact_id)
                                        elif order == 2:
                                            old_fname = found.get_first_name()
                                            old_lname = found.get_last_name()
                                            new_update = input("Change (" + found.get_last_name() + ") to ==> ")
                                            new_fname = old_fname
                                            new_lname = new_update
                                            contact_id = phone_trie.get(phone).information
                                            found.set_last_name(new_update)
                                            name_trie.delete(old_fname + old_lname)
                                            name_trie.insert(new_fname + new_lname, contact_id)
                                        elif order == 3:
                                            contact_old_phone_number = found.get_mobile_number()
                                            new_update = input("Change (" + found.get_mobile_number() + ") to ==> ")
                                            contact_new_phone_number = new_update
                                            contact_id = phone_trie.get(contact_old_phone_number).information
                                            phone_trie.delete(contact_old_phone_number)
                                            phone_trie.insert(contact_new_phone_number, contact_id)
                                            found.set_mobile_number(new_update)
                                        elif order == 2:
                                            new_update = input("Change (" + found.get_email_address() + ") to ==> ")
                                            found.set_email_address(new_update)
                                        elif order == 2:
                                            new_update = input("Change (" + found.get_address() + ") to ==> ")
                                            found.set_address(new_update)
                                        elif order == 2:
                                            new_update = input("Change (" + found.get_postal_code() + ") to ==> ")
                                            found.set_postal_code(new_update)
                                        print("UPDATED !")
                                        break
                                    else:
                                        pass
                            elif order == 2:
                                print('\n' * 3)
                                print("________________ SEARCH MENU -> DELETE CONTACT __________________")
                                contact_fname = found.get_first_name()
                                contact_lname = found.get_last_name()
                                contact_id = name_trie.get(found.get_first_name() + found.get_last_name()).information
                                contact_phone_number = found.get_mobile_number()
                                name_trie.delete(contact_fname + contact_lname)
                                phone_trie.delete(contact_phone_number)
                                contacts_list[int(hash_funcion(contact_id))].delete_value(found)
                                print(contact_fname, contact_lname, "DELETED !")
                                contacts_size -= 1
                                break
                            elif order == 3:
                                break
                    else:
                        print(phone, "not found !")
                    break
                elif order == 3:
                    break
        elif order == 3:
            while True:
                try:
                    # add new contact in which you have to obbey the phone number rules and postal code and email too !
                    print('\n'*3)
                    print("________________ ADD NEW CONTACT MENU __________________")
                    print("Please enter the new contact's information :")
                    fname = input("Name : ")
                    lname = input("Last Name : ")
                    mobile = input("Mobile Number : ")
                    email = input("Email Address : ")
                    address = input("Address : ")
                    postal = input("Postal Code : ")
                    if len(fname.strip()) > 0 and len(lname.strip()) > 0 and len(email.strip()) > 0 and \
                        len(address.strip()) > 0 and len(postal.strip()) > 0 and len(mobile.strip()) > 0 and \
                        mobile.strip().isdigit() and mobile.strip().startswith("09") and len(postal.strip()) > 0 and \
                        postal.strip().isdigit() and \
                        re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email).start() == 0:
                        if check_taken_name_or_phone(fname + lname, mobile) is False:
                            new_contact = Contact(fname.strip(), lname.strip(), mobile.strip(), email.strip(), address.strip(), postal.strip())
                            add_new_contact(new_contact, main_id_counter)
                            main_id_counter += 1
                            contacts_size += 1
                            break
                except:
                    print("INVALID INPUT !")
            print(new_contact.get_first_name(), new_contact.get_last_name(), "ADDED !")
        elif order == 4:
            # in this section by entering a name you will be having suggestions bsaed on each character that you
            # enter form a name
            given_word = input("Please enter the name: ")
            print("===========================================================")
            name_trie.pre_search(given_word)
            print("===========================================================")
    except:
        pass