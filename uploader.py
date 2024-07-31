import os
import sys
import subprocess
import json

def upload_docker_images(source_image,target_image,registry_url, username, password):
    # 登录到 Docker Registry
    login_command = f"docker login {registry_url} -u {username} -p {password}"
    subprocess.run(login_command, shell=True, check=True)
    
    # 打标签并推送镜像
    pull_command = f"docker pull {source_image}"
    tag_command = f"docker tag {source_image} {target_image}"
    push_command = f"docker push {target_image}"
    save_command = f"docker save {source_image} -o images/test"
    
    
    subprocess.run(pull_command, shell=True, check=True)
    #subprocess.run(save_command, shell=True, check=True)
    subprocess.run(tag_command, shell=True, check=True)
    subprocess.run(push_command, shell=True, check=True)
    
    # 登出 Docker Registry
    logout_command = f"docker logout {registry_url}"
    subprocess.run(logout_command, shell=True, check=True)

if __name__ == "__main__":
  username = sys.argv[1]
  password = sys.argv[2]
  registry_url = sys.argv[3]
  # 读取 JSON 文件
  with open('images.json') as file:
      images = json.load(file)
      for i in images:
          print("docker push %s" %(i["target"]))
          upload_docker_images(i["source"], i["target"],registry_url, username, password)
