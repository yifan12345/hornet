<template>
    <div class="case" style="float: left">
        <div style="height: 50px">
            <div style="float: left;height:30px;line-height:35px;">
                <i style="align-content: center">项目：</i>
            </div>
            <div>
                <el-select v-model="projectValue"
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
        </div>

        <el-card style="width: 29%;float: left">
            <el-button
                    type="text"
                    icon="el-icon-circle-plus-outline"
                    @click="createRootModule"
            >根节点
            </el-button>
            <div style="margin-top:6px;">
                <el-tree
                        :data="moduleDate"
                        show-checkbox
                        default-expand-all
                        :expand-on-click-node="false"
                        :render-content="renderContent"
                        @node-click="nodeClick"
                >
                </el-tree>
            </div>
        </el-card>
        <div style="width: 70%;float: right">
            <el-table
                    :data="caseData"
                    border
                    style="width: 100%">
                <el-table-column
                        prop="id"
                        label="ID"
                        width="40">
                </el-table-column>
                <el-table-column
                        prop="name"
                        label="名称"
                        width="120">
                </el-table-column>
                <el-table-column
                        prop="module.name"
                        label="所属模块"
                        width="120">
                </el-table-column>
                <el-table-column
                        prop="method"
                        label="请求类型"
                        width="80">
                </el-table-column>
                <el-table-column
                        prop="url"
                        label="URL"
                        width="220">
                </el-table-column>
                <el-table-column
                        prop="create_time"
                        label="创建时间"
                        width="120">
                </el-table-column>
                <el-table-column
                        prop="update_time"
                        label="更新时间"
                        width="120">
                </el-table-column>
            </el-table>
        </div>
        <caseModuleDialog
                v-if="dialogFlag"
                :rootId="rootFlag"
                :pid="projectValue"
                :proLabel="projectLabel"
                :parentObj="parentObj"
                @cancel="closeDiglog"
        ></caseModuleDialog>
    </div>
    <!--引入子组件-->

</template>

<script>
    import ProjectApi from "../../request/project";
    import ModuleApi from "../../request/module";
    import caseModuleDialog from "./caseModuleDialog";

    export default {
        data() {
            return {
                rootFlag: true,
                dialogFlag: false,
                moduleDate: [],
                projectOptions: [],
                projectValue: 1,
                projectLabel: "",
                parentObj: {},
                caseData: []

            };
        },
        components: {
            caseModuleDialog
        },
        mounted() {
            this.initProjectlist()
            this.initModulelist(this.projectValue)
        },
        methods: {
            append(data) {
                this.parentObj = data
                this.dialogFlag = true
                this.rootFlag = false
            },
            remove(node, data) {
                ModuleApi.deleteModules(data.id).then(resp => {
                    if (resp.success === true) {
                        this.$message.success("删除成功！");
                        this.initModulelist(this.projectValue)
                    } else {
                        this.$message.error(resp.error.msg);
                    }
                })
            },
            renderContent(h, {node, data}) {
                return (
                    <span class="custom-tree-node">
                <span>{node.label}</span>
                <span>
                  <el-button size="mini" type="text" on-click={() => this.append(data)}>
                      <el-button
                          type="text"
                          icon="el-icon-circle-plus-outline"
                      />
                  </el-button>
                  <el-button size="mini" type="text" on-click={() => this.remove(node, data)}>
                      <el-button type="text" icon="el-icon-delete"/>
                  </el-button>
                </span>
              </span>);
            },
            //初始化项目列表
            async initProjectlist() {
                const resp = await ProjectApi.getProjects(this.req);
                if (resp.success === true) {
                    this.projectValue = resp.items[0].id;
                    this.projectLabel = resp.items[0].name;
                    for (let i = 0; i < resp.items.length; i++) {
                        this.projectOptions.push({
                            value: resp.items[i].id,
                            label: resp.items[i].name,
                        })
                    }
                }
            },
            //修改选中的项目
            changeProject(value) {
                this.initModulelist(value)
                this.projectLabel = this.projectOptions.find(item => item.value === value).label;
                this.projectValue = value

            },
            //查询模块列表
            async initModulelist(pid) {
                const req = {project_id: pid};
                const resp = await ModuleApi.getProModule(req);
                if (resp.success === true) {
                    this.moduleDate = resp.items
                }
            },
            //创建根节点模块
            createRootModule() {
                this.dialogFlag = true
                this.rootFlag = true
            },
            //创建模块关闭
            closeDiglog() {
                this.dialogFlag = false;
                this.parentObj = {}
                this.initModulelist(this.projectValue);
            },
            handleClick(row) {
                console.log(row);
            },
            nodeClick(data){
                console.log(data)
                this.getCaselist(data.id)
            },
            //初始化用例列表
            async getCaselist(mid) {
                const resp = await ModuleApi.getModuleCases(mid);
                if (resp.success === true) {
                    this.caseData = resp.items
                    this.$message.success("查询成功");
                }
            },
        },

    };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .custom-tree-node {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-size: 14px;
        padding-right: 8px;
    }

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
