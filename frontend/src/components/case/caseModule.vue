<template>

    <div class="case" style="float: left">
        <div style="height: 50px">
            <div style="float: left;height:30px;line-height:35px;" >
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

        <el-card style="width: 300px">
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
                        node-key="id"
                        default-expand-all
                        :expand-on-click-node="false"
                        :render-content="renderContent">
                </el-tree>
            </div>
        </el-card>
        <caseModuleDialog
                v-if="dialogFlag"
                :rootId = "rootFlag"
                :pid="projectValue"
                :plabel = "projectLabel"
                @cancel="closeDiglog"
        ></caseModuleDialog>
    </div>
    <!--引入子组件-->

</template>

<script>
    let id = 1000;
    import ProjectApi from "../../request/project";
    import ModuleApi from "../../request/module";
    import caseModuleDialog from "./caseModuleDialog";

    export default {
        data() {
            const data = [];
            return {
                rootFlag:true,
                dialogFlag: false,
                moduleDate: [],
                projectOptions: [],
                projectValue: 1,
                projectLabel: "",

                data: JSON.parse(JSON.stringify(data)),
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
                const newChild = {id: id++, label: 'testtest', children: []};
                if (!data.children) {
                    this.$set(data, 'children', []);
                }
                data.children.push(newChild);
            },
            remove(node, data) {
                const parent = node.parent;
                const children = parent.data.children || parent.data;
                const index = children.findIndex(d => d.id === data.id);
                children.splice(index, 1);
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
                    console.log("-------->", this.projectOptions)
                }
            },
            //修改选中的项目
            changeProject(value) {
                this.initModulelist(value)
                this.projectLabel = this.projectOptions.find(item => item.value === value).label;
                this.projectValue = value
                console.log("选择项目名称",this.projectLabel)
            },
            //查询模块列表
            async initModulelist(pid) {
                const req = {project_id: pid};
                const resp = await ModuleApi.getProModule(req);
                if (resp.success === true) {
                    this.moduleDate = resp.items

                    console.log("-------->", resp)
                    console.log("-------->", this.moduleDate)

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
                this.initModulelist(this.projectValue);
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
