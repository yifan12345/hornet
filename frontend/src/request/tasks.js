import request from "../HttpCommon.js";

class TasksApi {
  createTasks(data) {
    return request.post("/api/tasks/", data);
  }
  getTasksList(data) {
    return request.get("/api/tasks/list", data);
  }
  getTaskDetail(tid){
    return request.get("/api/tasks/"+tid+"/")
  }
}

export default new TasksApi();
