# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LoubnaniItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    descreption = scrapy.Field()
    full_descreption = scrapy.Field()
    additional_information = scrapy.Field()
    weight_units = scrapy.Field()
    net_weight = scrapy.Field()
    total_weight = scrapy.Field()
    volume_units = scrapy.Field()
    volume = scrapy.Field()
    Qty_availibity_value = scrapy.Field()
    OutofStock = scrapy.Field()
    Price_curreny = scrapy.Field()
    Price = scrapy.Field()
    Comments = scrapy.Field()
    Categorie1 = scrapy.Field()
    Categorie2 = scrapy.Field()
    Categorie3 = scrapy.Field()
    Category_tree = scrapy.Field()
    Image_URL_bigpic = scrapy.Field()
    Image_title_bigpic = scrapy.Field()
    Image_Height_bigpic = scrapy.Field()
    Image_width_bigpic = scrapy.Field()
    Image_Length_bigpic = scrapy.Field()
    thickBox_pic = scrapy.Field()
    thunbnail_url = scrapy.Field()
    Thumbnail_height = scrapy.Field()
    Thumbnail_width = scrapy.Field()
    productCategory_title = scrapy.Field()
    productCategory_img_url = scrapy.Field()
    productCategory_img_alt = scrapy.Field()
    Crosseling_products_title = scrapy.Field()
    Crosseling_products_img_url = scrapy.Field()
    Crosseling_products_url = scrapy.Field()
    En_savoir_plus = scrapy.Field()
    Fiche_technique_wysigwig = scrapy.Field()
    Fiche_technique_items = scrapy.Field()
    Fiche_technique_values = scrapy.Field()
    commentaires = scrapy.Field()
