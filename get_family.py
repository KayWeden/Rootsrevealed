import type
def get_ancestors(p):
    all_ancestors = [p]
    for i in all_ancestors:
        for j in i.get_parents():
            if j not in all_ancestors:
                all_ancestors.append(j)
    return all_ancestors

def get_all_children(p):
    all_children = [p]
    for i in all_children:
        for j in i.get_children():
            if j not in all_children:
                all_children.append(j)
    return all_children

print(get_ancestors(bsp_Person))
