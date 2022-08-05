<template>
  <el-dialog
    :title="showTitle"
    :visible.sync="dialogVisible"
    width="800px"
    :before-close="closeDiglog"
  >
    <el-form
      :model="taskForm"
      :rules="rules"
      ref="ruleForm"
      label-width="100px"
      class="demo-ruleForm"
    >
      <el-form-item label="任务名称" prop="name">
        <el-input v-model="taskForm.name" />
      </el-form-item>
      <el-form-item label="任务描述" prop="desc">
        <el-input type="textarea" v-model="taskForm.describe" />
      </el-form-item>
      <el-card style="width: 29%; float: left">
        <div style="margin-top: 6px">
          <el-tree
            :data="moduleDate"
            node-key="id"
            default-expand-all
            :expand-on-click-node="false"
            @node-click="nodeClick"
          >
            <span class="custom-tree-node" slot-scope="{ node }">
              <span style="float: left">{{ node.label }}</span>
            </span>
          </el-tree>
        </div>
      </el-card>

      <el-form-item>
        <div style="width: 70%; float: right">
          <el-table :data="caseData" border @row-click="caseRowClick">
            <el-table-column prop="id" label="ID" width="40"> </el-table-column>
            <el-table-column prop="name" label="名称"> </el-table-column>
          </el-table>
        </div>
      </el-form-item>
      <el-form-item style="text-align: right">
        <el-button type="primary" @click="submitForm('ruleForm')"
          >确 定</el-button
        >
        <el-button @click="closeDiglog">取消</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>
<script>
import ProjectApi from "../../request/project";
import ModuleApi from "../../request/module";

export default {
  props: ["title", "pid"],
  name: "projectDialog",
  data() {
    return {
      showTitle: "",
      dialogVisible: true,
      taskForm: {
        name: "",
        describe: "",
      },
      moduleDate: [],
      rules: {
        name: [{ required: true, message: "请输入任务名称", trigger: "blur" }],
      },
      fileList: [],
    };
  },
  mounted() {
    if (this.title === "create") {
      this.showTitle = "创建任务";
    } else if (this.title === "edit") {
      this.showTitle = "编辑任务";
      // this.initProject();
    }
    this.initModulelist();
  },
  methods: {
    closeDiglog() {
      this.$emit("cancel", {});
    },
    //查询模块列表
    async initModulelist() {
      const req = { project_id: this.pid };
      const resp = await ModuleApi.getProModule(req);
      if (resp.success === true) {
        this.moduleDate = resp.items;
      }
    },
    //获取项目详情
    async initProject() {
      const resp = await ProjectApi.getProject(this.pid);
      if (resp.success === true) {
        this.projectForm = resp.item;
        this.fileList.push({
          name: resp.item.image,
          url: "static/images/" + resp.item.image,
        });
        this.$message.success("查询成功");
      } else {
        this.$message.error("查询失败");
      }
    },
    // 创建项目
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          if (this.title === "create") {
            ProjectApi.createProject(this.projectForm).then((resp) => {
              if (resp.success === true) {
                this.closeDiglog();
                this.$message.success("创建成功！");
              } else {
                this.$message.error(resp.error.message);
              }
            });
          } else if (this.title === "edit") {
            ProjectApi.updateProject(this.pid, this.projectForm).then(
              (resp) => {
                if (resp.success === true) {
                  this.closeDiglog();
                  this.$message.success("编辑成功！");
                } else {
                  this.$message.error(resp.error.message);
                }
              }
            );
          }
        } else {
          return false;
        }
      });
    },
  },
};
</script>
