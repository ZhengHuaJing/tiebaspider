# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests


class TiebaspiderPipeline(object):

	def __init__(self):
		self.file_name = './Image'
		# 创建文件夹
		if not os.path.exists(self.file_name):
			os.makedirs(self.file_name)

		# 图片名
		self.image_name = 1

		# 存放所有的图片url
		self.image_urls = []

	def process_item(self, item, spider):
		# 去除重复的图片url
		if item['image_url'] not in self.image_urls:
			self.image_urls.append(item['image_url'])

			with open(self.file_name + '/' + str(self.image_name) + '.jpg', 'wb') as file:
				file.write(requests.get(item['image_url']).content)
				self.image_name += 1

		return item
