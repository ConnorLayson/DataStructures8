
class DoctorNode:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Doctor name must be a non-empty string.")

        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side):
        if side not in ("left", "right"):
            raise ValueError("Side must be 'left' or 'right'.")

        new_doctor = DoctorNode(doctor_name)

        if self.root is None:
            raise ValueError("Cannot insert into a tree without a root.")

        parent = self._find_node(self.root, parent_name)

        if parent is None:
            raise ValueError(f"Parent doctor '{parent_name}' not found.")

        if getattr(parent, side) is not None:
            raise ValueError(f"The {side} position is already occupied.")

        setattr(parent, side, new_doctor)

    def _find_node(self, node, name):
        if node is None:
            return None

        if node.name == name:
            return node

        found = self._find_node(node.left, name)
        if found is not None:
            return found

        return self._find_node(node.right, name)

    def preorder(self, node):
        if node is None:
            return []

        return (
            [node.name]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )

    def inorder(self, node):
        if node is None:
            return []

        return (
            self.inorder(node.left)
            + [node.name]
            + self.inorder(node.right)
        )

    def postorder(self, node):
        if node is None:
            return []

        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )
