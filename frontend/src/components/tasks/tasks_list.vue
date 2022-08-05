<template>
  <div class="tasks">
    <div style="height: 100px; text-align: left; width: 100%">
      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-form-item label="项目列表">
          <el-select v-model="projectTaskId" placeholder="请选择项目">
            <el-option
              v-for="item in projectTaskOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="createTasks()" size="medium"
            >创建</el-button
          >
        </el-form-item>
      </el-form>
    </div>
    <el-row>
      <div v-for="(item, index) in tableData" :key="index">
        <el-col :span="7" class="project-card">
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>{{ item.name }} </span>
              <span style="float: right; padding: 3px 0" />
              <div style="float: right">
                <el-dropdown>
                  <span class="el-dropdown-link">
                    <i class="el-icon-setting" />
                  </span>
                  <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item>
                      <el-button type="text" @click="showEdit(item.id)"
                        >编辑
                      </el-button>
                    </el-dropdown-item>
                    <el-dropdown-item>
                      <el-button type="text" @click="deleteProject(item.id)"
                        >删除
                      </el-button>
                    </el-dropdown-item>
                  </el-dropdown-menu>
                </el-dropdown>
              </div>
            </div>
            <!--              <div>-->
            <!--                {{ item.describe }}-->
            <!--              </div>-->
            <img
              :src="item.image"
              class="image"
              style="height: 235px; width: 235px"
              alt=""
            />
          </el-card>
        </el-col>
      </div>
    </el-row>
    <div style="height: 100%; text-align: right"></div>
    <div style="width: 100%; text-align: right">
      <el-pagination
        cy-data="ProjectPagination"
        background
        @current-change="handleCurrentChange"
        layout="prev, pager, next"
        :page-size="req.size"
        :total="total"
      >
      </el-pagination>
    </div>
    <tasksDialog
      v-if="dialogFlag"
      @cancel="closeDiglog"
      :title="dialogTitle"
      :pid="projectTaskId"
    ></tasksDialog>
  </div>
</template>

<script>
// @ is an alias to /src
import ProjectApi from "../../request/project";
import tasksDialog from "./tasksDialog";

export default {
  name: "tasks",
  components: {
    tasksDialog,
  },
  data() {
    return {
      projectTaskId: "",
      projectTaskOptions: [],
      formInline: {
        user: "",
        region: "",
      },
      tableData: [],
      total: 50,
      dialogFlag: false,
      dialogTitle: "create",
      req: {},
    };
  },
  mounted() {
    this.initProjectlist();
  },
  methods: {
    onSubmit() {
      console.log("submit!");
    },
    //初始化项目列表接口
    async initProjectlist() {
      const resp = await ProjectApi.getProjects(this.req);
      if (resp.success === true) {
        this.projectTaskId = resp.items[0].id;
        for (let i = 0; i < resp.items.length; i++) {
          this.projectTaskOptions.push({
            value: resp.items[i].id,
            label: resp.items[i].name,
          });
        }
      }
    },
    showEdit(id) {
      this.curretProjectId = id;
      this.dialogTitle = "edit";
      this.dialogFlag = true;
    },
    async deleteProject(id) {
      const resp = await ProjectApi.delProject(id);
      if (resp.success === true) {
        this.tableData = resp.items;
        this.total = resp.total;
        this.$message.success("删除成功");
        this.initProjectlist();
      } else {
        this.$message.error("删除失败");
      }
    },
    createTasks() {
      this.dialogTitle = "create";
      this.dialogFlag = true;
    },
    closeDiglog() {
      this.dialogFlag = false;
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
