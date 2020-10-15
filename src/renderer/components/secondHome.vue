<template>
  <div class="secondHome">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">返回首页</el-breadcrumb-item>
      <el-breadcrumb-item >二级菜单</el-breadcrumb-item>
    </el-breadcrumb>



    <div class="itemContent">
      <div class="innerItem" v-for="(item,index) in checkList "  v-bind:key="index">
        <!-- <el-button @click="isHydropower(item)">{{item.name}}</el-button> -->

        <el-upload
        v-if="item.id==0"
        class="upload-demo"
        action="#"
        :on-change="handleChange"
        :file-list="fileList" 
        accept = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel"
        :auto-upload="false">
        <!-- <el-button  type="primary">光伏</el-button> -->
        <div class="homeIcon">
          <i></i>
          光伏
        </div>
        <!-- <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div> -->
      </el-upload>


      <el-upload
        v-if="item.id==1"
        class="upload-demo"
        action="#"
        :on-change="handleChange2"
        :file-list="fileList2" 
        accept = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel"
        :auto-upload="false">
        <div class="homeIcon">
          <i></i>
          风电
        </div>
        <!-- <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div> -->
      </el-upload>

      <el-upload
        v-if="item.id==2"
        class="upload-demo"
        action="#"
        :on-change="handleChange3"
        :file-list="fileList3" 
        accept = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel"
        :auto-upload="false">
        <div class="homeIcon">
          <i></i>
          负荷
        </div>
        <!-- <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div> -->
      </el-upload>


      

        <div v-if="item.id==3" >
          <div class="homeIcon" @click="isHydropower(item)">
          <i></i>
          水电
        </div>
          <!-- <el-button   type="primary" >水电</el-button> -->
          <span class="fivefiveopen">系统工作出力：{{showMsg1}}</span>
          <span class="fivefiveopen">每月电量:{{showMsg2}}</span>
        </div>
        <!-- <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div> -->
      </div>

      
      
      


    </div>


    <div class="itemButton">
      <el-button type="primary" @click="openChart">计算</el-button>
      <!-- <el-button type="warning">重置</el-button> -->
    </div>




    <el-dialog
      title="水电"
      :visible.sync="dialogVisible"
      width="30%"
      >
      <div >
        <el-input v-model="input1" placeholder="请输入系统工作出力"></el-input>
        <el-input class="toptoptop" v-model="input2" placeholder="请输入每个月的电量"></el-input>
      </div>

      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="openThePage">确 定</el-button>
        <el-button @click="dialogVisible = false">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { remote } from 'electron'

  export default {
    name: 'landing-page',
    data () {
      return {
        checkList:[],
        dialogVisible:false,
        input1:"",
        input2:"",
        fileList:[],
        fileList2:[],
        fileList3:[],
        showMsg1:"",
        showMsg2:""
      };
    },
    created(){
      let checkList=JSON.parse(localStorage.getItem("checkList"));
      let newList=[];
      for(let i=0;i<checkList.length;i++){
        newList.push({name:this.returnCnName(checkList[i]),id:checkList[i]});
      }
      this.checkList=newList;
    },
    methods: {
      isHydropower(data){
        if(data.id==3){
          this.dialogVisible=true;
         
        }else{
          


          return false;
        }
      },
      openThePage(){
          this.dialogVisible=false;
          this.showMsg1=this.input1;
          this.showMsg2=this.input2;

      },
      handleChange(file,fileList){
        if(fileList.length>0){
          this.fileList=[fileList[fileList.length-1]];
        }
      },
     handleChange2(file,fileList){
        if(fileList.length>0){
          this.fileList2=[fileList[fileList.length-1]];
        }
      },
      handleChange3(file,fileList){
        if(fileList.length>0){
          this.fileList3=[fileList[fileList.length-1]];
        }
      },

      openChart(){
        this.$router.push({
          path: "/showChart",
          query: {checkList: this.$route.query.checkList}
         })
      },
      returnCnName(param){
        switch (param){
          case "0":
            return "光伏";
          case "1":
            return "风电";
          case "2":
            return "负荷";
          case "3":
            return "水电";
        }
      }
    }
  }
</script>

<style>

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  .secondHome{
    padding-left:40px;
    padding-top:50px;
    background:url("../assets/bg2.png")no-repeat;
    height:100%;
  }
  .el-breadcrumb__item .el-breadcrumb__inner{
    color:#fff !important;
  }
  .el-breadcrumb__item:last-child .el-breadcrumb__inner{
    color:#90BFFF !important;
  }
  .el-breadcrumb{
    color:#fff;
  }
  .el-upload-list__item-name{
    color:#fff!important;
  }
  .itemContent{
    padding-top:100px;
    padding-left:100px;
  }
  .innerItem{
    margin-top:20px;
  }
  .itemButton{
    padding-top:100px;
    padding-left:100px;
  }
  .toptoptop{
    margin-top:30px;
  }

  .el-list-enter-active,
  .el-list-leave-active {
      transition: none !important;
    }

    .el-list-enter,
    .el-list-leave-active {
      opacity: 0 !important;
    }
    .el-upload-list {
      height: 40px !important;
    }

    .homeIcon{
      background: rgba(28, 68, 140, 0.5);
      border-radius: 5px;
      border: 1px solid #3593A6;
      color: #4EFFFF;
      width:120px;
      height:100px;
      display:flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    .homeIcon i{
      width:34px;
      height:44px;
      display:inline-block;
      background:url("../assets/icon.png")no-repeat;
      margin-bottom:10px;
    }
    .fivefiveopen{
      color:#fff;
    }
</style>
