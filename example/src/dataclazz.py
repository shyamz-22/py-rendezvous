from dataclasses import dataclass


@dataclass
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0


if __name__ == '__main__':
    item_cola_a = InventoryItem(name='cola',
                                unit_price=20.0,
                                quantity_on_hand=10)
    item_cola_b = InventoryItem(name='cola',
                                unit_price=20.0,
                                quantity_on_hand=10)

    print('Equal? ', item_cola_a == item_cola_b)
    print('Item', item_cola_b)
