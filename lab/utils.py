class TotalItemDetails:
    def __init__(self, **kwargs):
        self.item_name = kwargs['item_name']
        self.total_qty = kwargs['total_qty']
        self.category = kwargs['category']
        self.lab = kwargs['lab']
    
    def __str__(self):
        return self.item_name


def get_total_item_qty(items):
    total_dict = {}
    for item in items:
        if not str(item) in total_dict:
            item_obj = TotalItemDetails(item_name = item.item_name, total_qty = item.qty, category = item.category, lab = item.lab)
            total_dict[str(item)] = item_obj
        else:
            item_obj = total_dict[str(item)]
            item_obj.total_qty += item.qty
            total_dict[str(item)] = item_obj
            
    context_list = list(total_dict.values())
    return context_list