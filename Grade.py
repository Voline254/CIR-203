class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, student_dict):
        new_node = Node(student_dict)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def show_students(self):
        current = self.head

        while current:
            student = current.data
            print("Name:", student["name"])
            print("Adm No:", student["adm_no"])
            print("Grades:", student["grades"])
            print("---------------------")
            current = current.next


students = LinkedList()
students.add_student({
    "name": "Alice",
    "adm_no": "ADM001",
    "grades": [78, 85, 90]
})

students.add_student({
    "name": "Brian",
    "adm_no": "ADM002",
    "grades": [65, 72, 80]
})

students.add_student({
    "name": "Cynthia",
    "adm_no": "ADM003",
    "grades": [88, 91, 94]
})

students.show_students()
