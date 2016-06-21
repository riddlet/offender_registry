# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OffenderRegistryItem(scrapy.Item):
    # define the fields for your item here like:
    id_num = scrapy.Field()
    name = scrapy.Field()
    aliases = scrapy.Field()
    primary_residence = scrapy.Field()
    address_change_date = scrapy.Field()
    temp_residence = scrapy.Field()
    employ_address = scrapy.Field()
    school_address = scrapy.Field()
    convict_date = scrapy.Field()
    convict_location = scrapy.Field()
    registr_authority = scrapy.Field()
    charges = scrapy.Field()
    charge_details = scrapy.Field()
    custody_info = scrapy.Field()
    custody_agency = scrapy.Field()
    registr_status = scrapy.Field()
    tier = scrapy.Field()
    reg_term = scrapy.Field()
    information_contact = scrapy.Field()
    current_reg_date = scrapy.Field()
    sex = scrapy.Field()
    DOB = scrapy.Field()
    curr_age = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    race = scrapy.Field()
    skin_tone = scrapy.Field()
    eye_color = scrapy.Field()
    hair_color = scrapy.Field()
    vehicles = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
