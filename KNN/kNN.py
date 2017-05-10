#/usr/bin/env python
#-*-coding:utf-8-*-

import numpy as np
import operator

def tackledata(x,datasets):
	'''
	processing data 
	Data normalization
	shape the data

	return x which has same shape of datasets
	'''

def caldistance(x,datasets):
	'''
	calculate the distance between x and datasets


	return dis that means distance between x and datasets
	'''


def classfity(kdata,k):
	'''
	calssfity accoding k and distance
	
	return result 
	'''

def fit(x,datasets,labels,k):
	'''
	x means input value
	datasets mean the known data
	labels mean the labels of the known data
	k means k shortest distances to decide the classfity

	return k shortest distance and their labels
	'''
	x = tackledata(x)

	dis = caldistance(x,datasets)



def predict(x,k):
	'''
	predict x 
	'''

	

