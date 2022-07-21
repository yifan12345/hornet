<template>
    <el-dialog
            title="创建项目"
            :visible.sync="dialogVisible"
            width="40%"
            :before-close="closeDiglog">

      <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="项目名称" prop="name">
          <el-input v-model="ruleForm.name"/>
        </el-form-item>
        <el-form-item label="项目状态" prop="delivery">
          <el-switch v-model="ruleForm.delivery" style="right: 46%"/>
        </el-form-item>
        <el-form-item label="项目描述" prop="desc">
          <el-input type="textarea" v-model="ruleForm.desc"/>
        </el-form-item>
        <el-form-item style="text-align: right">
          <el-button type="primary" @click="submitForm('ruleForm')">确 定</el-button>
          <el-button @click="closeDiglog">取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
</template>
<script>
    export default {
        name: "projectDialog",
        data() {
            return {
                dialogVisible: true,
              ruleForm: {
                name: '',
                delivery: false,
                type: [],
                desc: ''
              },
              rules: {
                name: [
                  { required: true, message: '请输入活动名称', trigger: 'blur' },
                  { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
                ],
                type: [
                  { type: 'array', required: true, message: '请至少选择一个活动性质', trigger: 'change' }
                ],
                desc: [
                  { required: true, message: '请填写活动形式', trigger: 'blur' }
                ]
              }
            };
        },
        methods: {
            closeDiglog() {
                this.$emit('cancel', {})
            }
        }
    };
</script>
