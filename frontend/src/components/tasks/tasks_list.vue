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
    <div>
      <el-table :data="tableData" border style="width: 100%">
        <el-table-column fixed prop="id" label="ID" width="60"/>
        <el-table-column prop="name" label="姓名" width="120"/>
        <el-table-column prop="describe" label="描述" width="500"/>
        <el-table-column prop="create_time" label="创建时间" width="250"/>
        <el-table-column prop="update_time" label="更新时间" width="250"/>
        <el-table-column label="运行" width="50">
          <el-button type="text" size="medium" icon="el-icon-stopwatch" />
        </el-table-column>
        <el-table-column fixed="right" label="操作" width="250">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
            <el-button type="text" size="small">编辑</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div style="text-align: right">
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
import TasksApi from "../../request/tasks";
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
      projectForm: {
        id: 1,
      },
      total: 50,
      dialogFlag: false,
      dialogTitle: "create",
      req: {},
      tableData: []
    };
  },
  mounted() {
    this.initProjectlist();
  },
  methods: {
    deleteTask(index, rows) {
      rows.splice(index, 1);
    },
    onSubmit() {
      console.log("submit!");
    },
    //初始化任务列表

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
        this.initTasksList()
      }
    },
    async initTasksList() {
      const req = {project_id:this.projectForm.id}
      const resp = await TasksApi.getTasksList(req);
      if (resp.success === true) {
        this.tableData = resp.items
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
