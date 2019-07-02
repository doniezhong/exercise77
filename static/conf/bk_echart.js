// 横向柱状图
function createEHorBarChart(conf){
    let myChart = echarts.init(document.getElementById(conf.selector));
    let  legendData = [];
    for(let i=0; i < conf.data.series.length; i++){
        legendData.push(conf.data.series[i].name);
    }
    myChart.setOption({
        title : conf.data.title,
        tooltip : {
            trigger: 'axis'
        },
        legend: {
            data:legendData
        },
        toolbox: {
            show : true,
            feature : {
                mark : {show: true},
                dataView : {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar']},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        calculable : true,
        xAxis : [
            {
                type : 'value',
                boundaryGap : [0, 0.01]
            }
        ],
        yAxis : [
            {
                type : 'category',
                data : conf.data.yAxis
            }
        ],
        series : conf.data.series
    })
}

// 柱状图和折线图
function createEBarChart(conf){
    let myChart = echarts.init(document.getElementById(conf.selector));
    let legendData = [];//存放变量的name
    for(let i = 0; i < conf.data.series.length; i++){
        legendData.push(conf.data.series[i].name);
    }
    myChart.setOption({
        title : conf.data.title,
        legend: {
            y: 'bottom',
            data:legendData
        },
        tooltip : {
            trigger: 'axis'
        },
        toolbox: {
            show : true,
            feature : {
                mark : {show: true},
                dataView : {show: true, readOnly: false},
                magicType : {show: true, type: ['line', 'bar']},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        calculable : true,
        yAxis : [
            {
                type : 'value',
                splitArea : {show : true}
            }
        ],
        xAxis : {
            type : 'category',
            data: conf.data.xAxis,
        },
        series : conf.data.series
    })
}

 var createCharts = function(type, selectors, data) {
     for (let i=0; i < data.length; i++){
         let conf = {
             selector: selectors[i],
             data: data[i]
         };
         bk_chart[type](conf)
     }
 };

var bk_chart = {
    line: createEBarChart,
    bar: createEBarChart,
    hor_bar: createEHorBarChart,
};
