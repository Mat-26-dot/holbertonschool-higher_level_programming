#!/usr/bin/env python3

from abc import ABC

class VerboseList(list):

    def append(self, item):
        print(f"Added {item} to the list")
        super().append(item)
    
    def extend(self, items):
        print(f"Extended the list with {len(items)} items: {items}")
        super().extend(items)
    
    def remove(self, item):
        print(f"Removed {item} from list")
        super().remove(item)    
    
    def pop(self, index=-1):
        item = self[index]
        print(f"Popped {item} from the list")
        return super().pop(index)