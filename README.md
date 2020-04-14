# NaturalSelection

### WIP

Projet to run simple simulation of natural selection\
Flask web application\
Docker\
Python code

### Install docker
Follow the instructions here to install docker-ce https://docs.docker.com/install/linux/docker-ce/ubuntu/

After, run these commands so you do not need to use sudo to run docker
```bash
> sudo usermod -aG docker your_name
> newgrp docker
```

### Install docker-compose
```bash
> sudo curl -L https://github.com/docker/compose/releases/download/1.25.4/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
> sudo chmod +x /usr/local/bin/docker-compose
```

### Start the application
```bash
> docker-compose up --build
```
You can access the web app at: http://localhost:5000/

### Lint Code with Flake8
The flake8 linter can be run to lint the python code and enforce code quality rules (PEP8).

```bash
> docker-compose -f docker-compose.lint.yml up --build
```

