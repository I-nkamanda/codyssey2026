Run 'docker --help' for more information
ersatzvitamin9579@c4r3s1 codyssey2026 % docker --help
Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Common Commands:
  run         Create and run a new container from an image 
  ㄴ> docker 이미지를 불러와서 이미지 기반으로 컨테이너를 만들고 실행한다.
  ㄴ> 형태: `docker run -p 3000:80 my-app`: 
    ㄴ> docker run (컨테이너 run 할게) | -p 3000:80 (포트 맵핑-호스트3000:컨테이너80)| my-app이라는 이름으로
  exec        Execute a command in a running container
  ㄴ> 이미 돌아가고 있는 컨테이너 안에서 커맨드를 실행한다.
  ps          List containers
  ㄴ> **p**rocess **s**tatus 여서 ps라고 한다. 현재 실행중인 컨테이너의 상태를 보여준다. (linux에서도 같은 명령어를 쓴다.)
  ㄴ> ps -a 하면 all을 보여달라는 거니까 중지되거나 종료된 컨테이너도 함께 볼 수 있다.
  build       Build an image from a Dockerfile
  ㄴ> Dockerfile을 읽어서 실행 가능한 이미지(image)를 생성한다.
  ㄴ> 형태: `docker build -t my-app`
  bake        Build from a file
  ㄴdocker image 다수를 한 번에 build 할 수 있는 명령어.
  pull        Download an image from a registry
  ㄴ> 이미 있는 도커 이미지를 가져온다
  push        Upload an image to a registry
  images      List images
  login       Authenticate to a registry
  logout      Log out from a registry
  search      Search Docker Hub for images
  version     Show the Docker version information
  info        Display system-wide information

Management Commands:
  builder     Manage builds
  buildx*     Docker Buildx
  compose*    Docker Compose
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  plugin      Manage plugins
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Swarm Commands:
  swarm       Manage Swarm

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  import      Import the contents from a tarball to create a filesystem image
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

Global Options:
      --config string      Location of client config files (default
                           "/Users/ersatzvitamin9579/.docker")
  -c, --context string     Name of the context to use to connect to the daemon
                           (overrides DOCKER_HOST env var and default context set
                           with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host string        Daemon socket to connect to
  -l, --log-level string   Set the logging level ("debug", "info", "warn", "error",
                           "fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default
                           "/Users/ersatzvitamin9579/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default
                           "/Users/ersatzvitamin9579/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default
                           "/Users/ersatzvitamin9579/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Run 'docker COMMAND --help' for more information on a command.