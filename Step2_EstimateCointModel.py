#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import statsmodels.api as sapi
import numpy as np
import statsmodels.tsa.api as tsaapi


# In[2]:


import os


# In[202]:


class CointModel(object):
    def __init__(self,X1,X2):
        '''
        一般来说将X1作为因变量，将X2作为自变量
        尽量提供对数价格
        '''
        self.X1 = X1
        self.X2 = X2
        self.b = 0 #截距项
        self.beita = 1 #系数项
        self.e = [] #残差
        
    def adf_test_x1_x2(self):
        '''
        检验X1，X2是否为同阶单整序列
        返回 X1,X2 adf 检验的P值
        '''
        result_x1 = tsaapi.stattools.adfuller(self.X1)
        result_x2 = tsaapi.stattools.adfuller(self.X2)
        return result_x1[1],result_x2[1]
        
    def adf_test_dx1_dx2(self):
        '''
        检验差分后的X1，X2是否是平稳的
        返回 dX1，dX2 adf 检验的P值
        '''
        result_dx1 = tsaapi.stattools.adfuller(pd.Series(self.X1).diff().dropna())
        result_dx2 = tsaapi.stattools.adfuller(pd.Series(self.X2).diff().dropna())
        return result_dx1[1],result_dx2[1]
    
    def fit(self,print_summary=False):
        '''
        print_summary:bool，是否输出回归结果
        返回 b,beita，残差
        '''
        ###拟合，
        self.X2 = sapi.add_constant(self.X2)
        ols_model = sapi.OLS(self.X1,self.X2)
        ols_result = ols_model.fit()
        if print_summary:
            print(ols_result.summary2())
        self.b = ols_result.params[0]
        self.beita = ols_result.params[1]
        self.e = ols_result.resid
        return self.b,self.beita,self.e
    
    def resid_stationary_test(self,maxlag=None):
        '''
        检验残差是否平稳
        maxlag:确定最大滞后项，若无则自动设置AIC为准则
        返回 adf检验统计量，Pvalue，滞后阶数，critical values
        '''
        adfresult = tsaapi.stattools.adfuller(self.e,maxlag=maxlag)
        return adfresult[0],adfresult[1],adfresult[2],adfresult[4]