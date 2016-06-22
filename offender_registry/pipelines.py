# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline

def clean_bulk(item, search_string, skip):
	k = []
	for lab in search_string:
		for i, j in enumerate(item):
			if j == lab:
				k.append(item[i+skip].strip())
	return k

def clean_bulk_bookends(item, search_string1, search_string2):
	pos1 = []
	pos2 = []
	if search_string2:
		stringlist = [x.strip() for x in search_string2]
	else:
		stringlist = ['','Conviction Date:']
	for i, j in enumerate(item):
		if j.strip() == search_string1:
			pos1.append(i+1)
		if len(pos1) > len(pos2) and j.strip() in stringlist:
			pos2.append(i)
	sels = []
	for i, j in enumerate(pos1):
		sels.append(''.join(item[j:pos2[i]]))
	return sels



class OffenderRegistryPipeline(object):

	def process_item(self, item, spider):
		item['name'] = [item['name'][0].strip()]
		if item['aliases']:
			item['aliases'] = [item['aliases'][0].replace(u'\u2022','-|-').encode('utf-8')]
		item['primary_residence'] = [item['primary_residence'][0].strip()]
		item['convict_date'] = clean_bulk(item['convict_date'], ['Conviction Date:'], 1)
		item['convict_location'] = clean_bulk(item['convict_location'], ['Location:'], 1)
		item['registr_authority'] = clean_bulk(item['registr_authority'], ['Registration Authority:', 'Jurisdiction:'], 1)
		item['charges'] = clean_bulk_bookends(item['charges'], 'Charges:', item['charge_details'])
		item['charge_details'] = [''.join(item['charge_details'])]
		item['custody_info'] = clean_bulk(item['custody_info'], ['Custody/Supervision Information'], 3)
		item['custody_agency'] = clean_bulk(item['custody_agency'], ['Agency:'], 1)
		v1 = clean_bulk(item['registr_status'], ['Registration Status:'], 1)
		v2 = clean_bulk(item['registr_status'], ['Registration Status:'], 2)
		if len(v1[0]) > len(v2[0]):
			item['registr_status'] = v1
		else:
			item['registr_status'] = v2
		item['tier'] = clean_bulk(item['tier'], ['Tier:'], 2)
		item['reg_term'] = clean_bulk(item['reg_term'], ['Reg. Term:'], 2)
		item['information_contact'] = clean_bulk(item['information_contact'], ['Information Contact:'], 2)
		item['current_reg_date'] = clean_bulk(item['current_reg_date'], ['Current Registration Date:'], 1)
		item['sex'] = clean_bulk(item['sex'], ['Sex:'], 2)
		item['DOB'] = clean_bulk(item['DOB'], ['Date of Birth:'], 2)
		item['curr_age'] = clean_bulk(item['curr_age'], ['Current Age:'], 2)
		item['height'] = clean_bulk(item['height'], ['Height:'], 2)
		item['weight'] = clean_bulk(item['weight'], ['Weight:'], 2)
		item['race'] = clean_bulk(item['race'], ['Race:'], 2)
		item['skin_tone'] = clean_bulk(item['skin_tone'], ['Skin Tone:'], 2)
		item['eye_color'] = clean_bulk(item['eye_color'], ['Eye Color:'], 2)
		item['hair_color'] = clean_bulk(item['hair_color'], ['Hair Color:'], 2)
		item['vehicles'] = clean_bulk_bookends([x.strip() for x in item['vehicles']], 'Vehicle Information', ['Exceptions'])
		return item

