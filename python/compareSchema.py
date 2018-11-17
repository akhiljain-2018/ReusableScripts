#! /usr/bin/env python
import csv

from datadiff import diff # Dict diff
import click

@click.command()
@click.option('--files','-f',multiple=True, default='',help='Compare files by data in csv')
def main(files):
	#oldDict=get_dict('OldSchema.csv')
	#newDict=get_dict('NewSchema.csv')
	oldDict=get_dict(files[0])
	newDict=get_dict(files[1])
	
	print(diff(oldDict,newDict))
	
def get_dict(filename):
	with open(filename,mode='r') as fp:
		csv_reader=csv.DictReader(fp)
		dataDict={}
		for row in csv_reader:
			dataDict[row['name'].lower()]=row['type']
		return dataDict




if __name__ == '__main__':
	main()