<template>
    <div class="case">
        <el-select v-model="value"
                   placeholder="请选择项目"
                   @change="changeProject">
            <el-option
                v-for="item in projectOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
        </el-select>
    </div>
</template>

<script>
    import ProjectApi from "../../request/project";
    import ModuleApi from "../../request/module";

    export default {
        data() {
            return {
                projectOptions: [
                    {
                        value:"",
                        label:""
                    }
                ],
                value:""

            };
        },
        mounted() {
          this.initProjectlist()
        },
        methods: {
            //初始化项目列表
            async initProjectlist() {
                const resp = await ProjectApi.getProjects(this.req);
                if (resp.success === true) {
                    for (let i = 0; i < resp.items.length; i++) {
                        this.projectOptions.push({
                            value: resp.items[i].id,
                            label: resp.items[i].name,
                        })
                    }
                    console.log("-------->",this.projectOptions)
                }
            },
            //修改选中的项目
            changeProject(value) {
                this.initModulelist(value)
            },
            //查询模块列表
            async initModulelist(pid) {
                const req = {project_id:pid};
                const resp = await ModuleApi.getProModule(req);
                if (resp.success === true) {

                    console.log("-------->",resp)
                }
            },
        }
    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h3 {
        margin: 40px 0 0;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        display: inline-block;
        margin: 0 10px;
    }
    a {
        color: #42b983;
    }
</style>
