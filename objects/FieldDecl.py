class FieldDecl:
    def __init__(self, object_node, type_node, node_list):
        self.object_node = object_node
        self.type_node = type_node
        self.node_list = node_list

    def __iter__(self):
        # first, yield everthing every one of the child nodes would yield.
        for child in self.node_list:
            for item in child:
                # the two for loops is because there's multiple children, and we need to iterate
                # over each one.
                yield item

        # finally, yield self
        yield self