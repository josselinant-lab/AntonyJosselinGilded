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

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=5, quality=80)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 5)

    def test_backstage_increases_by_1_above_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 21)

    def test_backstage_increases_by_2_at_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 22)

    def test_backstage_increases_by_3_at_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 23)

    def test_backstage_quality_0_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_conjured_degrades_by_2(self):
        items = [Item("Conjured Mana Cake", sell_in=10, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 18)

    def test_conjured_degrades_by_4_after_expiration(self):
        items = [Item("Conjured Mana Cake", sell_in=0, quality=20)]
        GildedRose(items).update_quality()
        self.assertEqual(items[0].quality, 16)

        
if __name__ == '__main__':
    unittest.main()
