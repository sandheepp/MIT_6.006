def reorder_students(D):
    length = len(D)
    iter_node = D.head
    for _ in range(n-1):
        iter_node = iter_node.next
    a = iter_node # pointer value of nth element
    b = iter_node.next # pointer value of the (n+1)th element
    iter_node_prev = a
    iter_node = b
  
    for _ in range(n):
        iter_node_next = iter_node.next
        iter_node.next = iter_node_prev
        iter_node_prev, iter_node = iter_node, iter_node_next
    c = iter_node_prev
    a.next = c
    b.next = None