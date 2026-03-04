# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            is_aged_brie = item.name == "Aged Brie"                                          
            is_backstage = item.name == "Backstage passes to a TAFKAL80ETC concert"          
            is_sulfuras  = item.name == "Sulfuras, Hand of Ragnaros"
            is_conjured  = "Conjured" in item.name 

            if is_sulfuras:
                continue

            item.sell_in -= 1

            if is_aged_brie:
                item.quality += 1
                if item.sell_in < 0:
                    item.quality += 1

            elif is_backstage:
                item.quality += 1
                if item.sell_in < 10:
                    item.quality += 1
                if item.sell_in < 5:
                    item.quality += 1
                if item.sell_in < 0:
                    item.quality = 0

            elif is_conjured:
                item.quality -= 2
                if item.sell_in < 0:
                    item.quality -= 2

            else:
                item.quality -= 1
                if item.sell_in < 0:
                    item.quality -= 1

            if item.quality > 50:
                item.quality = 50
            if item.quality < 0:
                item.quality = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
