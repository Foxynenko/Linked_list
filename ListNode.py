class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Створюємо фіктивний вузол для зручності
    dummy = ListNode()
    current = dummy
    
    # Поки обидва списки не порожні
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Додаємо залишки одного зі списків (якщо є)
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    return dummy.next
