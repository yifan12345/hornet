<template>
    <el-dialog
      :title="showTitle"
      :visible.sync="dialogVisible"
      width="40%"
      :before-close="closeDiglog">

      <el-form :model="projectForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="项目名称" prop="name">
          <el-input v-model="projectForm.name"/>
        </el-form-item>
        <el-form-item label="项目描述" prop="desc">
          <el-input type="textarea" v-model="projectForm.describe"/>
        </el-form-item>
<!--        <el-form-item label="上传图片" prop="desc">-->
<!--          <el-upload-->
<!--            class="upload-demo"-->
<!--            :action="updateURL"-->
<!--            :on-preview="handlePreview"-->
<!--            :on-remove="handleRemove"-->
<!--            :file-list="fileList"-->
<!--            list-type="picture">-->
<!--            <el-button size="small" type="primary">点击上传</el-button>-->
<!--            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>-->
<!--          </el-upload>-->
<!--        </el-form-item>-->
        <el-form-item style="text-align: right">
          <el-button type="primary" @click="submitForm('ruleForm')">确 定</el-button>
          <el-button @click="closeDiglog">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
</template>
<script>
  import ProjectApi from "../../request/project"
  export default {
    props:['title','pid'],
    name: "projectDialog",
    data() {
      return {
        showTitle:"",
        updateURL:"http://127.0.0.1:8000/api/projects/upload",
        dialogVisible: true,
        projectForm: {
          name: '',
          describe: '',
          image:'4414c173d96eeb45357529422daf9afd.png'
        },
        rules: {
          name: [
            { required: true, message: '请输入项目名称', trigger: 'blur' },
          ],
        }
      };
      },
    mounted(){
      if(this.title === "create"){
        this.showTitle = "创建项目";
      }else if(this.title === "edit"){
        this.showTitle = "编辑项目";
        this.initProject()
      }
    },
    methods: {
      closeDiglog() {
          this.$emit('cancel', {})
      },
      async initProject() {
        const resp = await ProjectApi.getProject(this.pid);
        if (resp.success === true) {
          this.projectForm = resp.item;
          this.$message.success("查询成功")
        } else {
          this.$message.error("查询失败")
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
                  this.$message.success("创建成功！")
                } else {
                  this.$message.error(resp.error.message)
                }
              })
            } else if (this.title === "edit") {
              ProjectApi.updateProject(this.pid, this.projectForm).then((resp) => {
                  if (resp.success === true) {
                    this.closeDiglog();
                    this.$message.success("编辑成功！")
                  } else {
                    this.$message.error(resp.error.message)
                  }
                }
              )
            }
          } else {
            return false
            }
          });
        },
      },
    };

</script>
