import request from "../HttpCommon.js";

class ModuleApi {
  getProModule(data) {
    return request.get("/api/modules/tree", data);
  }

  createModules(data) {
    return request.post("/api/modules/", data);
  }

  getProject(id) {
    return request.get("/api/projects/" + id + "/");
  }

  delProject(id) {
    return request.delete("/api/projects/" + id + "/");
  }

  updateProject(id, data) {
    return request.put("/api/projects/" + id + "/", data);
  }
}

export default new ModuleApi();
