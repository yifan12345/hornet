<template>
  <div class="home">
    <el-card class="box-card">
      <div style="height: 50px; text-align: left; width: 100%">
        <el-button type="primary" @click="showCreate">创建</el-button>
      </div>
      <div style="height: 700px">
        <div v-for="o in tableData" :key="o" class="text item">
          <el-col :span="7" class="project-card">
            <el-card style="width: 300px">
              <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
              <div slot="header" class="clearfix">
                <span>{{ o.name }}</span>
                <el-button style="float: right; padding: 3px 0" type="text item"
                  >操作按钮</el-button
                >
              </div>
              {{ o.address }}
            </el-card>
          </el-col>
        </div>
      </div>
      <div style="height: 100%; text-align: right">
        <el-pagination
          background
          @current-change="handleCurrentChange"
          layout="prev, pager, next"
          :page-size="req.size"
          :total="total"
        >
        </el-pagination>
      </div>
    </el-card>
    <!--引入子组件-->
    <projectDialog v-if="showDialog"/>
  </div>
</template>

<script>
// @ is an alias to /src
import projectDialog from "@/components/projects/projectDialog.vue"
import ProjectApi from "../../request/project";
export default {
  name: "Project",
  comments: { projectDialog },
  data() {
    return {
      tableData: [],
      req: {
        page: 1,
        size: 6,
      },
      total: 50,
      showDialog: false,
    };
  },
  created() {
    this.initProjectlist();
  },
  methods: {
    async initProjectlist() {
      const resp = await ProjectApi.getProjects(this.req);
      if (resp.success === true) {
        this.tableData = resp.items;
        this.total = resp.total;
        this.$message.success("查询成功");
      } else {
        this.$message.error("查询失败");
      }
    },
    showCreate() {
      this.showDialog = true;
    },
    //跳转到第几页
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.req.page = val;
      this.initProjectlist();
    },
  },
};
</script>
<style>
.box-card {
}
</style>
