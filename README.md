# AH-pairs-trading
本科毕业设计，AH股配对交易策略研究

说明：

- Step1 GetData 为从使用Wind api 获取数据
- Step2 EstimateCointModel 为协整分析主要notebook，其中class CointModel为基于statsmodels的二次封装，CointModel将在Step3 import 调用
- Step3 BackTest 为回测主要notebook
  - class Position 头寸类
  - class Portfolio 资产类，为简易调用，直接在内部拥有成员函数 开仓：open_positon，平仓：close_positon，还有求夏普比率、最大回撤等函数。
  - def back_test 回测主函数，封装参数类型详见函数释义。

由于时间原因，代码暂时没有整理，将在后续进行整理