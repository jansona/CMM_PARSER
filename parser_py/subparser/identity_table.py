

class TableItem(object):

    def __init__(self, name=None, idt_type=None, value=None, domain=None):
        self.name = name
        self.type = idt_type
        self.value = value
        self.domain = domain


class Table(object):

    def __init__(self):

        self.table = dict()

    def add_item(self, name=None, idt_type=None, value=None, domain=None):
        item = TableItem(name, idt_type, value, domain)

        if item.name in self.table.keys():
            self.table[item.name].append(item)
        else:
            self.table[item.name] = [item]

    def get_item(self, name=None, domain=None):

        items = self.table[name]

        # TODO 暂时这么写
        return items[0]

    def show(self):

        for idt_name in self.table.keys():
            print(idt_name)
            print(self.table[idt_name])


idt_table = Table()
