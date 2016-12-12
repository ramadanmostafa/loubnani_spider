# -*- coding: utf-8 -*-
import scrapy
from loubnani.items import LoubnaniItem

class LoubnanispiderSpider(scrapy.Spider):
    name = "loubnaniSpider"
    allowed_domains = ["loubnani.fr"]
    def start_requests(self):
        f = open("loubnani\\spiders\\test.txt")
        for line_url in f:
            yield scrapy.Request(line_url,callback = self.parse_item)

    def parse_item(self, response):
        item = LoubnaniItem()
        item["link"] = response.url
        item["title"] = response.xpath('//*[@id="pb-left-column"]/h1/text()').extract_first()
        item["descreption"] = response.xpath('//*[@id="short_description_content"]/p/text()').extract_first()
        item["Price_curreny"] = "Euros"
        item["Price"] = response.xpath('//*[@id="our_price_display"]/text()').extract_first().split()[0]
        item["Comments"] = response.xpath('//*[@id="product_comments_block_tab"]/p/text()').extract_first()
        item["Categorie1"] = response.xpath('//*[@id="center_column"]/div[1]/a[2]/text()').extract_first()
        item["Categorie2"] = response.xpath('//*[@id="center_column"]/div[1]/a[3]/text()').extract_first()
        item["Categorie3"] = item["title"]
        item["Category_tree"] = item["Categorie1"] + "/" + item["Categorie2"] + "/" + item["Categorie3"]
        item["Image_URL_bigpic"] = response.xpath('//*[@id="bigpic"]/@src').extract_first()
        item["Image_title_bigpic"] = response.xpath('//*[@id="bigpic"]/@title').extract_first()
        item["Image_Height_bigpic"] = response.xpath('//*[@id="bigpic"]/@height').extract_first()
        item["Image_width_bigpic"] = response.xpath('//*[@id="bigpic"]/@width').extract_first()
        item["Image_Length_bigpic"] = response.xpath('//*[@id="bigpic"]/@length').extract_first()
        item["thickBox_pic"] = response.xpath('//*[@id="thumbnail_434"]/a/@href').extract_first()
        item["thunbnail_url"] = response.xpath('//*[@id="thumb_434"]/@src').extract_first()
        item["Thumbnail_height"] = response.xpath('//*[@id="thumb_434"]/@height').extract_first()
        item["Thumbnail_width"] = response.xpath('//*[@id="thumb_434"]/@width').extract_first()
        item["En_savoir_plus"] = response.xpath('//*[@id="idTab1"]/p/span/text()').extract_first()
        item["commentaires"] = item["Comments"]
        item["weight_units"] = "Grammes"
        item["full_descreption"] = "" #--------------------------------------------------------------------------------
        item["additional_information"] = "" #--------------------------------------------------------------------------------
        item["net_weight"] = "" #--------------------------------------------------------------------------------
        item["total_weight"] = "" #--------------------------------------------------------------------------------
        item["volume_units"] = "" #--------------------------------------------------------------------------------
        item["volume"] = "" #--------------------------------------------------------------------------------
        item["Qty_availibity_value"] = "" #--------------------------------------------------------------------------------
        item["OutofStock"] = "" #--------------------------------------------------------------------------------
        item["productCategory_title"] = "" #--------------------------------------------------------------------------------
        item["productCategory_img_url"] = "" #--------------------------------------------------------------------------------
        item["productCategory_img_alt"] = "" #--------------------------------------------------------------------------------
        item["Crosseling_products_title"] = "" #--------------------------------------------------------------------------------
        item["Crosseling_products_img_url"] = "" #--------------------------------------------------------------------------------
        item["Crosseling_products_url"] = "" #--------------------------------------------------------------------------------
        item["Fiche_technique_wysigwig"] = "" #--------------------------------------------------------------------------------
        item["Fiche_technique_items"] = "" #--------------------------------------------------------------------------------
        item["Fiche_technique_values"] = "" #--------------------------------------------------------------------------------

        yield item
        #all_categories = response.xpath('//*[@id="categories_block_left"]/div/ul/li/ul/li/a/@href').extract()
        # title = response.xpath('//*[@id="pb-left-column"]/h1/text()').extract_first()
        # Categorie1 = response.xpath('//*[@id="center_column"]/div[1]/a[2]/text()').extract_first(),
        # Categorie2 = response.xpath('//*[@id="center_column"]/div[1]/a[3]/text()').extract_first(),

#        for i in range(len(c1)):
#        yield {
##            'link' : response.url,
##            'title' : response.xpath('//*[@id="pb-left-column"]/h1/text()').extract_first(),
##            'descreption' : response.xpath('//*[@id="short_description_content"]/p/text()').extract_first(),
##            #'additional_informations' : response.xpath('').extract_first(),#--------------------------------------------------
##            'weight_units' : "Grammes",
##            'net_weight' : response.xpath('//*[@id="idTab2"]/li[1]/text()').extract_first(),
##            'total_weight' : response.xpath('//*[@id="idTab2"]/li[2]/text()').extract_first(),
##            #'volume_units' : response.xpath('').extract_first(),#--------------------------------------------------
##            #'volume' : response.xpath('').extract_first(),#--------------------------------------------------
##            #'Qty_availibity_value' : response.xpath('').extract_first(),#--------------------------------------------------
##            #'OutofStock' : response.xpath('').extract_first(),#--------------------------------------------------
##            'Price_curreny' : "Euros",
##            'Price' : response.xpath('//*[@id="our_price_display"]/text()').extract_first().split()[0],
##            'Comments' : response.xpath('//*[@id="product_comments_block_tab"]/p/text()').extract_first(),
##            'Categorie1' : response.xpath('//*[@id="center_column"]/div[1]/a[2]/text()').extract_first(),
##            'Categorie2' : response.xpath('//*[@id="center_column"]/div[1]/a[3]/text()').extract_first(),
##            'Categorie3' : title ,
##            'Category_tree' :  str(Categorie1) + "/" + str(Categorie2) + "/" + str(title),
##            'Image URL_bigpic' : response.xpath('//*[@id="bigpic"]/@src').extract_first(),
##            'Image_title_bigpic' : response.xpath('//*[@id="bigpic"]/@title').extract_first(),
##            'Image_Height_bigpic' : response.xpath('//*[@id="bigpic"]/@height').extract_first(),
##            'Image_width_bigpic' : response.xpath('//*[@id="bigpic"]/@width').extract_first(),
##            'Image_Length_bigpic' : response.xpath('//*[@id="bigpic"]/@length').extract_first(),
##            'thickBox_pic' : response.xpath('//*[@id="thumbnail_434"]/a/@href').extract_first(),
##            'thunbnail_url' : response.xpath('//*[@id="thumb_434"]/@src').extract_first(),
##            'Thumbnail_height' : response.xpath('//*[@id="thumb_434"]/@height').extract_first(),
##            'Thumbnail_width' : response.xpath('//*[@id="thumb_434"]/@width').extract_first(),
##            'productCategory_title' : response.xpath('//*[@id="productscategory_list"]/ul/li/a/@title').extract(),
##            'productCategory_img_url' : response.xpath('//*[@id="productscategory_list"]/ul/li/a/img/@src').extract(),
##            'productCategory_img_alt' : response.xpath('//*[@id="productscategory_list"]/ul/li/a/img/@alt').extract(),
##            'Crosseling_products_title' : response.xpath('//*[@id="crossselling_list"]/ul/li/p/a/@title').extract(),
##            'Crosseling_products_img_url' : response.xpath('//*[@id="crossselling_list"]/ul/li/a/img/@src').extract(),
##            'Crosseling_products_url' : response.xpath('//*[@id="crossselling_list"]/ul/li/p/a/@href').extract(),
##            'En_savoir_plus' : response.xpath('//*[@id="idTab1"]/p/span/text()').extract_first(),
##            'Fiche_technique_wysigwig' : response.xpath('//*[@id="idTab2"]').extract_first(),
##            'Fiche_technique_items' : response.xpath('//*[@id="idTab2"]/li/span/text()').extract(),
##            'Fiche_technique_values' : response.xpath('//*[@id="idTab2"]/li/text()').extract(),
##            'commentaires' : response.xpath('//*[@id="product_comments_block_tab"]/p/text()').extract_first(),
#            }
