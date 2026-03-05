# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
        
    def test_normal_item_degrades_by_1(self):
        items = [Item("Vest", sell_in=10, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 19)
        self.assertEqual(items[0].sell_in, 9)

    def test_normal_item_degrades_by_2_after_expiration(self):
        items = [Item("Vest", sell_in=0, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 18)

    def test_quality_never_negative(self):
        items = [Item("Vest", sell_in=0, quality=0)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_aged_brie_increases_quality(self):
        items = [Item("Aged Brie", sell_in=10, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 21)

    def test_aged_brie_increases_by_2_after_expiration(self):
        items = [Item("Aged Brie", sell_in=0, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 22)

    def test_quality_never_above_50(self):
        items = [Item("Aged Brie", sell_in=10, quality=50)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 50)

        
if __name__ == '__main__':
    unittest.main()
