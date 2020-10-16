<template>
  <div class="showChart">
      <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">返回首页</el-breadcrumb-item>
      <el-breadcrumb-item  :to="{ path: '/secondHome' }">返回上一页</el-breadcrumb-item>
      <el-breadcrumb-item >三级菜单</el-breadcrumb-item>

    </el-breadcrumb>
    <div id="main" class="echartBox"></div>
  </div>
</template>

<script>
import echarts from 'echarts'
  export default {
    name: 'landing-page',
    data () {
      return {
          checkList:{},
          tableData:[]
      };
    },
    created(){
      this.checkList=this.$route.query.checkList;
    },
    mounted(){
        this.tableData=JSON.parse(localStorage.getItem("tableData"));
        console.log(this.tableData);
        let legendList=[];
        let xData=[];
        let yData=[];
        let _this=this;
        let totalArr=[];
        let dataArr=[];
        for(let item in this.tableData){
            legendList.push(item);
            let arr=[]
            this.tableData[item].forEach((innerItem,index)=>{
                // console.log(_this.sumArr(innerItem))
                // arr.push(_this.sumArr(innerItem))
                arr.push(_this.sumArr(innerItem))

            })
            totalArr.push(arr);

            let arr2=[];
            this.tableData[item].forEach((innerItem,index)=>{
                arr2.push(index+1+"号")
            })
            dataArr=arr2;
        }
        var myChart = echarts.init(document.getElementById('main'))
      // 指定图表的配置项和数据
      var option = {
        title: {
          text: '',
          textStyle:{
                color:"#fff"
            }
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985'
            },
            
          }
        },
        legend: {
          data: legendList,
          textStyle:{
                color:"#fff"
            }
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: dataArr,
            axisLabel: {
                show: true,
                textStyle: {
                  color: "#fff"  //这里用参数代替了
                }
              },
          }
        ],
        yAxis: [
          {
            type: 'value',
             axisLabel: {
                show: true,
                textStyle: {
                  color: "#fff"  //这里用参数代替了
                }
              },
          },
        ],
        series: [
          {
            name: '总体',
            type: 'line',
            stack: '总量',
            areaStyle: {},
            data: totalArr[0]
          },
          {
            name: '缺电',
            type: 'line',
            stack: '总量',
            areaStyle: {},
            data: totalArr[1]
          },
          {
            name: '弃电',
            type: 'line',
            stack: '总量',
            areaStyle: {},
            data: totalArr[2]
          },
         
        ]
      }
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
    },
    methods: {
        sumArr(arr){
            return arr.reduce(function(prev,cur){
                // console.log(prev)
                // console.log(cur)
                // console.log("======")
                return parseFloat(prev) + parseFloat(cur);
            },0);
        }
    }
  }
</script>

<style>
.echartBox {
        /* width: 40%; */
        height: 520px;
        margin-left: 40px;
        margin-top: 100px;
      }
  .showChart{
      padding-left:40px;
    padding-top:50px;
    height:100%;
    background:#052345;
  }
</style>
