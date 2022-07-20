import request from "../HttpCommon.js";

class ProjectApi {
  getProjects(data) {
    return request.get("/api/projects/list", data);
  }

  logout(data) {
    return request.delete("/api/users/login/", data);
  }

  register(data) {
    return request.post("/api/users/register", data);
  }
}

export default new ProjectApi();
