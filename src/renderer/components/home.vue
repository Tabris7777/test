<template>
  <div class="home">

    <div class="title">电力平衡计算</div>

    <div>
       <el-button type="primary" @click="openTheDoor">配比选择</el-button>
        <el-button type="primary">其他1</el-button>
        <el-button type="primary">其他2</el-button>
        <el-button type="primary">其他3</el-button>
    </div>
   





    <el-dialog
      title="配比选择"
      :visible.sync="dialogVisible"
      width="30%"
      >
      <div>
        <el-checkbox-group v-model="checkList">
          <el-checkbox label="0">光伏</el-checkbox>
          <el-checkbox label="1">风电</el-checkbox>
          <el-checkbox label="2">负荷</el-checkbox>
          <el-checkbox label="3">水电</el-checkbox>
        </el-checkbox-group>
      </div>

      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="openThePage">确 定</el-button>
        <el-button @click="dialogVisible = false">取 消</el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>

  export default {
    name: 'landing-page',
    data () {
      return {
        radio: '1',
        dialogVisible:false,
        checkList: []
      };
    },
    methods: {
      openTheDoor(){
        this.dialogVisible=true;
        this.checkList=[];
      },
      openThePage(){
        if(this.checkList.length===0){
          this.$message.error('请选择配比');
          return false;
        }
        this.dialogVisible=false;
        this.$router.push({
          path: '/secondHome',
          query: {checkList: this.checkList}
        })
        localStorage.setItem("checkList",JSON.stringify(this.checkList))
      }
    }
  }
</script>

<style lang="less">

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  .home{
    display:flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width:100%;
    height:100%;
    .title{
      margin-bottom:50px;
      font-size: 48px;
      font-family: BentonSans-Bold, BentonSans;
      font-weight: bold;
    }
  }
  
</style>
